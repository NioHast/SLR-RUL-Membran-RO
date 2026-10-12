"""
make_kernel.py - Build the Kaggle *pilot* kernel (notebook + metadata).

Purpose:
    Generate, on the local machine, the two files Kaggle needs to push the pilot
    full-text extraction kernel: the notebook (`slr_pilot.ipynb`) and its
    `kernel-metadata.json`. The notebook itself installs `marker-pdf` + `pymupdf`
    on the Kaggle GPU, runs `marker_single` on each PDF, and crops figures with
    PyMuPDF. This script only *writes* those files; it does not upload them.

INPUT:
    - No input file is read; the notebook cells are embedded below as strings.

OUTPUT:
    - <K>/slr_pilot.ipynb          : the generated pilot notebook.
    - <K>/kernel-metadata.json     : the Kaggle kernel metadata (id, dataset, GPU on).

How to run:
        python3 make_kernel.py

NOTE:
    Paths are absolute: K="/tmp/opencode/kaggle_pilot/kernel" MUST be adjusted to
    your own working location. The other phase2/phase5 scripts use
    ROOT="/home/nioha/Downloads/SLR", which also MUST be adjusted.
"""

import json, os

# --- Output folder for the generated kernel files ---
K = "/tmp/opencode/kaggle_pilot/kernel"
os.makedirs(K, exist_ok=True)


def cell(src):
    """Wrap a raw source string into a Jupyter notebook `code` cell dict."""
    return {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [],
            "source": [l + "\n" for l in src.split("\n")]}


# --- Cell 1: environment check + install marker-pdf/pymupdf ---
c1 = '''import subprocess, sys
print(subprocess.run(["nvidia-smi"],capture_output=True,text=True).stdout[:500])
print("=== install marker-pdf + pymupdf ===")
r=subprocess.run("pip install -q marker-pdf pymupdf 2>&1 | tail -6", shell=True, capture_output=True, text=True)
print(r.stdout[-1500:]); print("rc",r.returncode)
import fitz
try:
    import marker
    print("marker OK")
except Exception as e:
    print("marker import err", e)'''

# --- Cell 2: run marker on every pilot PDF + crop figures, then zip the output ---
c2 = '''import os, glob, subprocess, shutil, zipfile, re, fitz
IN="/kaggle/input/slr-pilot-pdfs"
OUT="/kaggle/working/out"; os.makedirs(OUT, exist_ok=True)
pdfs=sorted(glob.glob(os.path.join(IN,"*.pdf")))
print("PDFs:", [os.path.basename(p) for p in pdfs])

cap_re=re.compile(r'^\\s*(Fig(ure)?\\.?|Table|Tabel|Gambar)\\s*\\.?\\s*(\\d+)', re.I)
def col_edges(page,W):
    cov=[0]*(int(W)+1)
    for b in page.get_text("blocks"):
        x0=int(max(0,b[0])); x1=int(min(W,b[2]))
        for x in range(x0,x1+1): cov[x]+=1
    lo,hi=int(0.30*W),int(0.70*W); seg=cov[lo:hi]
    if not seg: return [0,int(W)]
    best=lo+min(range(len(seg)), key=lambda i: seg[i]); mx=max(seg)
    return [0,best,int(W)] if (mx>0 and cov[best]<=0.5*mx) else [0,int(W)]
def crop_figs(pdf, outdir, dpi=300):
    os.makedirs(outdir, exist_ok=True); doc=fitz.open(pdf); n=0
    for pno,page in enumerate(doc,1):
        R=page.rect; W=R.width; edges=col_edges(page,W)
        grafs=[d["rect"] for d in page.get_drawings()]
        for im in page.get_images(full=True):
            try: grafs+=list(page.get_image_rects(im[0]))
            except: pass
        caps=[]
        for b in page.get_text("dict").get("blocks",[]):
            for l in b.get("lines",[]):
                t="".join(s["text"] for s in l.get("spans",[]))
                if cap_re.match(t): caps.append((fitz.Rect(l["bbox"]),t.strip()))
        for cap,t in caps:
            fw=cap.width>0.7*W
            if len(edges)==3 and not fw:
                c0,c1=(edges[0],edges[1]) if (cap.x0+cap.x1)/2<edges[1] else (edges[1],edges[2])
            else: c0,c1=0,W
            inc=lambda g: c0-2<=(g.x0+g.x1)/2<=c1+2
            tab=t.lower().startswith(("table","tabel"))
            cands=[g for g in grafs if ((g.y0>=cap.y1-2 and (g.y0-cap.y1)<0.6*R.height) if tab else (g.y1<=cap.y0+2 and (cap.y0-g.y1)<0.75*R.height)) and inc(g)]
            if not cands: continue
            x0=min(max(c0,min(g.x0 for g in cands)),cap.x0); y0=min(g.y0 for g in cands)
            x1=max(min(c1,max(g.x1 for g in cands)),cap.x1); y1=max(g.y1 for g in cands)
            clip=fitz.Rect(x0-3,y0-3,x1+3,y1+3)&R
            if clip.width<20 or clip.height<20: continue
            n+=1; page.get_pixmap(matrix=fitz.Matrix(dpi/72,dpi/72),clip=clip).save(os.path.join(outdir,f"fig-{n:02d}_p{pno}.png"))
    return n

for f in pdfs:
    base=os.path.splitext(os.path.basename(f))[0]
    d=os.path.join(OUT,base); os.makedirs(d, exist_ok=True)
    r=subprocess.run(["marker_single", f, "--output_dir", d], capture_output=True, text=True)
    print(base,"| marker rc",r.returncode)
    print((r.stdout or "")[-500:]); print((r.stderr or "")[-500:])
    nf=crop_figs(f, os.path.join(d,"figures_crop"))
    print(base,"| fig crops:",nf)
shutil.make_archive("/kaggle/working/slr_pilot_out","zip",OUT)
print("OUT:", os.listdir("/kaggle/working"))
print("TREE:")
for root,dirs,files in os.walk(OUT):
    print(root.replace(OUT,""), "|", files[:8])'''

# --- Assemble the notebook JSON (2 code cells) and write it ---
nb = {"cells": [cell(c1), cell(c2)],
      "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"}, "language_info": {"name": "python"}},
      "nbformat": 4, "nbformat_minor": 5}
json.dump(nb, open(os.path.join(K, "slr_pilot.ipynb"), "w"))

# --- Kaggle kernel metadata: pilot dataset, GPU + internet enabled ---
meta = {"id": "muhammadnioh/slr-pilot-marker", "title": "SLR Pilot Marker", "code_file": "slr_pilot.ipynb",
        "language": "python", "kernel_type": "notebook", "is_private": True,
        "enable_gpu": True, "enable_internet": True, "dataset_sources": ["muhammadnioh/slr-pilot-pdfs"],
        "competition_sources": [], "kernel_sources": []}
json.dump(meta, open(os.path.join(K, "kernel-metadata.json"), "w"), indent=1)

print("kernel folder:", os.listdir(K))
