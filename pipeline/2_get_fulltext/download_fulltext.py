#!/usr/bin/env python3
"""
download_fulltext.py  (v2 - expanded resolver)
Download the OPEN ACCESS full-text PDF for the entire corpus AUTOMATICALLY.
Tries ALL OA locations: OpenAlex (best + locations) and Unpaywall (best + oa_locations).
Save to ../full_text/ . Those that are truly closed are logged in fulltext_report.json.
Run: python3 download_fulltext.py   (safe to repeat; existing files are skipped)

INPUT:
    - data/corpus_*.json (corpus metadata: no, doi, author, year, title).
OUTPUT:
    - ../full_text/00X_*.pdf            : OA PDFs successfully downloaded.
    - ../full_text/fulltext_report.json : status of each article (ok/skip/closed).
How to run:
        python3 download_fulltext.py
NOTE:
    Paths are computed relative to the location of this file (HERE/data ->
    ../full_text), so the folder structure must be kept as is. Other scripts in
    the pipeline use absolute paths (e.g. BASE="/tmp/opencode/slr") which you MUST
    change to your own working location.
"""

import json, os, glob, urllib.request, urllib.parse, re

# --- Paths & configuration ---
HERE=os.path.dirname(os.path.abspath(__file__)); DATA=os.path.join(HERE,"data")
OUT=os.path.join(os.path.dirname(HERE),"full_text"); os.makedirs(OUT,exist_ok=True)
EMAIL="mnioh@students.undip.ac.id"; UA={"User-Agent":"slr-fulltext/1.0 (mailto:%s)"%EMAIL}

# --- Load all corpus records ---
rows=[]
for fp in sorted(glob.glob(os.path.join(DATA,"corpus_*.json"))): rows+=json.load(open(fp))
rows.sort(key=lambda r:r.get("no",0))

def _get(url,timeout=90):
    """Download the URL with the configured User-Agent."""
    return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=timeout).read()

def oa_urls(doi):
    """Collect ALL candidate OA PDF URLs for one DOI (OpenAlex + Unpaywall)."""
    urls=[]
    if doi:
        # Source 1: OpenAlex - best_oa_location + all locations.
        try:
            w=json.loads(_get("https://api.openalex.org/works/doi:"+urllib.parse.quote(doi)+f"?mailto={EMAIL}",40))
            for loc in ([w.get("best_oa_location")]+(w.get("locations") or [])):
                if loc:
                    if loc.get("pdf_url"): urls.append(loc["pdf_url"])
                    elif loc.get("is_oa") and loc.get("landing_page_url"): urls.append(loc["landing_page_url"])
        except Exception: pass
        # Source 2: Unpaywall - best_oa_location + oa_locations.
        try:
            u=json.loads(_get(f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={EMAIL}",40))
            for loc in ([u.get("best_oa_location")]+(u.get("oa_locations") or [])):
                if loc and loc.get("url_for_pdf"): urls.append(loc["url_for_pdf"])
        except Exception: pass
    # Drop duplicates, keep the order of appearance.
    seen=set(); out=[]
    for x in urls:
        if x and x not in seen: seen.add(x); out.append(x)
    return out

# --- Download PDF per article ---
rep=[]; ok=0; closed=0
for r in rows:
    doi=(r.get("doi") or "").lower()
    # Filename: 00X_Firstauthor_Year.pdf
    name=f'{r.get("no"):03d}_'+re.sub(r'[^A-Za-z0-9]+','_',(r.get("penulis","") or "?").split(" ")[0])+f'_{r.get("tahun","")}.pdf'
    dest=os.path.join(OUT,name)
    # Already exists and has a reasonable size -> skip (idempotent script).
    if os.path.exists(dest) and os.path.getsize(dest)>1000:
        ok+=1; rep.append({"no":r["no"],"file":name,"status":"skip"}); continue
    saved=False; used=""
    for url in oa_urls(doi):
        try:
            b=_get(url,90)
            # Accept only when it is truly a PDF (magic bytes "%PDF").
            if b[:4]==b"%PDF":
                open(dest,"wb").write(b); saved=True; used=url; break
        except Exception:
            continue
    if saved:
        ok+=1; rep.append({"no":r["no"],"file":name,"status":"ok","url":used}); print(f'  [ok ] {r["no"]:3d} {name}')
    else:
        closed+=1; rep.append({"no":r["no"],"title":r.get("judul"),"doi":r.get("doi"),"status":"closed"}); print(f'  [xx ] {r["no"]:3d} closed | {r.get("judul","")[:55]}')

# --- Write the summary report ---
json.dump({"ok":ok,"closed":closed,"total":len(rows),"items":rep}, open(os.path.join(OUT,"fulltext_report.json"),"w"), ensure_ascii=False, indent=1)
print(f"\nSelesai: {ok} terunduh (OA), {closed} closed. Folder: {OUT}")
