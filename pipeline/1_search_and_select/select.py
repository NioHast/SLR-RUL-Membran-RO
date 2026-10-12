"""
select.py - Select the core corpus from the ranked articles (stage 1: selection).

Purpose:
    From ranked.json, drop articles with medical/clinical topics (BLOCK) and
    articles without a sufficiently long abstract, then tag each article with
    concept pillars A-G. The core corpus is formed by prioritizing 4 anchor
    reference articles first, then filling the rest following the score order up
    to a quota of 72 articles.

INPUT:
    - ranked.json (output of rank.py).

OUTPUT:
    - selected.json (core corpus; each article is given a "pillars" field).

How to run:
        python3 select.py

NOTE:
    The script reads/writes files in the current working directory (not absolute
    paths). Other scripts in this pipeline use absolute paths (e.g.
    BASE="/tmp/opencode/slr") which you MUST change to your own working location.
"""

import json, re

scored=json.load(open("ranked.json"))

# Medical/clinical topic keywords that are dropped (outside the scope of this SLR).
BLOCK=["kidney","renal","glomerular","nephrolog","hepat","cancer","tumor","patient","clinical","dialysis","alzheimer","blood","antibody","drug","protein fouling"]

def has(t,ks): return any(k in t for k in ks)
def norm(s): return (s or "").lower()

# --- Tag each article's concept pillars (A=censoring ... G=Indonesian context) ---
pilots=[]
for w in scored:
    t=norm(w["title"]); a=norm(w["abstract"]); txt=t+" "+a
    if len(a)<120: continue       # requires a sufficiently informative abstract
    if has(t,BLOCK): continue     # drop medical topics
    pillars=[]
    if has(txt,["censor","survival analysis","weibull","hazard","cox","time-to-event"]): pillars.append("A")
    if has(txt,["lstm","cnn","transformer","deep learning","neural network","recurrent","autoencoder","resnet","attention"]): pillars.append("B")
    if has(txt,["bayesian","uncertainty","conformal","probabilistic"]): pillars.append("C")
    if has(txt,["few-shot","few shot","transfer learning","meta-learning","meta learning","small data","few sample","domain adaptation","data augmentation","hierarchical"]): pillars.append("D")
    if has(txt,["reverse osmosis","desalination","membrane","fouling","mbr","ultrafiltration","permeate","brackish","seawater","water treatment"]): pillars.append("E")
    if has(txt,["decision support","maintenance schedul","predictive maintenance","condition-based","dss","cmmst","cost","decision making","cmms"]): pillars.append("F")
    if has(txt,["indonesia","water plant","drinking water","rural","community"]): pillars.append("G")
    if not pillars: pillars=["B"]  # fallback: pillar B at minimum
    w["pillars"]=pillars
    pilots.append(w)

# select: take top by score but balance pillars; cap
# --- Selection: prioritize anchor articles, then fill up to the quota ---
sel=[]
seen=set()
# Ensure the 4 anchor articles are included first (matched by title).
anchors=["AI-based remaining useful life prediction of seawater desalination",
         "A Neural Network-Based Survival Analysis Model Considering Censored",
         "LSTM and Transformers based methods for Remaining Useful Life",
         "Survival Models for Predictive Maintenance and Remaining Useful Life"]
for w in pilots:
    for an in anchors:
        if an.lower() in (w["title"] or "").lower() and w["id"] not in seen:
            sel.append(w); seen.add(w["id"])
# then fill by score, requiring a pillar diversity
# The rest is filled following the score order up to the quota of 72 articles.
for w in pilots:
    if len(sel)>=72: break
    if w["id"] in seen: continue
    sel.append(w); seen.add(w["id"])
json.dump(sel, open("selected.json","w"), ensure_ascii=False)

# --- Summary of pillar coverage & top articles ---
from collections import Counter
c=Counter()
for w in sel:
    for p in w["pillars"]: c[p]+=1
print("selected:",len(sel))
print("pillar coverage:",dict(sorted(c.items())))
print("with abstract:",sum(1 for w in sel if len(w['abstract'])>150))
for i,w in enumerate(sel[:12],1):
    print(i,w["year"],(w["venue"] or "")[:40],"|",(w["title"] or "")[:70])
