#!/usr/bin/env python3
"""
download_closed_playwright.py
Iterate over every DOI in DAFTAR_CLOSED, open it via Playwright, find the PDF
link/button, download it only if it is truly a PDF and public; SKIP if it needs
login / has no PDF. Save to ../full_text/ . Results are logged in
closed_playwright_report.json .
Run: python3 download_closed_playwright.py

INPUT:
    - data/corpus_*.json                (metadata: no, doi, author, year, title).
    - ../full_text/fulltext_report.json (list of articles with "closed" status).
OUTPUT:
    - ../full_text/00X_*.pdf                      : PDFs successfully downloaded.
    - ../full_text/closed_playwright_report.json  : status of each attempt.
How to run:
        python3 download_closed_playwright.py   (requires Playwright + Chrome)
NOTE:
    Paths are computed relative to the location of this file (HERE/data ->
    ../full_text), so the folder structure must be kept as is. Other scripts in
    the pipeline use absolute paths (e.g. BASE="/tmp/opencode/slr") which you MUST
    change to your own working location.
"""

import json, os, glob, re
from playwright.sync_api import sync_playwright

# --- Paths ---
HERE=os.path.dirname(os.path.abspath(__file__))
DATA=os.path.join(HERE,"data"); OUT=os.path.join(os.path.dirname(HERE),"full_text")
os.makedirs(OUT, exist_ok=True)

# --- Load corpus & closed-article list from the previous stage's report ---
rows=[]
for fp in sorted(glob.glob(os.path.join(DATA,"corpus_*.json"))): rows+=json.load(open(fp))
byno={r["no"]:r for r in rows}
rep=json.load(open(os.path.join(OUT,"fulltext_report.json")))
closed=[x for x in rep["items"] if x.get("status")=="closed"]

def name_for(no):
    """Build the PDF filename following the convention of download_fulltext.py."""
    r=byno.get(no,{})
    a=re.sub(r'[^A-Za-z0-9]+','_',(r.get("penulis","") or "?").split(" ")[0])
    return f'{no:03d}_{a}_{r.get("tahun","")}.pdf'

# Real browser UA so it is not easily blocked.
UA=("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36")
res=[]
with sync_playwright() as p:
    # Launch headless Chrome with flags for stability on a server/container.
    b=p.chromium.launch(channel="chrome", args=["--no-sandbox","--disable-dev-shm-usage","--disable-blink-features=AutomationControlled"])
    ctx=b.new_context(accept_downloads=True, user_agent=UA)
    page=ctx.new_page()
    for x in closed:
        no=x["no"]; doi=x.get("doi"); dest=os.path.join(OUT,name_for(no))
        # Already exists and has a reasonable size -> skip.
        if os.path.exists(dest) and os.path.getsize(dest)>1000:
            res.append({"no":no,"status":"skip"}); continue
        status="closed"; used=""
        try:
            # Open the DOI page.
            page.goto("https://doi.org/"+doi, wait_until="domcontentloaded", timeout=35000)
            page.wait_for_timeout(2500)
            urls=[]
            # 1) Check the citation_pdf_url meta tag (the most reliable way).
            try:
                meta=page.evaluate("()=>{const m=document.querySelector('meta[name=\\\"citation_pdf_url\\\"]');return m?m.content:null;}")
                if meta: urls.append(meta)
            except Exception: pass
            # 2) Scan all links/buttons that look like a PDF link.
            try:
                cand=page.evaluate("""()=>{
                    const out=[];
                    document.querySelectorAll('a,button').forEach(e=>{
                        const h=e.href||''; const t=(e.textContent||'').toLowerCase();
                        if(/pdf/i.test(h)||/\\.pdf/i.test(h)||/download.*pdf|pdf.*download|\\bpdf\\b|full[- ]?text/i.test(t)) out.push(h);
                    });
                    return out;}""")
                urls+=cand
            except Exception: pass
            # Clean up: unique + only valid http URLs.
            urls=[u for u in dict.fromkeys([u for u in urls if isinstance(u,str) and u.startswith("http")])]
            # Try at most 8 URLs; accept only when the response is a valid PDF.
            for u in urls[:8]:
                try:
                    r=ctx.request.get(u, timeout=45000)
                    ct=(r.headers.get("content-type","") or "").lower()
                    if r.ok and ("pdf" in ct or ".pdf" in u.lower()):
                        body=r.body()
                        if body[:4]==b"%PDF":
                            open(dest,"wb").write(body); status="ok"; used=u; break
                except Exception: pass
        except Exception as e:
            status="error:"+type(e).__name__
        res.append({"no":no,"status":status,"url":used})
        print(f'  [{status:12s}] {no:3d} {x.get("title","")[:55]}')
    ctx.close(); b.close()

# --- Write the summary report ---
ok=sum(1 for r in res if r["status"] in ("ok","skip"))
json.dump({"checked":len(res),"ok":ok,"items":res}, open(os.path.join(OUT,"closed_playwright_report.json"),"w"), ensure_ascii=False, indent=1)
print(f"\nSelesai: {ok}/{len(res)} berhasil (OA baru terunduh). Folder: {OUT}")
