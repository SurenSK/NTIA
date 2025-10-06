import os
import re
import torch
import numpy as np
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer

FILE_PATH = "spec_nodes.md"
MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
WINDOW = 100
MIN_TOKENS = 5
HALF_WINDOW_FOR_NOVELTY = 12
TARGET_K = 72
MIN_SEG_LEN = 6
BATCH_SIZE = 64

def sentence_split(text):
    return re.split(r'(?<=[\.!?])\s+(?=[\"\'\(\[]?[A-Z0-9])', text)

def merge_short_sentences(sentences, tokenizer, min_tokens):
    merged = []
    for s in sentences:
        if not s or not s.strip():
            continue
        tok_len = len(tokenizer(s, add_special_tokens=False).input_ids)
        if merged and tok_len < min_tokens:
            merged[-1] = (merged[-1] + " " + s).strip()
        else:
            merged.append(s.strip())
    return merged

with open(FILE_PATH, "r", encoding="utf-8") as f:
    full_text = f.read()

raw_sentences = sentence_split(full_text)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
sentences = merge_short_sentences(raw_sentences, tokenizer, MIN_TOKENS)
N = len(sentences)
if N == 0:
    raise RuntimeError("No sentences after preprocessing.")

device = "cuda" if torch.cuda.is_available() else "cpu"
embed_model = SentenceTransformer(MODEL_NAME, device=device)
emb = embed_model.encode(sentences, convert_to_tensor=True, show_progress_bar=True, batch_size=BATCH_SIZE)
emb = torch.nn.functional.normalize(emb, p=2, dim=1)

G = np.zeros((N, N), dtype=np.float32)
with torch.no_grad():
    for i in range(N):
        j0 = max(0, i - WINDOW)
        j1 = min(N, i + WINDOW + 1)
        sims = torch.matmul(emb[j0:j1], emb[i]).cpu().numpy()
        idx = np.arange(j0, j1)
        G[i, idx] = sims
        G[idx, i] = sims
np.fill_diagonal(G, 0.0)

def integral_image(A):
    II = np.zeros((A.shape[0] + 1, A.shape[1] + 1), dtype=np.float64)
    II[1:, 1:] = np.cumsum(np.cumsum(A, axis=0), axis=1)
    return II

def rect_sum(II, r0, c0, r1, c1):
    return II[r1 + 1, c1 + 1] - II[r0, c1 + 1] - II[r1 + 1, c0] + II[r0, c0]

def square_sum(II, a, b):
    return rect_sum(II, a, a, b, b)

def novelty_curve(G, m):
    II = integral_image(G)
    n = G.shape[0]
    nov = np.zeros(n, dtype=np.float64)
    for t in range(m, n - m):
        L0 = t - m
        L1 = t - 1
        R0 = t
        R1 = t + m - 1
        tl = square_sum(II, L0, L1)
        br = square_sum(II, R0, R1)
        tr = rect_sum(II, L0, R0, L1, R1)
        bl = rect_sum(II, R0, L0, R1, L1)
        nov[t] = (tl + br) - (tr + bl)
    denom = (m * m) + (m * m)
    if denom > 0:
        nov /= denom
    return nov

nov = novelty_curve(G, HALF_WINDOW_FOR_NOVELTY)
if nov.max() > 0:
    nov = (nov - nov.min()) / (nov.max() - nov.min() + 1e-8)

def smooth(x, w):
    if w <= 1:
        return x
    k = np.ones(w, dtype=np.float64) / w
    return np.convolve(x, k, mode="same")

nov_smooth = smooth(nov, 5)

def select_peaks(values, num_peaks, min_distance):
    candidates = np.where((values[1:-1] > values[:-2]) & (values[1:-1] >= values[2:]))[0] + 1
    order = candidates[np.argsort(values[candidates])[::-1]]
    selected = []
    for idx in order:
        if len(selected) >= num_peaks:
            break
        if all(abs(idx - s) >= min_distance for s in selected):
            selected.append(idx)
    selected = np.array(sorted(selected), dtype=int)
    return selected.tolist()

num_cuts = max(0, min(TARGET_K - 1, N - 1))
cut_indices = select_peaks(nov_smooth, num_cuts, MIN_SEG_LEN)

plt.figure(figsize=(12, 12))
plt.imshow(G, cmap="hot", interpolation="nearest", vmin=0.0, vmax=1.0)
for c in cut_indices:
    plt.axvline(c + 0.5, color="cyan", linewidth=0.6, alpha=0.7)
    plt.axhline(c + 0.5, color="cyan", linewidth=0.6, alpha=0.7)
plt.colorbar(label="Cosine Similarity")
plt.title(f'Banded Self-Similarity Matrix (±{WINDOW}) with Novelty Cuts of {N} Sentence Units')
plt.xlabel('Unit Index')
plt.ylabel('Unit Index')
plt.savefig('spec_similarity_heatmap_banded_sentences_with_cuts.png', dpi=300, bbox_inches='tight')

plt.figure(figsize=(12, 3))
plt.plot(nov_smooth, linewidth=1.0)
plt.scatter(cut_indices, nov_smooth[cut_indices], s=12)
plt.title('Novelty Curve with Selected Cut Points')
plt.xlabel('Unit Index')
plt.ylabel('Novelty')
plt.tight_layout()
plt.savefig('novelty_curve.png', dpi=300, bbox_inches='tight')

print(f"Found {len(cut_indices)} cuts. First 10: {cut_indices[:10]}")
print("Saved: spec_similarity_heatmap_banded_sentences_with_cuts.png and novelty_curve.png")
