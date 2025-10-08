import os
import re
import sys
import torch
import numpy as np
import matplotlib.pyplot as plt
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM
gpu_num = int(sys.argv[1])
num_gpus = int(sys.argv[2])
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b", torch_dtype=torch.float16, device_map='auto')
windowSz = 5000
windowStride = windowSz//2
batchSz = 16
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
    "Procedure: PDU Session Establishment"
]
# check incose
# check attn > naive, low entropy
relationships = ['HAS_NO_RELATION_TO', 'HAS_PART', 'PERFORMS', 'DEPENDS_ON', 'SENDS', 'CONFIGURES', 'IMPLEMENTS', 'CONSTRAINED_BY']

def scoreRelationships(window_tokens):
    window_text = tokenizer.decode(window_tokens, skip_special_tokens=True)
    so_prompts = [f"Based on the text provided, identify the relationship between the subject and object.\n\nText: \"{window_text}\"\n\nSubject: {s}\nObject: {o}\nRelationship:" for s in objects for o in objects]
    prompt_lens = [len(tokenizer.encode(p, add_special_tokens=False)) for p in so_prompts]
    
    relation_scores = []
    for rel in relationships:
        full_texts = [p + " " + rel for p in so_prompts]
        scores_for_rel = []
        for i in range(0, len(full_texts), batchSz):
            batch_texts = full_texts[i:i + batchSz]
            batch_prompt_lens = prompt_lens[i:i + batchSz]
            inputs = tokenizer(batch_texts, padding=True, return_tensors="pt", add_special_tokens=False).to(DEVICE)
            labels = inputs.input_ids.clone()
            
            for j in range(len(batch_texts)):
                labels[j, :batch_prompt_lens[j]] = -100

            with torch.no_grad():
                logits = model(**inputs).logits
            
            B, S, V = logits.shape
            log_probs = -F.cross_entropy(logits.view(B * S, V), labels.view(B * S), reduction='none').view(B, S)
            completion_tokens = (labels != -100).sum(dim=1).clamp(min=1)
            seq_log_probs = log_probs.sum(dim=1) / completion_tokens
            scores_for_rel.extend(seq_log_probs.cpu().tolist())
        relation_scores.append(torch.tensor(scores_for_rel).view(len(objects), len(objects)))
    
    return torch.stack(relation_scores).flatten().tolist()

all_window_scores = []
window_starts = list(range(0, len(tks) - windowSz, windowStride))
for w in window_starts[gpu_num::num_gpus]:
    selTks = tks[w:w + windowSz]
    scores = scoreRelationships(selTks)
    all_window_scores.append(torch.tensor(scores).view(len(relationships), len(objects), len(objects)))

res = torch.stack(all_window_scores).rename('window', 'relationship', 'source', 'dest')
torch.save(res, f"res_gpu_{gpu_num}.pt")
