"""
supp.py - Add supporting articles from additional queries (stage 1: supplement).

Purpose:
    Run 8 additional queries (focused on data limitations, prognostic few-shot,
    and the Indonesian context) to OpenAlex, then add their NEW results to
    pool.json without overwriting existing records.

INPUT:
    - pool.json (output of harvest.py; will be extended).

OUTPUT:
    - pool.json (rewritten: old articles + new supporting articles).

How to run:
        python3 supp.py

NOTE:
    The script reads/writes files in the current working directory (not absolute
    paths). Other scripts in this pipeline use absolute paths (e.g.
    BASE="/tmp/opencode/slr") which you MUST change to your own working location.
"""

import json, time, urllib.parse, urllib.request, re

# --- OpenAlex endpoint configuration ---
MAIL="mailto=student@example.org"
BASE="https://api.openalex.org/works"
SELECT="id,doi,title,publication_year,authorships,primary_location,cited_by_count,type,language,open_access,abstract_inverted_index,topics"

# --- Additional queries targeting gaps in the initial corpus ---
qs=["remaining useful life limited data","prognostics small sample deep learning",
    "predictive maintenance water treatment plant Indonesia","desalination Indonesia membrane",
    "survival analysis predictive maintenance Indonesia","machine learning maintenance Indonesia water",
    "remaining useful life data scarcity augmentation","few-shot prognostics industrial"]

def fetch(q,per=40):
    """Fetch one page of results for one query."""
    filt=f"title_and_abstract.search:{q},type:article,has_doi:true"
    url=f"{BASE}?filter={urllib.parse.quote(filt)}&per_page={per}&select={SELECT}&sort=relevance_score:desc&{MAIL}"
    req=urllib.request.Request(url,headers={"User-Agent":"slr/1.0"})
    return json.load(urllib.request.urlopen(req,timeout=60))

def rec(inv):
    """Reconstruct the abstract from the OpenAlex inverted index."""
    if not inv: return ""
    p={}
    for w,ix in inv.items():
        for i in ix: p[i]=w
    return " ".join(p[k] for k in sorted(p))

# Load the existing pool so old articles are not overwritten.
pool={w["id"]:w for w in json.load(open("pool.json"))}
before=len(pool)

# --- Add new query results that are not yet in the pool ---
for q in qs:
    try: d=fetch(q)
    except Exception as e: print("ERR",q,e); continue
    for w in d.get("results",[]):
        if w["id"] in pool: continue   # skip ones that already exist
        names=[a.get("author",{}).get("display_name","") for a in (w.get("authorships") or [])]
        pl=w.get("primary_location") or {}; src=pl.get("source") or {}
        pool[w["id"]]={"id":w["id"],"doi":w.get("doi"),"title":w.get("title"),"year":w.get("publication_year"),
            "authors":names,"venue":src.get("display_name"),"host":src.get("host_organization_name"),
            "cites":w.get("cited_by_count"),"type":w.get("type"),"oa":(w.get("open_access") or {}).get("is_oa"),
            "abstract":rec(w.get("abstract_inverted_index"))[:2500],"topics":[],"_queries":[q]}
    print(f"total {len(pool)} | {q}")
    time.sleep(0.6)  # polite delay so as not to overload the API

# --- Save the extended pool ---
json.dump(list(pool.values()),open("pool.json","w"),ensure_ascii=False)
print("pool grew",before,"->",len(pool))
