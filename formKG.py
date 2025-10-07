import os
import re
import torch
import numpy as np
import matplotlib.pyplot as plt
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b")
windowSz = 1000
windowStride = windowSz//2
batchSz = 16
negativeRelationship = False

FILE_PATH = "spec_nodes.md"
with open(FILE_PATH, "r", encoding="utf-8") as f:
    text = f.read()
    tks = tokenizer.encode(text)

# Canonical list of objects for your graph.
# This would replace the `objects = []` line in your script.
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

relationships = ['HAS_PART', 'PERFORMS', 'DEPENDS_ON', 'SENDS', 'CONFIGURES', 'IMPLEMENTS', 'CONSTRAINED_BY']
if negativeRelationship: relationships.append('HAS_NO_RELATION_TO')
outputs = [f"{s} {r} {o}" for s in objects for o in objects for r in relationships]
outputs = tokenizer(outputs, padding=False, add_special_tokens=False)

def scoreRelationships(window): # -> List of floats of length len(relationships), len(objects), len(objects)
    prompt = f"Based on the following text from a technical specification, extract a single relationship in the format 'Subject Relation Object'.\n\ntext: \"{tokenizer.decode(window)}\"\n\nExtracted Relationship: "
    prompt = tokenizer(prompt, padding=False, add_special_tokens=False)
    nlls = [] # we get the teacher forced loss when given the text
    for i in range(0, len(outputs), batchSz):
        outputsSel = outputs[i:i+batchSz]
        full_texts = [prompt + o for o in outputsSel] # send to device
        labels = prompt.input_ids.clone()
        for j in range(len(full_texts)):
            labels[j, :len(prompt.input_ids[j])] = -100
        labels[prompt.attention_mask == 0] = -100
        with torch.no_grad():
            logits = model(**full_texts).logits
        B, S, V = logits.shape
        log_probs_per_token = -F.cross_entropy(logits.view(B*S,V), labels.view(B*S), reduction='none').view(B,S)
        log_probs = log_probs_per_token.sum(dim=1)
        _nlls = (log_probs).tolist()
        nlls.extend(_nlls)
    return nlls

res = []
for w in range(0, len(tks)-windowSz, windowStride):
    selTks = tks[w:w+windowSz]
    scores = scoreRelationships(selTks)
    res.append(torch.tensor(scores).view(len(relationships), len(objects), len(objects)))

res = torch.stack(res).rename('window', 'relationship', 'source', 'dest')
res = res.max(dim='window').values
res = res.argmax(dim='relationship')