import os
import re
import torch
import numpy as np
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b")
windowSz = 1000
windowStride = windowSz//2

FILE_PATH = "spec_nodes.md"
with open(FILE_PATH, "r", encoding="utf-8") as f:
    text = f.read()
    tks = tokenizer.encode(text)

objects = []
relationships = []

batchSz = 16
def scoreRelationships(window): # -> List of floats of length len(relationships), len(objects), len(objects)
    prompts = [] # form the List of strings of length len(relationships), len(objects), len(objects)
    promptTks = tokenizer.encode(prompts) # tokenized prompts
    nlls = [] # we get the teacher forced loss when given the text
    for i in range(0, len(prompts)-batchSz, batchSz):
        selPrompts = prompts[i:i+batchSz]
        _nlls = [] # llm stuff, tbd
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