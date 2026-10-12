"""
harvest.py - Harvest article metadata from OpenAlex (stage 1: search).

Purpose:
    Send 16 search queries to the OpenAlex API, then merge all results into a
    single pool of unique articles. Deduplication is based on the OpenAlex ID.
    Each record stores the title, DOI, year, authors, venue, citation count,
    open access status, abstract (reconstructed from "abstract_inverted_index"),
    topics, and the list of queries that found it.

INPUT:
    - Reads no input file (the query list is embedded directly in the script).
    - Network source: https://api.openalex.org/works

OUTPUT:
    - pool.json : all unique harvested articles.
    - pool.csv  : quick summary (title, year, venue, cites, doi, oa).

How to run:
    Run from this folder (output is written to the working directory):
        python3 harvest.py

NOTE:
    The script writes output files to the current working directory (not an
    absolute path), so make sure to run it from the correct folder or adjust the
    path. Other scripts in this pipeline use absolute paths (e.g.
    BASE="/tmp/opencode/slr") which you MUST change to your own working location.
"""

import json, time, urllib.parse, urllib.request, re, csv, sys

# --- OpenAlex endpoint configuration ---
MAIL="mailto=student@example.org"
BASE="https://api.openalex.org/works"
# Fields requested from the API (limits the response size).
SELECT="id,doi,title,publication_year,authorships,primary_location,cited_by_count,type,language,open_access,abstract_inverted_index,topics,referenced_works_count"

# --- Search query list (covers RUL pillars, censoring, DL, and the RO domain) ---
queries = [
 "remaining useful life survival analysis",
 "remaining useful life censored",
 "remaining useful life censored data deep learning",
 "predictive maintenance censored data",
 "remaining useful life LSTM prediction",
 "remaining useful life Bayesian neural network",
 "reverse osmosis membrane remaining useful life",
 "reverse osmosis membrane fouling prediction machine learning",
 "membrane fouling prediction machine learning",
 "desalination predictive maintenance machine learning",
 "remaining useful life few-shot learning",
 "remaining useful life transfer learning",
 "Weibull degradation remaining useful life",
 "membrane replacement prediction",
 "water treatment predictive maintenance",
 "prognostics health management deep learning censored",
]

def fetch(q, per=50):
    """Fetch one page of results for one query, sorted by relevance score."""
    # Filter: search in title+abstract, article type only, DOI required.
    filt = f"title_and_abstract.search:{q},type:article,has_doi:true"
    url = f"{BASE}?filter={urllib.parse.quote(filt)}&per_page={per}&select={SELECT}&sort=relevance_score:desc&{MAIL}"
    req = urllib.request.Request(url, headers={"User-Agent":"slr-harvest/1.0 (mailto:student@example.org)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def reconstruct(inv):
    """Reconstruct the abstract text from the OpenAlex inverted-index structure."""
    if not inv: return ""
    # Invert the word -> position map into position -> word, then assemble in order.
    pos={}
    for w,idxs in inv.items():
        for i in idxs: pos[i]=w
    return " ".join(pos[k] for k in sorted(pos))

# --- Harvest: iterate each query and add new results to the pool ---
pool={}
for q in queries:
    try:
        d=fetch(q)
    except Exception as e:
        print("ERR",q,e); continue
    got=0
    for w in d.get("results",[]):
        wid=w["id"]
        # Existing article: just record the additional query that found it.
        if wid in pool:
            pool[wid]["_queries"].append(q); continue
        auths=w.get("authorships",[]) or []
        names=[a.get("author",{}).get("display_name","") for a in auths]
        pl=w.get("primary_location") or {}
        src=(pl.get("source") or {})
        pool[wid]={
            "id":wid,"doi":w.get("doi"),"title":w.get("title"),
            "year":w.get("publication_year"),
            "authors":names,
            "venue":src.get("display_name"),
            "host":src.get("host_organization_name"),
            "cites":w.get("cited_by_count"),
            "type":w.get("type"),
            "oa":(w.get("open_access") or {}).get("is_oa"),
            "abstract":reconstruct(w.get("abstract_inverted_index"))[:2500],
            "topics":[t.get("display_name") for t in (w.get("topics") or [])][:3],
            "_queries":[q],
        }
        got+=1
    print(f"{got:3d} new  | total {len(pool):4d} | {q}")
    time.sleep(0.6)  # polite delay so as not to overload the API

# --- Save harvest results ---
json.dump(list(pool.values()), open("pool.json","w"), ensure_ascii=False)
print("TOTAL unique:", len(pool))

# Compact CSV for quick review
with open("pool.csv","w",newline="",encoding="utf-8") as f:
    wr=csv.writer(f); wr.writerow(["title","year","venue","cites","doi","oa"])
    for w in sorted(pool.values(), key=lambda x:-(x["cites"] or 0)):
        wr.writerow([w["title"],w["year"],w["venue"],w["cites"],w["doi"],w["oa"]])
print("saved pool.json / pool.csv")
