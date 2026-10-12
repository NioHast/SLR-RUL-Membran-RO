"""
issn.py - Map DOI to ISSN/venue via OpenAlex (stage 3: journal classification).

Purpose:
    For each DOI in the corpus, fetch source (journal) information from OpenAlex:
    ISSN-L, ISSN list, journal name, type, and DOAJ status. The result is used by
    classify_scopus.py to match journals to SCImago quartiles.

INPUT:
    - corpus_*.json (corpus files in the working directory; field "doi").
OUTPUT:
    - issn_map.json (DOI -> {issn_l, issn, source, type, in_doaj} map).
How to run:
        python3 issn.py
NOTE:
    The script reads/writes files in the current working directory (not absolute
    paths). Run it from the folder containing corpus_*.json, or adjust the path.
    Other scripts in the pipeline use absolute paths (e.g. BASE="/tmp/opencode/slr")
    which you MUST change to your own working location.
"""

import json, glob, urllib.request, urllib.parse, time

# --- Load all DOIs from the corpus files ---
rows=[]
for fp in sorted(glob.glob("corpus_*.json")): rows+=json.load(open(fp))
dois=[r["doi"] for r in rows if r.get("doi")]

def batch(ds):
    """Query OpenAlex for a set of DOIs (OR filter with '|' as separator)."""
    f="doi:"+"|".join(ds)
    u="https://api.openalex.org/works?filter="+urllib.parse.quote(f)+"&per_page=50&select=doi,primary_location,authorships,title"
    req=urllib.request.Request(u,headers={"User-Agent":"issn/1.0 (mailto:s@example.org)"})
    return json.load(urllib.request.urlopen(req,timeout=60))

# --- Query in chunks of 40 DOIs (so the URL is not too long) ---
out={}
for i in range(0,len(dois),40):
    try: d=batch(dois[i:i+40])
    except Exception as e: print("err",e); continue
    for w in d.get("results",[]):
        # The DOI from OpenAlex is a URL -> take the part after the prefix.
        doi=(w.get("doi") or "").replace("https://doi.org/","")
        src=((w.get("primary_location") or {}).get("source") or {})
        out[doi]={"issn_l":src.get("issn_l"),"issn":src.get("issn"),"source":src.get("display_name"),"type":src.get("type"),"in_doaj":src.get("is_in_doaj")}
    time.sleep(0.4)  # polite delay so as not to overload the API

# --- Save the mapping ---
json.dump(out,open("issn_map.json","w"),ensure_ascii=False,indent=1)
print("mapped",len(out),"of",len(dois))

# Summary of the number of unique venues.
uv={}
for v in out.values():
    if v.get("source"): uv[v["source"]]=v.get("issn_l")
print("unique venues:",len(uv))
