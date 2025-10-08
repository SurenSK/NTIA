import os
import sys
import torch
import torch.nn.functional as F
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers.cache_utils import DynamicCache

gpu_num = int(sys.argv[1])
num_gpus = int(sys.argv[2])

tokenizer = AutoTokenizer.from_pretrained("openai/gpt-oss-20b")
if tokenizer.pad_token_id is None:
    tokenizer.pad_token = tokenizer.eos_token
tokenizer.truncation_side = "left"
tokenizer.padding_side = "right"

model = AutoModelForCausalLM.from_pretrained(
    "openai/gpt-oss-20b",
    dtype=torch.bfloat16,
    device_map="auto",
)
model.eval()
torch.set_grad_enabled(False)

windowSz = 2048
windowStride = windowSz // 2
pairBatchSz = 1
relsChunkSz = 1

FILE_PATH = "spec_nodes.md"
with open(FILE_PATH, "r", encoding="utf-8") as f:
    text = f.read()
    tks = tokenizer.encode(text)

objects = [
    "SMO",
    "Non-Real Time RIC",
    "Near-Real Time RIC",
    "O-Cloud",
    "gNB",
    "O-CU",
    "O-CU-CP",
    "O-CU-UP",
    "O-DU",
    "O-RU",
    "O-CU-CP: OAM-Agent",
    "O-CU-CP: gNB Procedure Management",
    "O-CU-CP: Cell Procedure Management",
    "O-CU-CP: UE Procedure Management",
    "O-CU-CP: RRC Encoder-Decoder",
    "O-CU-CP: NGAP Encoder-Decoder",
    "O-CU-CP: XnAP Encoder-Decoder",
    "O-CU-CP: F1AP Encoder-Decoder",
    "O-CU-UP: OAM-Agent",
    "O-CU-UP: eGTPU",
    "O-CU-UP: NR PDCP",
    "O-CU-UP: SDAP",
    "O-DU: L1 Functional Blocks",
    "O-DU: L2 Functional Blocks",
    "O-DU: OAM-Agent",
    "O-DU: E2 Handler",
    "O-DU: F1AP Handler",
    "O-DU: F1-U Handler",
    "O-DU: NR-RLC",
    "O-DU: NR-MAC",
    "O-DU: NR-Scheduler",
    "O-DU: Front Haul Module",
    "O-DU: Accelerator Abstraction Layer (AAL)",
    "Protocol: F1AP",
    "Protocol: NGAP",
    "Protocol: XnAP",
    "Protocol: E2AP",
    "Protocol: RRC",
    "Protocol: PDCP",
    "Protocol: SDAP",
    "Protocol: RLC",
    "Protocol: MAC",
    "Protocol: eGTP-U",
    "Spec: FAPI",
    "Spec: NETCONF",
    "Channel: PDSCH",
    "Channel: PUSCH",
    "Channel: PDCCH",
    "Channel: PUCCH",
    "Channel: PBCH",
    "Channel: PRACH",
    "Signal: DMRS",
    "Signal: SRS",
    "Signal: SSB",
    "Function: Synchronization",
    "Function: Beamforming",
    "Function: Handover",
    "Function: RAN Slicing",
    "Function: Network Energy Savings (NES)",
    "Procedure: UE Registration",
    "Procedure: RACH",
    "Procedure: PDU Session Establishment",
]

relationships = ["HAS_NO_RELATION_TO", "HAS_PART", "PERFORMS", "DEPENDS_ON", "SENDS", "CONFIGURES", "IMPLEMENTS", "CONSTRAINED_BY"]

const_prefix_ids = tokenizer("Based on the text provided, identify the relationship between the subject and object.\n\nText: \"", add_special_tokens=False).input_ids
const_after_window_ids = tokenizer("\"\n\nSubject: ", add_special_tokens=False).input_ids
const_between_so_ids = tokenizer("\nObject: ", add_special_tokens=False).input_ids
const_ending_ids = tokenizer("\nRelationship:", add_special_tokens=False).input_ids
label_ids_list = [tokenizer(" " + rel, add_special_tokens=False).input_ids for rel in relationships]
max_label_len = max(len(x) for x in label_ids_list)
labels_padded = torch.full((len(relationships), max_label_len), tokenizer.pad_token_id, dtype=torch.long)
labels_loss = torch.full((len(relationships), max_label_len), -100, dtype=torch.long)
for i, seq in enumerate(label_ids_list):
    L = len(seq)
    labels_padded[i, :L] = torch.tensor(seq, dtype=torch.long)
    labels_loss[i, :L] = torch.tensor(seq, dtype=torch.long)

def left_truncate(ids, maxlen):
    if len(ids) <= maxlen:
        return ids
    return ids[-maxlen:]

def build_base_ids(window_ids, subj, obj, maxlen):
    s_ids = tokenizer(subj, add_special_tokens=False).input_ids
    o_ids = tokenizer(obj, add_special_tokens=False).input_ids
    ids = const_prefix_ids + window_ids + const_after_window_ids + s_ids + const_between_so_ids + o_ids + const_ending_ids
    return left_truncate(ids, maxlen)

def pad_batch(seqs, pad_id):
    maxlen = max(len(s) for s in seqs)
    out = torch.full((len(seqs), maxlen), pad_id, dtype=torch.long)
    mask = torch.zeros((len(seqs), maxlen), dtype=torch.long)
    for i, s in enumerate(seqs):
        L = len(s)
        out[i, :L] = torch.tensor(s, dtype=torch.long)
        mask[i, :L] = 1
    return out, mask

def repeat_cache(past: DynamicCache, repeat_factor: int) -> DynamicCache:
    legacy = past.to_legacy_cache()
    rep_legacy = []
    for layer in legacy:
        rep_legacy.append(tuple(x.repeat_interleave(repeat_factor, dim=0) for x in layer))
    return DynamicCache.from_legacy_cache(rep_legacy)
def scoreRelationships(window_tokens):
    max_ctx = getattr(model.config, "max_position_embeddings", 4096)
    pairs = [(si, oi) for si in range(len(objects)) for oi in range(len(objects))]
    rel_scores = torch.empty(len(relationships), len(objects), len(objects), dtype=torch.float32)
    window_ids = window_tokens
    base_batches = [pairs[i:i+pairBatchSz] for i in range(0, len(pairs), pairBatchSz)]
    for batch_pairs in tqdm(base_batches):
        base_ids = [build_base_ids(window_ids, objects[si], objects[oi], max_ctx) for si, oi in batch_pairs]
        input_ids, attn_mask = pad_batch(base_ids, tokenizer.pad_token_id)
        input_ids = input_ids.to(model.device)
        attn_mask = attn_mask.to(model.device)
        with torch.inference_mode(), torch.autocast(device_type="cuda", dtype=torch.bfloat16):
            base_out = model(input_ids=input_ids, attention_mask=attn_mask, use_cache=True, return_dict=True)
        past = base_out.past_key_values
        P = input_ids.size(0)
        past_len = past.get_seq_length()
        for r0 in range(0, len(relationships), relsChunkSz):
            r1 = min(r0 + relsChunkSz, len(relationships))
            labels_in = labels_padded[r0:r1].to(model.device)
            labels_loss_in = labels_loss[r0:r1].to(model.device)
            Rb, T = labels_in.shape
            labels_in_rep = labels_in.unsqueeze(0).repeat(P, 1, 1).view(P * Rb, T)
            labels_loss_rep = labels_loss_in.unsqueeze(0).repeat(P, 1, 1).view(P * Rb, T)
            rep_past = repeat_cache(past, Rb)
            base_attn_rep = attn_mask.repeat_interleave(Rb, dim=0)
            ones_label = torch.ones((P * Rb, T), dtype=base_attn_rep.dtype, device=base_attn_rep.device)
            attn_mask_full = torch.cat([base_attn_rep, ones_label], dim=1)
            with torch.inference_mode(), torch.autocast(device_type="cuda", dtype=torch.bfloat16):
                out = model(input_ids=labels_in_rep, attention_mask=attn_mask_full, past_key_values=rep_past, use_cache=True, return_dict=True)
            B, T2, V = out.logits.shape
            flat_loss = F.cross_entropy(out.logits.reshape(B * T2, V), labels_loss_rep.reshape(B * T2), reduction="none", ignore_index=-100)
            token_mask = (labels_loss_rep != -100).to(out.logits.dtype)
            token_counts = token_mask.sum(dim=1).clamp(min=1)
            seq_log_probs = (-flat_loss.view(B, T2) * token_mask).sum(dim=1) / token_counts
            scores = seq_log_probs.view(P, Rb).transpose(0, 1).detach().cpu()
            for k, (si, oi) in enumerate(batch_pairs):
                rel_scores[r0:r1, si, oi] = scores[:, k]
    return rel_scores.flatten().tolist()


window_starts = list(range(0, len(tks) - windowSz, windowStride))
for w in tqdm(window_starts[gpu_num::num_gpus]):
    selTks = tks[w : w + windowSz]
    scores = scoreRelationships(selTks)
    torch.save(torch.tensor(scores).view(len(relationships), len(objects), len(objects)), f'res_{w}.pt')
