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
    attn_implementation="flash_attention_2"
)
model.eval()

windowSz = 3000
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
so_pairs = [(s, o) for s in objects for o in objects]

def dissect_template(tokenizer):
    # Find user turn tokens
    c = [{"role": "user", "content": "DUMMY"}]
    s = tokenizer.apply_chat_template(c, tokenize=False)
    pre, post = s.split("DUMMY")
    user_prefix_t = tokenizer.encode(pre, add_special_tokens=False)
    user_suffix_t = tokenizer.encode(post, add_special_tokens=False)
    
    # Find tokens between user and assistant
    c = [{"role": "user", "content": "A"}, {"role": "assistant", "content": "B"}]
    s = tokenizer.apply_chat_template(c, tokenize=False)
    s_user = tokenizer.apply_chat_template(c[:1], tokenize=False)
    s_asst = "B" # The content of the assistant message is B
    separator = s.replace(s_user, "").replace(s_asst, "")
    asst_prefix_t = tokenizer.encode(separator, add_special_tokens=False)

    # Find assistant turn suffix
    c = [{"role": "user", "content": "A"}, {"role": "assistant", "content": "DUMMY"}]
    s = tokenizer.apply_chat_template(c, tokenize=False)
    _, post = s.split("DUMMY")
    asst_suffix_t = tokenizer.encode(post, add_special_tokens=False)
    
    return {
        "user_prefix": torch.tensor(user_prefix_t, dtype=torch.long),
        "user_suffix": torch.tensor(user_suffix_t, dtype=torch.long),
        "asst_prefix": torch.tensor(asst_prefix_t, dtype=torch.long),
        "asst_suffix": torch.tensor(asst_suffix_t, dtype=torch.long),
    }

template_parts = dissect_template(tokenizer)
rel_token_map = {
    rel: tokenizer.encode(f" {rel}", add_special_tokens=False) 
    for rel in relationships
}
so_token_map = {
    (s, o): tokenizer.encode(f"Subject: {s}\nObject: {o}\nRelationship:", add_special_tokens=False)
    for s, o in so_pairs
}

import copy
import torch
import torch.nn.functional as F
from transformers import StaticCache
from tqdm import tqdm

def scoreRelationships(window_tokens):
    # This function assumes the following variables are defined in the global scope:
    # tokenizer, model, template_parts, so_token_map, rel_token_map,
    # relationships, so_pairs, batchSz

    window_text = tokenizer.decode(window_tokens, skip_special_tokens=True)
    shared_prefix = f'Based on the text provided, identify the relationship between the subject and object.\n\nText: "{window_text}"\n\n'
    shared_prefix_t = torch.tensor(tokenizer.encode(shared_prefix, add_special_tokens=False), dtype=torch.long)
    
    tokens_to_cache = torch.cat([
        template_parts["user_prefix"],
        shared_prefix_t
    ]).to(model.device).unsqueeze(0)
    
    base_cache = StaticCache(config=model.config, max_batch_size=batchSz, max_cache_len=model.config.max_position_embeddings, device=model.device, dtype=torch.bfloat16)
    with torch.inference_mode(), torch.autocast(device_type="cuda", dtype=torch.bfloat16):
        outputs = model(input_ids=tokens_to_cache, attention_mask=torch.ones_like(tokens_to_cache), past_key_values=base_cache, use_cache=True)
        base_cache = outputs.past_key_values
    
    relation_scores = []
    for rel in tqdm(relationships, desc="Relationships"):
        scores_for_rel = []
        rel_t_list = rel_token_map[rel]
        rel_len = len(rel_t_list)
        
        for i in range(0, len(so_pairs), batchSz):
            batch_so = so_pairs[i:i+batchSz]
            
            batch_input_ids = []
            batch_labels = []
            for s, o in batch_so:
                so_t = torch.tensor(so_token_map[(s, o)], dtype=torch.long)
                rel_t = torch.tensor(rel_t_list, dtype=torch.long)
                
                input_ids = torch.cat([
                    so_t,
                    template_parts["user_suffix"],
                    template_parts["asst_prefix"],
                    rel_t,
                    template_parts["asst_suffix"]
                ])
                batch_input_ids.append(input_ids)

                labels = input_ids.clone()
                labels[:-rel_len] = -100
                batch_labels.append(labels)

            padded_input_ids = torch.nn.utils.rnn.pad_sequence(batch_input_ids, batch_first=True, padding_value=tokenizer.pad_token_id).to(model.device)
            padded_labels = torch.nn.utils.rnn.pad_sequence(batch_labels, batch_first=True, padding_value=-100).to(model.device)
            
            full_attention_mask = torch.ones(
                (padded_input_ids.shape[0], tokens_to_cache.shape[1] + padded_input_ids.shape[1]),
                dtype=torch.long, 
                device=model.device
            )
            inputs = {'input_ids': padded_input_ids, 'attention_mask': full_attention_mask}
            
            cache_copy = copy.deepcopy(base_cache)
            with torch.inference_mode(), torch.autocast(device_type="cuda", dtype=torch.bfloat16):
                logits = model(**inputs, past_key_values=cache_copy).logits
            
            B, S, V = logits.shape
            log_probs = -F.cross_entropy(logits.view(B*S, V), padded_labels.view(B*S), reduction="none", ignore_index=-100).view(B, S)
            completion_tokens = (padded_labels != -100).sum(dim=1).clamp(min=1)
            seq_log_probs = log_probs.sum(dim=1) / completion_tokens
            scores_for_rel.extend(seq_log_probs.detach().cpu().tolist())
            
        relation_scores.append(torch.tensor(scores_for_rel).view(len(objects), len(objects)))
        
    return torch.stack(relation_scores).flatten().tolist()

# all_window_scores = []
window_starts = list(range(0, len(tks) - windowSz, windowStride))
for w in tqdm(window_starts[gpu_num::num_gpus]):
    selTks = tks[w : w + windowSz]
    scores = scoreRelationships(selTks)
    torch.save(torch.tensor(scores).view(len(relationships), len(objects), len(objects)), f'res_{w}.pt')
    
# res = torch.stack(all_window_scores)
# torch.save(res, f"res_gpu_{gpu_num}.pt")