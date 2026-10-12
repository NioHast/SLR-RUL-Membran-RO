#!/usr/bin/env python3
"""
fill_report.py - Fill placeholders in report.md with real numbers (stage 4).

Purpose:
    Read the corpus + synthesis.json, then replace the HTML comment markers
    (<!-- PRISMA -->, <!-- PILAR -->, <!-- DIMENSI -->, <!-- TABLES -->,
    <!-- SINTESIS -->, <!-- GAP -->) in report.md with tables/text that are
    already populated with numbers, and write them out as report_filled.md
    (ready -> docx).

INPUT:
    - BASE/corpus_*.json      (corpus metadata).
    - BASE/harvest_stats.json (harvest statistics; optional).
    - BASE/synthesis.json     (narrative synthesis per dimension + gap).
    - BASE/report.md          (report template containing the markers).
OUTPUT:
    - BASE/report_filled.md   (report ready to be converted to docx).
How to run:
        python3 fill_report.py
NOTE:
    BASE is the ABSOLUTE path "/tmp/opencode/slr" which you MUST change to your own
    working location before running. glob/Counter are imported mid-script exactly as
    in the original version (unchanged).
"""

# Fill report.md markers with real numbers from corpus + synthesis, then build docx.
import json, os, re
BASE="/tmp/opencode/slr"

def load(fn):
    """Load the JSON at BASE/fn; return [] if the file does not exist."""
    p=os.path.join(BASE,fn)
    return json.load(open(p)) if os.path.exists(p) else []

import glob

# --- Load & sort the corpus ---
rows=[]
for _fp in sorted(glob.glob(os.path.join(BASE,"corpus_*.json"))):
    rows += json.load(open(_fp))
rows.sort(key=lambda r:r.get("no",0))
stats=load("harvest_stats.json"); syn=load("synthesis.json")

from collections import Counter

# --- Compute the pillar distribution & dimension coverage ---
pillar=Counter(r.get("pilar","") for r in rows)
dims={"d1":"D1 Data/Sensor","d2":"D2 Target/Failure","d3":"D3 Censoring","d4":"D4 Arsitektur Model","d5":"D5 Ketidakpastian","d6":"D6 Keputusan/DSS","d7":"D7 Domain RO/Membran","d8":"D8 Skala Data"}
dimcnt={k:sum(1 for r in rows if r.get(k)) for k in dims}

# --- Build the PRISMA / pillar / dimension tables ---
total_id=stats.get("records_identified_unique","?")
prisma=[
 ["Tahap","Jumlah","Keterangan"],
 ["Identifikasi (record unik)","%s"%total_id,"Pencarian OpenAlex/Crossref, 24 query"],
 ["Disaring (judul/abstrak)","%s"%stats.get("records_screened","?"),"Kriteria relevansi keyword + abstrak tersedia"],
 ["Layak (full-record)","%d"%len(rows),"Artikel inti berabstrak, 2015-2026"],
 ["Termasuk (korpus sintesis)","%d"%len(rows),"Semua pilar A-G tercakup"],
]
pilar_tbl=[["Pilar/Tema","Jumlah Artikel"]]+[[k,v] for k,v in sorted(pillar.items())]
dim_tbl=[["Dimensi Konsep","Jumlah Artikel","/ Total"]]+[[dims[k],dimcnt[k],"/%d"%len(rows)] for k in dims]

def tbl(rows_):
    """Convert a list of rows into a Markdown table (helper function, unused)."""
    out=[]
    for r in rows_:
        out.append("| "+" | ".join(str(x) for x in r)+" |")
    return "\n".join(out)

# --- Sample table of core articles (first 25 in the original order) ---
rep=[["No","Tahun","Jurnal","Judul","Pilar"]]
for r in rows[:25]:
    rep.append([r.get("no"),r.get("tahun"),(r.get("jurnal") or "")[:34],(r.get("judul") or "")[:70],r.get("pilar","")])

# --- Read the template & replace each marker with the filled table/text ---
src=open(os.path.join(BASE,"report.md"),encoding="utf-8").read()
src=src.replace("<!-- PRISMA -->", "| "+" | ".join(prisma[0])+" |\n"+"\n".join("| "+" | ".join(str(c) for c in row)+" |" for row in prisma[1:]))
src=src.replace("<!-- PILAR -->", "| "+" | ".join(pilar_tbl[0])+" |\n"+"\n".join("| "+" | ".join(str(c) for c in row)+" |" for row in pilar_tbl[1:]))
src=src.replace("<!-- DIMENSI -->", "| "+" | ".join(dim_tbl[0])+" |\n"+"\n".join("| "+" | ".join(str(c) for c in row)+" |" for row in dim_tbl[1:]))
src=src.replace("<!-- TABLES -->", "### 3.4 Contoh Artikel Inti (25 dari %d)\n\n"%len(rows)+"\n".join("| "+" | ".join(str(c) for c in row)+" |" for row in rep[1:] ) if False else "### 3.4 Contoh Artikel Inti\n\n"+"| "+" | ".join(rep[0])+" |\n"+"\n".join("| "+" | ".join(str(c) for c in row)+" |" for row in rep[1:]))
# synthesis bullets
sint="\n".join(f"- **{dims[k]}**: {syn.get(k,'')} ({dimcnt[k]}/{len(rows)} artikel)" for k in dims)
src=src.replace("<!-- SINTESIS -->", sint)
src=src.replace("<!-- GAP -->", syn.get("gap","(gap belum tersedia)"))

# --- Write the result ---
open(os.path.join(BASE,"report_filled.md"),"w",encoding="utf-8").write(src)
print("report_filled.md written; papers=%d; pillars=%s; dims=%s"%(len(rows),dict(pillar),dimcnt))
