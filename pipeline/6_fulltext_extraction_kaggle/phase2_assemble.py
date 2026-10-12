"""
phase2_assemble.py - Assemble per-paper folders from Kaggle output (stage 6).

Purpose:
    For every paper in the corpus, build a folder under `deliverables/per_paper/`
    containing: the source PDF, the Marker-generated `text.md`, the extracted
    figures, the Kaggle `meta.json`, and an `extraction.json` summary (dimension
    flags d1..d8, visual-evidence counts, inclusion status). Input comes from the
    unzipped Kaggle output (`_KAGGLE_FULL/unz`) plus the local `full_text` PDFs.

INPUT:
    - ROOT/source_code/data/corpus_a.json  : the corpus (paper list + metadata).
    - ROOT/full_text/*.pdf                 : original PDFs, matched by title.
    - ROOT/deliverables/per_paper/_KAGGLE_FULL/unz/<NNN>/**  : unzipped Kaggle
      output (Marker markdown, *_meta.json, *.jpeg figures).

OUTPUT:
    - ROOT/deliverables/per_paper/<slug>/paper.pdf
    - ROOT/deliverables/per_paper/<slug>/text.md
    - ROOT/deliverables/per_paper/<slug>/figures/*
    - ROOT/deliverables/per_paper/<slug>/meta.json
    - ROOT/deliverables/per_paper/<slug>/extraction.json

How to run:
        python3 phase2_assemble.py
    Run AFTER the Kaggle kernel output has been unzipped into `_KAGGLE_FULL/unz`.

NOTE:
    Paths are absolute: ROOT="/home/nioha/Downloads/SLR" MUST be adjusted to your
    own working location before running.
"""

import json, os, re, glob, shutil

# --- Absolute paths (CHANGE ME to match your own working location) ---
ROOT = "/home/nioha/Downloads/SLR"
UNZ = os.path.join(ROOT, "deliverables", "per_paper", "_KAGGLE_FULL", "unz")
FT = os.path.join(ROOT, "full_text")
PP = os.path.join(ROOT, "deliverables", "per_paper")

# --- Load the corpus (list of papers with judul/penulis/tahun/doi/etc.) ---
corpus = json.load(open(os.path.join(ROOT, "source_code", "data", "corpus_a.json")))


def san(t):
    """Sanitize a title so it can be used as a file name (strip illegal chars, cap length)."""
    t = re.sub(r'[\r\n\t]+', ' ', t or ""); t = re.sub(r'[\\/:*?"<>|]', '', t); t = re.sub(r'\s+', ' ', t).strip().strip('.')
    return t[:180].strip()


# --- Map every local full-text PDF by its basename for title lookup ---
ft = {os.path.basename(f): f for f in glob.glob(FT + "/*.pdf")}


def find_ft(title):
    """Find the local PDF whose filename best matches `title` (exact, else normalized key)."""
    fn = san(title) + ".pdf"
    if fn in ft: return ft[fn]
    key = re.sub(r'[^a-z0-9]', '', san(title).lower())[:60]
    for hb, hp in ft.items():
        if re.sub(r'[^a-z0-9]', '', hb.lower())[:60] == key: return hp
    return None


def find_md(no):
    """Find the Marker markdown file for paper number `no` (first match)."""
    hits = glob.glob(os.path.join(UNZ, "%03d" % no, "**", "*.md"), recursive=True)
    return hits[0] if hits else None


def find_figs(no):
    """List all extracted JPEG figures for paper number `no`."""
    return glob.glob(os.path.join(UNZ, "%03d" % no, "**", "*.jpeg"), recursive=True)


# --- Keyword rules: paper is marked "relevant" for a dimension if any keyword appears ---
DIMS = {"d1": ["sensor", "transducer", "measurement", "time series", "time-series", "signal", "spectral", "vibration", "temperature", "pressure", "flow", "ph "],
        "d2": ["failure", "remaining useful life", "rul", "degradation", "health index", "threshold", "end-of-life", "end of life"],
        "d3": ["censor", "censored", "survival analysis", "weibull", "hazard", "time-to-event", "time to event", "cox"],
        "d4": ["lstm", "transformer", "neural network", "deep learning", "machine learning", "random forest", "cnn", "convolutional", "bayesian", "gaussian process", "svm", "xgboost"],
        "d5": ["uncertaint", "confidence interval", "credible interval", "posterior", "probabilistic"],
        "d6": ["maintenance", "decision", "schedul", "clean-in-place", "cip", "replacement", "cost", "dss", "policy"],
        "d7": ["reverse osmosis", "membrane", "desalin", "brackish", "seawater", "fouling", "permeate"],
        "d8": ["small data", "few-shot", "few shot", "limited data", "transfer learning", "hierarchical", "small sample", "data scarcity", "poor data"]}


def dims(text):
    """Return {d1..d8: "1"|""} by keyword-matching the lower-cased full text."""
    t = text.lower(); out = {}
    for k, ks in DIMS.items(): out[k] = "1" if any(x in t for x in ks) else ""
    return out


# --- Legacy/unused mapping of manual overrides (disabled by `if False`) ---
rows = []; man = {m["no"]: m for m in json.load(open(os.path.join(ROOT, "source_code", "data", "..", "..", "tmp") + "")) } if False else {}

built = 0; nolog = []

# --- Build one folder per corpus paper ---
for r in corpus:
    no = r["no"]; md = find_md(no)
    slug = f'{no:03d}_' + re.sub(r'[^A-Za-z]+', '_', (r.get("penulis", "?") or "?").split(" ")[0]) + f'_{r.get("tahun","")}'
    d = os.path.join(PP, slug); os.makedirs(d, exist_ok=True)

    # pdf: copy the source full-text PDF if it could be matched
    src = find_ft(r.get("judul"))
    if src: shutil.copy2(src, os.path.join(d, "paper.pdf"))

    # text.md + figures: copy the Marker markdown and all extracted JPEGs
    txt = ""
    if md:
        shutil.copy2(md, os.path.join(d, "text.md")); txt = open(md, encoding="utf-8", errors="replace").read()
        fg = os.path.join(d, "figures"); os.makedirs(fg, exist_ok=True)
        for i, f in enumerate(sorted(find_figs(no)), 1):
            shutil.copy2(f, os.path.join(fg, os.path.basename(f)))
    else: nolog.append(no)

    # meta.json: copy the Kaggle *_meta.json if present
    mj = glob.glob(os.path.join(UNZ, "%03d" % no, "**", "*_meta.json"), recursive=True)
    if mj: shutil.copy2(mj[0], os.path.join(d, "meta.json"))

    # counts: number of equations, markdown table rows, and keyword dimension flags
    n_eq = len(re.findall(r'\$\$', txt))//2 + txt.count('\\begin{equation}')
    n_tab = len(re.findall(r'^\|.*\|$', txt, re.M))
    dm = dims(txt)

    # extraction.json: per-paper summary consumed by the later merge/finalize steps
    ext = {"no": no, "judul": r.get("judul"), "penulis": r.get("penulis"), "tahun": r.get("tahun"),
           "jurnal": r.get("jurnal"), "doi": r.get("doi"), "kuartil": r.get("klasifikasi"), "pilar": r.get("pilar"),
           "relevansi": None, "kualitas": None, "dimensi": dm,
           "bukti_visual": {"figures": len(find_figs(no)), "equations": n_eq, "table_rows": n_tab}, "status_inklusi": "diterima"}
    json.dump(ext, open(os.path.join(d, "extraction.json"), "w"), ensure_ascii=False, indent=1)
    built += 1

print("folder dibangun:", built, "| tanpa md:", nolog)
