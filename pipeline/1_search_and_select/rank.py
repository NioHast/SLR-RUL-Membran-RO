"""
rank.py - Score the relevance of each article (stage 1: ranking).

Purpose:
    Score every article in pool.json based on the presence of keywords in the
    title+abstract (RUL pillars, censoring, deep learning, RO/membrane domain),
    plus a bonus when core keywords appear in the title, as well as a logarithmic
    weight from the citation count. This score order is what the next selection
    stage uses.

INPUT:
    - pool.json (output of harvest.py).

OUTPUT:
    - ranked.json (pool.json with a "_score" field added and sorted).

How to run:
        python3 rank.py

NOTE:
    The script reads/writes files in the current working directory (not absolute
    paths). Other scripts in this pipeline use absolute paths (e.g.
    BASE="/tmp/opencode/slr") which you MUST change to your own working location.
"""

import json, re, math

pool=json.load(open("pool.json"))

# --- Keyword dictionary per pillar (different weights per group) ---
RUL=["remaining useful life","rul","prognos","degradation","failure prediction","health index","predictive maintenance","condition-based","remaining life","residual life"]
CEN=["censor","survival analysis","weibull","hazard","time-to-event","failure time"]
DL=["deep learning","neural network","lstm","transformer","bayesian","machine learning","recurrent","convolutional"]
DOM=["reverse osmosis","membrane","desalination","fouling","scaling","water treatment","clean-in-place","cip ","permeate","brackish","seawater"]

def norm(s): return (s or "").lower()

# --- Compute the score of each article ---
scored=[]
for w in pool:
    t=norm(w["title"]); a=norm(w["abstract"]); txt=t+" "+a
    # Skip articles that are clearly not in English.
    lang=w.get("language")
    if lang not in (None,"en","english"): continue
    s=0
    # Weight per keyword occurrence in the combined title+abstract text.
    s+=3*sum(1 for k in RUL if k in txt)
    s+=3*sum(1 for k in CEN if k in txt)
    s+=2*sum(1 for k in DL if k in txt)
    s+=4*sum(1 for k in DOM if k in txt)
    # Extra bonus when core keywords appear in the title.
    if any(k in t for k in RUL): s+=4
    if any(k in t for k in DOM): s+=5
    if any(k in t for k in CEN): s+=3
    # Small weight from citations (log so it does not dominate the score).
    s+=min(math.log1p(w["cites"] or 0),5)
    w["_score"]=round(s,1)
    scored.append(w)

# --- Sort: highest score first, then most citations ---
scored.sort(key=lambda x:(-x["_score"], -(x["cites"] or 0)))
json.dump(scored, open("ranked.json","w"), ensure_ascii=False)
print("ranked:", len(scored))

# Display the top 130 articles as a summary in the terminal.
for i,w in enumerate(scored[:130],1):
    v=(w["venue"] or "")[:44]
    print(f'{i:3d} s{w["_score"]:5.1f} c{w["cites"]:>4} {w["year"]} | {v:44s} | {(w["title"] or "")[:78]}')
