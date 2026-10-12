#!/usr/bin/env python3
"""
build_xlsx.py - Build the SLR results spreadsheet (stage 4).

Purpose:
    Create SLR_Korpus.xlsx from data/corpus_*.json (+ synthesis.json) with 6
    sheets: Korpus, Ringkasan & Status, Matriks Konsep (Webster-Watson), Sintesis
    & Gap Final, Peta Teori ke Dimensi, and Konsep Kunci Model.
    Features: order Q1->Q2->Q3->SINTA1->SINTA2 then newest year; mark the anchor
    paper (Gao); check-matrix for dimensions D1-D8.

INPUT:
    - BASE/corpus_*.json      (corpus metadata).
    - BASE/harvest_stats.json (harvest statistics; optional).
    - BASE/synthesis.json     (synthesis + gap + theory + concepts).
OUTPUT:
    - /home/nioha/Downloads/SLR_Korpus.xlsx
How to run:
        python3 build_xlsx.py
NOTE:
    BASE="/tmp/opencode/slr" and OUT="/home/nioha/Downloads/SLR_Korpus.xlsx"
    are ABSOLUTE paths; you MUST change them to your own working location before running.
"""

# Build SLR_Korpus.xlsx from data/corpus_*.json (+ synthesis.json).
# Features: order Q1->Q2->Q3->SINTA1->SINTA2 then newest year; mark the anchor paper (Gao); check-matrix.
import json, os, glob
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

BASE="/tmp/opencode/slr"
OUT="/home/nioha/Downloads/SLR_Korpus.xlsx"

def load(fn):
    """Load the JSON at BASE/fn; return [] if the file does not exist."""
    p=os.path.join(BASE,fn)
    return json.load(open(p)) if os.path.exists(p) else []

# --- Load the entire corpus ---
rows=[]
for _fp in sorted(glob.glob(os.path.join(BASE,"corpus_*.json"))):
    rows += json.load(open(_fp))

# order: quartile tier -> newest year -> pillar -> title
def _tier(r):
    k=str(r.get("klasifikasi",""))
    if k.startswith("Scopus Q1"): return 1
    if k.startswith("Scopus Q2"): return 2
    if k.startswith("Scopus Q3"): return 3
    return 4
rows.sort(key=lambda r:(_tier(r), -(r.get("tahun") or 0), r.get("pilar",""), (r.get("judul") or "").lower()))
for _i,_r in enumerate(rows,1): _r["no"]=_i

def _is_gao(r):
    """True if this article is the main anchor paper (Gao) - will be highlighted purple."""
    return "A Neural Network-Based Survival Analysis Model" in (r.get("judul") or "")

# prevent text from being treated as a formula (do not start with "=")
def _s(v): return (" "+v) if isinstance(v,str) and v.startswith("=") else v

stats=load("harvest_stats.json"); syn=load("synthesis.json")

# --- Basic styling ---
wb=Workbook()
hdr_font=Font(bold=True,color="FFFFFF")
hdr_fill=PatternFill("solid",fgColor="1F4E78")
wrap=Alignment(wrap_text=True,vertical="top")
thin=Side(style="thin",color="BFBFBF")
border=Border(left=thin,right=thin,top=thin,bottom=thin)
PURPLE_ROW=PatternFill("solid",fgColor="C9A0DC")   # anchor paper (Gao)
PURPLE_CHK=PatternFill("solid",fgColor="E6DAF5")   # checked cell
PURPLE_TXT="5B2C87"

def style_header(ws,ncol):
    """Apply header styling (row 1) to all columns."""
    for c in range(1,ncol+1):
        cell=ws.cell(row=1,column=c); cell.font=hdr_font; cell.fill=hdr_fill
        cell.alignment=Alignment(wrap_text=True,vertical="center",horizontal="center")
def autosize(ws,widths):
    """Set each column's width according to the `widths` list."""
    for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w

# ---- Sheet 1: Korpus ----
ws=wb.active; ws.title="SLR - Korpus Jurnal"
cols=["No","Pilar/Tema","Judul Artikel","Penulis","Tahun","Nama Jurnal","Klasifikasi","Link/DOI","Ringkasan Temuan","Kontribusi terhadap Research Gap"]
ws.append(cols)
for r in rows:
    doi=r.get("doi") or ""
    link=("https://doi.org/"+doi) if doi else ""
    ws.append([_s(r.get("no")),_s(r.get("pilar")),_s(r.get("judul")),_s(r.get("penulis")),r.get("tahun"),_s(r.get("jurnal")),_s(r.get("klasifikasi")),link,_s(r.get("ringkasan")),_s(r.get("kontribusi"))])
    if _is_gao(r):
        for c in ws[ws.max_row]: c.fill=PURPLE_ROW
style_header(ws,len(cols)); autosize(ws,[5,30,52,22,7,30,26,34,60,55])
for row in ws.iter_rows(min_row=2):
    for c in row: c.alignment=wrap; c.border=border
ws.freeze_panes="A2"
# Legend below the corpus table.
_lr=ws.max_row+2
ws.cell(row=_lr,column=1,value="LEGENDA").font=Font(bold=True)
_lc=ws.cell(row=_lr+1,column=1,value="Ungu"); _lc.fill=PURPLE_ROW
ws.cell(row=_lr+1,column=2,value="paper acuan utama (Gao et al., 2025, IEEE TASE)")
ws.cell(row=_lr+2,column=1,value="Urutan: Q1 > Q2 > Q3; dalam tier sama, tahun terbaru lebih dulu.")
ws.cell(row=_lr+3,column=1,value="Klasifikasi kuartil: SCImago 'SJR Best Quartile' (turunan Scopus).")

# ---- Sheet 2: Ringkasan & Status ----
ws2=wb.create_sheet("Ringkasan & Status")
ws2.append(["Status Kompilasi SLR - RUL Membran RO (Censored/Small-Data)"])
ws2["A1"].font=Font(bold=True,size=12)
from collections import Counter as _C
_qc=_C()
for _r in rows:
    _k=str(_r.get("klasifikasi",""))
    if _k.startswith("Scopus Q"): _qc[_k.split(" (")[0]]+=1
_qtxt=", ".join(f"{kk.replace('Scopus ','')}={vv}" for kk,vv in sorted(_qc.items()))
items=[
 ("Target korpus","50+ jurnal internasional (Scopus) + rujukan pendukung nasional"),
 ("Terkumpul (korpus inti)",f"{len(rows)} artikel (semua memiliki abstrak)"),
 ("Sumber metadata","OpenAlex (agregator Crossref/DOAJ); pencarian title+abstract; type=article; has_doi=true"),
 ("Catatan identifikasi",f"{stats.get('records_identified_unique','?')} record unik setelah dedup; disaring judul/abstrak"),
 ("Verifikasi Scopus",f"{sum(1 for r in rows if str(r.get('klasifikasi','')).startswith('Scopus'))}/{len(rows)} jurnal terindeks Scopus (sumber: SCImago 'SJR Best Quartile' + SJR 2024; turunan Scopus)"),
 ("Kuartil (Q1-Q4)",f"{_qtxt} (tanpa Q4)"),
 ("Kekurangan","Kuartil dari SCImago 'SJR Best Quartile' (turunan Scopus), BUKAN file literal 'Scopus Source List'; edisi 2022 + SJR 2024. Ringkasan artikel disusun dari abstrak, bukan full-text."),
]
for k,v in items: ws2.append([_s(k),_s(v)])
ws2.append([])
ws2.append(["Sebaran Pilar"]); ws2.cell(row=ws2.max_row,column=1).font=Font(bold=True)
pc=_C(r.get("pilar","") for r in rows)
for p,n in sorted(pc.items()): ws2.append([_s(p),n])
autosize(ws2,[34,70])

# ---- Sheet 3: Matriks Konsep ----
ws3=wb.create_sheet("Matriks Konsep (Webster-Watson)")
dims=["D1 Data/Sensor","D2 Target/Failure","D3 Censoring","D4 Arsitektur Model","D5 Ketidakpastian","D6 Keputusan/DSS","D7 Domain RO/Membran","D8 Skala Data"]
h=["No","Penulis (Tahun)"]+dims
ws3.append(h)
for r in rows:
    ws3.append([r.get("no"),_s(f'{r.get("penulis","")} ({r.get("tahun","")})')]+["✓" if r.get(f"d{i}") else "" for i in range(1,9)])
    _rw=ws3.max_row
    # Color the check cells: the Gao row uses dark purple, others light purple.
    _chkfill = PURPLE_ROW if _is_gao(r) else PURPLE_CHK
    for i in range(1,9):
        if r.get(f"d{i}"):
            cell=ws3.cell(row=_rw,column=2+i); cell.fill=_chkfill; cell.font=Font(color=PURPLE_TXT)
style_header(ws3,len(h)); autosize(ws3,[5,26]+[15]*8)
for row in ws3.iter_rows(min_row=2):
    for c in row: c.alignment=Alignment(horizontal="center",vertical="top"); c.border=border
ws3.freeze_panes="C2"
# Matrix legend.
_lr=ws3.max_row+2
ws3.cell(row=_lr,column=1,value="LEGENDA").font=Font(bold=True)
_c1=ws3.cell(row=_lr+1,column=1,value="✓"); _c1.fill=PURPLE_CHK; _c1.font=Font(color=PURPLE_TXT)
ws3.cell(row=_lr+1,column=2,value="dimensi tercakup")
_c2=ws3.cell(row=_lr+2,column=1,value="✓"); _c2.fill=PURPLE_ROW; _c2.font=Font(color=PURPLE_TXT)
ws3.cell(row=_lr+2,column=2,value="paper acuan utama (Gao et al., 2025) — hanya sel yang dicentang")
ws3.cell(row=_lr+3,column=1,value="Kolom D1–D8 = dimensi konsep (lihat sheet 'Sintesis & Gap Final').")

# ---- Sheet 4: Sintesis & Gap ----
ws4=wb.create_sheet("Sintesis & Gap Final")
ws4.append(["Sintesis Ekstraksi & Perumusan Research Gap"]); ws4["A1"].font=Font(bold=True,size=12)
dl={"d1":"D1 Data/Sensor","d2":"D2 Target/Failure","d3":"D3 Censoring","d4":"D4 Arsitektur Model","d5":"D5 Ketidakpastian","d6":"D6 Keputusan/DSS","d7":"D7 Domain RO/Membran","d8":"D8 Skala Data"}
ws4.append(["Dimensi","Jumlah Rujukan",f"/ {len(rows)}","Sintesis Naratif"] if rows else ["Dimensi","Jumlah","","Sintesis"])
cnt={k:sum(1 for r in rows if r.get(k)) for k in dl}
for k,label in dl.items(): ws4.append([label,cnt[k],f"/ {len(rows)}",_s(syn.get(k,""))])
ws4.append([]); ws4.append(["RESEARCH GAP FINAL"]); ws4.cell(row=ws4.max_row,column=1).font=Font(bold=True)
ws4.append([_s(syn.get("gap",""))])
autosize(ws4,[34,14,10,95])

# ---- Sheet 5: Peta Teori ----
ws5=wb.create_sheet("Peta Teori ke Dimensi")
ws5.append(["Teori Sumber","Dimensi","Rujukan Pendukung Utama","Apa yang Diukur"])
for row in syn.get("teori",[]): ws5.append([_s(x) for x in row])
style_header(ws5,4); autosize(ws5,[30,26,40,55])

# ---- Sheet 6: Konsep Kunci ----
ws6=wb.create_sheet("Konsep Kunci Model")
ws6.append(["Konsep","Definisi","Posisi pada Model Penelitian Ini"])
for row in syn.get("konsep",[]): ws6.append([_s(x) for x in row])
style_header(ws6,3); autosize(ws6,[28,60,60])

wb.save(OUT)

# validation: there must be no cell of type formula
nf=0
for sh in wb.worksheets:
    for row in sh.iter_rows():
        for c in row:
            if c.data_type=="f": nf+=1
print("WROTE",OUT,"| rows:",len(rows),"| sel-formula (harus 0):",nf)
