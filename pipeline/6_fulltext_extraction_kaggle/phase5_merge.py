import json, glob, os, re
ROOT="/home/nioha/Downloads/SLR"; PP=os.path.join(ROOT,"deliverables","per_paper")
corpus=json.load(open(os.path.join(ROOT,"source_code","data","corpus_a.json")))
ext={}
for d in sorted(glob.glob(PP+"/*/")):
    n=os.path.basename(d.rstrip("/"))
    if n in ("_KAGGLE_FULL","_PILOT"): continue
    m=re.match(r'^(\d{3})_', n)
    if not m: continue
    try: ext[int(m.group(1))]=json.load(open(os.path.join(d,"extraction.json"),encoding="utf-8"))
    except Exception: pass
kept=[]; gugur=[]
for r in corpus:
    e=ext.get(r["no"])
    if e:
        inc=str(e.get("status_inklusi",""))
        if inc.startswith("gugur"):
            gugur.append({"no":r["no"],"judul":r.get("judul"),"doi":r.get("doi"),"alasan":inc}); continue
        r["ringkasan"]=e.get("ringkasan") or r.get("ringkasan")
        r["kontribusi"]=e.get("kontribusi") or r.get("kontribusi")
        r["relevansi"]=e.get("relevansi")
        r["kualitas_skor"]=e.get("kualitas",{}).get("skor")
        for k in ["d1","d2","d3","d4","d5","d6","d7","d8"]:
            r[k]="1" if e.get("dimensi",{}).get(k) else ""
    kept.append(r)
for i,r in enumerate(kept,1): r["no"]=i
json.dump(kept, open(os.path.join(ROOT,"source_code","data","corpus_a.json"),"w"), ensure_ascii=False, indent=1)
json.dump(gugur, open(os.path.join(ROOT,"source_code","data","phase5_gugur.json"),"w"), ensure_ascii=False, indent=1)
# distribution
from collections import Counter
print("korpus:",len(kept),"| gugur:",len(gugur))
for g in gugur: print("  GUGUR",g["no"],g["judul"][:50])
print("tier:",dict(Counter(r.get("relevansi") for r in kept)))
dims={f"d{i}":sum(1 for r in kept if r.get(f"d{i}")) for i in range(1,9)}
print("dims:",dims)
print("pilar:",dict(Counter(r.get("pilar") for r in kept)))
