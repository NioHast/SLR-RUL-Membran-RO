#!/usr/bin/env python3
"""
classify_scopus.py
------------------
Assign the 'klasifikasi' field to every article in data/corpus_*.json based on
OFFICIAL sources derived from Scopus (SCImago):

  1) Primary  : mirror_data/sjr_quart.csv  -> "SJR Best Quartile" column (official, 2022 ed.)
  2) Supplement: mirror_data/sjr_all.csv    -> SJR 2024 (for new journals) -> quartile derived per field
  3) Fallback : "Belum terverifikasi (Non-Scopus/Prosiding?)"

Matching uses ISSN (print + electronic) via data/issn_map.json.

INPUT:
    - data/issn_map.json          (DOI -> ISSN map, output of issn.py).
    - ../mirror_data/sjr_quart.csv (SCImago 2022 ed.: "SJR Best Quartile" column).
    - ../mirror_data/sjr_all.csv   (SCImago panel 1999-2025).
OUTPUT:
    - data/corpus_*.json (rewritten; each article is given a "klasifikasi" field).
How to run:
        python3 classify_scopus.py
NOTE:
    Paths are computed relative to the location of this file (HERE/data and
    HERE/../mirror_data), so the folder structure must be kept. Other scripts in
    the pipeline use absolute paths (e.g. BASE="/tmp/opencode/slr") which you MUST
    change to your own working location.
"""

import json, glob, csv, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
MIR  = os.path.join(os.path.dirname(HERE), "mirror_data")

def norm(i):  return (i or "").replace("-", "").replace(" ", "").upper().strip()
def toks(c):  return [norm(t) for t in str(c or "").split(",") if norm(t)]

# --- 1) official SJR Best Quartile ---
# Build the ISSN -> official quartile info index.
idx = {}
with open(os.path.join(MIR, "sjr_quart.csv"), encoding="utf-8", errors="replace") as f:
    for row in csv.DictReader(f, delimiter=";"):
        info = {"q": (row.get("SJR Best Quartile") or "").strip(),
                "cov": row.get("Coverage"), "title": row.get("Title")}
        for t in toks(row.get("Issn")):
            idx[t] = info

# --- 2) SJR 2024 (derived quartile per field) ---
# `latest` stores the newest row per ISSN; `byf` groups SJR 2024 per field.
latest, byf = {}, collections.defaultdict(list)
with open(os.path.join(MIR, "sjr_all.csv"), encoding="utf-8", errors="replace") as f:
    for row in csv.DictReader(f):
        for t in toks(row.get("Issn")):
            latest.setdefault(t, row)
            if row.get("year") == "2024":
                try: s = float(row["SJR"])
                except Exception: continue
                byf[row.get("field")].append((s, t))
# Derive the quartile per field from the SJR 2024 ranking.
q24 = {}
for field, lst in byf.items():
    lst.sort(reverse=True); n = len(lst)
    for rank, (s, t) in enumerate(lst):
        q24[t] = min(4, int(rank / (max(n, 1) / 4.0)) + 1)

iss = json.load(open(os.path.join(DATA, "issn_map.json")))

# Manual override for journals that have been verified (journal name -> label).
SCOPUS_OVERRIDE_VERIFIED = {
    "Machine Learning with Applications": "Scopus Q1 (SCImago SJR Best Quartile)",
    "Cleaner Water": "Scopus Q2 (SCImago SJR Best Quartile)",
}

# --- 3) Classify each article ---
rows_all = []
for fp in sorted(glob.glob(os.path.join(DATA, "corpus_*.json"))):
    d = json.load(open(fp))
    for r in d:
        v = iss.get(r.get("doi", ""), {})
        cands = [v.get("issn_l")] + (v.get("issn") or [])
        # Priority 1: match to the official SJR Best Quartile.
        hit = next((norm(c) for c in cands if c and norm(c) in idx), None)
        if hit and idx[hit]["q"].startswith("Q"):
            r["klasifikasi"] = f"Scopus {idx[hit]['q']} (SCImago SJR Best Quartile)"
        else:
            # Priority 2: new journal -> use the SJR 2024 quartile (if available).
            c = next((norm(x) for x in cands if x and (norm(x) in q24 or norm(x) in latest)), None)
            if c and c in q24:
                r["klasifikasi"] = f"Scopus Q{q24[c]} (SCImago SJR 2024)"
            elif c:
                r["klasifikasi"] = "Scopus (SCImago; kuartil tak tersedia)"
            else:
                # Priority 3: not found -> mark as unverified.
                r["klasifikasi"] = "Belum terverifikasi (Non-Scopus/Prosiding?)"
        # Manual overrides win over the automatic result.
        if r.get("jurnal") in SCOPUS_OVERRIDE_VERIFIED:
            r["klasifikasi"] = SCOPUS_OVERRIDE_VERIFIED[r["jurnal"]]
        rows_all.append(r)
    json.dump(d, open(fp, "w"), ensure_ascii=False, indent=1)

# --- Classification distribution summary ---
c = collections.Counter(r["klasifikasi"] for r in rows_all)
print("klasifikasi selesai. Distribusi:")
for k, v in sorted(c.items(), key=lambda kv: -kv[1]):
    print(f"  {v:3d}  {k}")
