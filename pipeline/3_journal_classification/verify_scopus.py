"""
verify_scopus.py - Independent verification of Scopus coverage & quartiles (stage 3).

Purpose:
    Independently recompute how many corpus journals are actually indexed in
    Scopus (via sjr_all.csv) along with their quartiles, as a cross-check against
    classify_scopus.py. The result is used to verify the claim
    "N/N Scopus journals" in the report.

INPUT:
    - issn_map.json (output of issn.py).
    - sjr_all.csv   (SCImago mirror; must be present in the working directory).
OUTPUT:
    - scopus_check.json (per DOI: {scopus, title, sjr, year, q}).
How to run:
        python3 verify_scopus.py
NOTE:
    The script reads/writes files in the current working directory. Copy sjr_all.csv
    from ../mirror_data/ into this folder first (or adjust the path). Other scripts
    in the pipeline use absolute paths (e.g. BASE="/tmp/opencode/slr") which you
    MUST change to your own working location.
"""

import json, csv, collections

iss=json.load(open("issn_map.json"))

def norm(i): return (i or "").replace("-","").replace(" ","").upper().strip()
def toks(cell): return [norm(t) for t in str(cell or "").split(",") if norm(t)]

# --- Build the ISSN -> SJR rows index ---
rows=list(csv.DictReader(open("sjr_all.csv",encoding="utf-8",errors="replace")))
idx=collections.defaultdict(list)
for r in rows:
    for t in toks(r.get("Issn")): idx[t].append(r)

# --- SJR 2024 quartile per field ---
byf=collections.defaultdict(list)
for r in rows:
    if r.get("year")!="2024": continue
    try: s=float(r["SJR"])
    except: continue
    for t in toks(r.get("Issn")): byf[r.get("field")].append((s,t))
quart={}
for f,lst in byf.items():
    lst.sort(reverse=True); n=len(lst)
    for rank,(s,t) in enumerate(lst):
        quart[(f,t)]=min(4,int(rank/(max(n,1)/4.0))+1)

# --- Check each DOI: is its ISSN present in the Scopus index? ---
res={}
for doi,v in iss.items():
    cands=[x for x in ([v.get("issn_l")]+(v.get("issn") or [])) if x]
    hit=None
    for c in cands:
        if norm(c) in idx: hit=norm(c); break
    if hit:
        rr=sorted(idx[hit], key=lambda x:(x.get("year") or ""))
        last=rr[-1]   # newest SJR row for this ISSN
        q=next((quart.get((r.get("field"),hit)) for r in rr if r.get("year")=="2024"), None)
        res[doi]={"scopus":True,"title":last.get("Title"),"sjr":last.get("SJR"),"year":last.get("year"),"q":q}
    else:
        res[doi]={"scopus":False}
json.dump(res,open("scopus_check.json","w"),ensure_ascii=False,indent=1)

# --- Summary of the verification results ---
n=len(res); ok=sum(1 for x in res.values() if x["scopus"])
qs=collections.Counter(x.get("q") for x in res.values() if x["scopus"])
print(f"matched {ok}/{n}  ({ok/n*100:.0f}%)")
print("quartile:",dict(sorted(qs.items(), key=lambda kv:(kv[0] is None, kv[0]))))
miss=sorted(set(iss[d]["source"] for d in res if not res[d]["scopus"]))
print("unmatched venues (%d):"%len(miss)); [print("  -",m) for m in miss]
