import os
import sys
import torch
import torch.nn.functional as F
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM

gpu_num = int(sys.argv[1])
num_gpus = int(sys.argv[2])

tokenizer = AutoTokenizer.from_pretrained("openai/gpt-oss-20b")
if tokenizer.pad_token_id is None:
    tokenizer.pad_token = tokenizer.eos_token
tokenizer.truncation_side = "left"

model = AutoModelForCausalLM.from_pretrained(
    "openai/gpt-oss-20b",
    dtype=torch.bfloat16,
    device_map="auto",
)
model.eval()

windowSz = 3072
windowStride = windowSz // 2
batchSz = 4
negativeRelationship = False

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

def scoreRelationships(window_tokens):
    window_text = tokenizer.decode(window_tokens, skip_special_tokens=True)
    user_contents = [f'Based on the text provided, identify the relationship between the subject and object.\n\nText: "{window_text}"\n\nSubject: {s}\nObject: {o}\nRelationship:' for s in objects for o in objects]
    user_prompts_as_messages = [[{"role": "user", "content": c}] for c in user_contents]
    def prompt_len(msg):
        ids = tokenizer.apply_chat_template(msg, add_generation_prompt=True, tokenize=True)
        return len(ids) if isinstance(ids, list) else ids.shape[-1]
    user_prompt_token_lens = [prompt_len(p) for p in user_prompts_as_messages]
    relation_scores = []
    for rel in relationships:
        all_messages_for_rel = [[{"role": "user", "content": user_content}, {"role": "assistant", "content": f" {rel}"}] for user_content in user_contents]
        scores_for_rel = []
        for i in range(0, len(all_messages_for_rel), batchSz):
            batch_messages = all_messages_for_rel[i : i + batchSz]
            batch_prompt_lens = user_prompt_token_lens[i : i + batchSz]
            rendered = [tokenizer.apply_chat_template(m, add_generation_prompt=False, tokenize=False) for m in batch_messages]
            enc = tokenizer(
                rendered,
                padding=True,
                truncation=True,
                max_length=model.config.max_position_embeddings,
                return_tensors="pt",
            )
            inputs = {k: v.to(model.device) for k, v in enc.items()}
            labels = inputs["input_ids"].clone()
            for j in range(len(batch_messages)):
                labels[j, : batch_prompt_lens[j]] = -100
            labels[inputs["attention_mask"] == 0] = -100
            with torch.inference_mode(), torch.autocast(device_type="cuda", dtype=torch.bfloat16):
                logits = model(**inputs).logits
            B, S, V = logits.shape
            log_probs = -F.cross_entropy(logits.view(B * S, V), labels.view(B * S), reduction="none", ignore_index=-100).view(B, S)
            completion_tokens = (labels != -100).sum(dim=1).clamp(min=1)
            seq_log_probs = log_probs.sum(dim=1) / completion_tokens
            scores_for_rel.extend(seq_log_probs.detach().cpu().tolist())
        relation_scores.append(torch.tensor(scores_for_rel).view(len(objects), len(objects)))
    return torch.stack(relation_scores).flatten().tolist()

all_window_scores = []
window_starts = list(range(0, len(tks) - windowSz, windowStride))
for w in tqdm(window_starts[gpu_num::num_gpus]):
    selTks = tks[w : w + windowSz]
    scores = scoreRelationships(selTks)
    all_window_scores.append(torch.tensor(scores).view(len(relationships), len(objects), len(objects)))

res = torch.stack(all_window_scores)
torch.save(res, f"res_gpu_{gpu_num}.pt")
