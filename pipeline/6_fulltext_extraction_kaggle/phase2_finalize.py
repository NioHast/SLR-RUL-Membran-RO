"""
phase2_finalize.py - Finalize per-paper analysis + update the corpus (stage 6).

Purpose:
    After `phase2_assemble.py` has built each per-paper folder, run this to:
      (1) write a human-readable `analysis.txt` per paper (title, authors, venue,
          visual-evidence counts, dimension flags, abstract snippet);
      (2) copy the full-text dimension flags (d1..d8) back into the corpus;
      (3) rewrite `corpus_a.json` and produce `_INDEX.csv` (one row per paper).

INPUT:
    - ROOT/source_code/data/corpus_a.json          : the corpus (paper list).
    - ROOT/deliverables/per_paper/<slug>/extraction.json : per-paper summary
      produced by phase2_assemble.py.
    - ROOT/deliverables/per_paper/<slug>/text.md   : Marker markdown (for abstract).

OUTPUT:
    - ROOT/deliverables/per_paper/<slug>/analysis.txt (overwritten per paper).
    - ROOT/source_code/data/corpus_a.json             (rewritten with full-text dims).
    - ROOT/deliverables/per_paper/_INDEX.csv          (index of all kept folders).

How to run:
        python3 phase2_finalize.py
    Run AFTER phase2_assemble.py has finished.

NOTE:
    Paths are absolute: ROOT="/home/nioha/Downloads/SLR" MUST be adjusted to your
    own working location before running.
"""

import json, os, re, glob

# --- Absolute paths (CHANGE ME to match your own working location) ---
ROOT = "/home/nioha/Downloads/SLR"; PP = os.path.join(ROOT, "deliverables", "per_paper")
corpus = json.load(open(os.path.join(ROOT, "source_code", "data", "corpus_a.json")))

idx = []

# --- Walk every corpus paper and finalize the ones whose folder exists ---
for r in corpus:
    slug = f'{r["no"]:03d}_' + re.sub(r'[^A-Za-z]+', '_', (r.get("penulis", "?") or "?").split(" ")[0]) + f'_{r.get("tahun","")}'
    d = os.path.join(PP, slug)
    if not os.path.isdir(d): continue

    # Load the per-paper extraction summary written by phase2_assemble.py
    ext = json.load(open(os.path.join(d, "extraction.json")))
    txt = ""
    tp = os.path.join(d, "text.md")
    if os.path.exists(tp): txt = open(tp, encoding="utf-8", errors="replace").read()

    # abstract snippet: grab the opening text after "Abstract" up to the next heading
    ab = ""
    m = re.search(r'[Aa]bstract[^\n]*[\n\s]+(.{200,1200}?)(\n#|\n\*?Index Terms|Keywords)', txt, re.S)
    if m: ab = re.sub(r'\s+', ' ', m.group(1)).strip()[:600]

    # Assemble the human-readable analysis.txt block-by-block
    lines = []
    lines.append(f'PAPER {r["no"]}: {r.get("judul")}')
    lines.append(f'Penulis: {r.get("penulis")} ({r.get("tahun")}) | {r.get("jurnal")} | {r.get("klasifikasi")} | DOI {r.get("doi")}')
    lines.append(f'Pilar: {r.get("pilar")}')
    ev = ext.get("bukti_visual", {})
    lines.append(f'Bukti full-text: figures={ev.get("figures")}, equations={ev.get("equations")}, table_rows={ev.get("table_rows")}')
    dm = ext.get("dimensi", {}); lines.append("Dimensi (full-text): " + ", ".join(k for k, v in dm.items() if v))
    if ab: lines.append("Abstrak (potongan): " + ab)
    lines.append("(Ringkasan & kontribusi rinci: lihat SLR_Korpus.xlsx)")
    open(os.path.join(d, "analysis.txt"), "w", encoding="utf-8").write("\n".join(lines))

    # update corpus dims from full-text: overwrite d1..d8 with the full-text flags
    for k in ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8"]:
        if dm.get(k): r[k] = "1"
        else: r[k] = ""   # use full-text
    idx.append({"no": r["no"], "slug": slug, "doi": r.get("doi"), "kuartil": r.get("klasifikasi"), "pilar": r.get("pilar"), "figures": ev.get("figures"), "equations": ev.get("equations")})

# --- Persist the updated corpus ---
json.dump(corpus, open(os.path.join(ROOT, "source_code", "data", "corpus_a.json"), "w"), ensure_ascii=False, indent=1)

# --- Write the index CSV (one row per finalized paper folder) ---
import csv
with open(os.path.join(PP, "_INDEX.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(idx[0].keys())); w.writeheader(); w.writerows(idx)

# --- Print a quick dimension summary over the whole corpus ---
import collections
dims = {f"d{i}": sum(1 for r in corpus if r.get(f"d{i}")) for i in range(1, 9)}
print("folder:", len(idx), "| dims (full-text):", dims)
