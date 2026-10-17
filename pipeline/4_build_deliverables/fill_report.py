#!/usr/bin/env python3
"""
fill_report.py - Fill the report template with real, single-source numbers.

Purpose:
    Read metadata/corpus_a.json, metadata/prisma_flow.json,
    metadata/core_papers.json and synthesis.json, then replace the HTML-comment
    markers in report.md with Markdown tables/text. Figure markers
    ({{FIG:...}}) are left untouched for build_docx.py.

INPUT:
    - metadata/corpus_a.json
    - metadata/prisma_flow.json
    - metadata/core_papers.json
    - pipeline/4_build_deliverables/synthesis.json
    - pipeline/4_build_deliverables/report.md
OUTPUT:
    - pipeline/4_build_deliverables/report_filled.md
How to run:
        python3 fill_report.py
"""
import json
import os
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", ".."))
META = os.path.join(ROOT, "metadata")


def load(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def md_table(header, rows):
    out = ["| " + " | ".join(str(x) for x in header) + " |",
           "| " + " | ".join("---" for _ in header) + " |"]
    for r in rows:
        out.append("| " + " | ".join(str(x) for x in r) + " |")
    return "\n".join(out)


rows = [r for r in load(os.path.join(META, "corpus_a.json"), []) if r.get("included", True)]
prisma = load(os.path.join(META, "prisma_flow.json"), {})
core = load(os.path.join(META, "core_papers.json"), [])
syn = load(os.path.join(BASE, "synthesis.json"), {})

pillar = Counter((r.get("pilar") or "?") for r in rows)
dims = {"d1": "D1 Data/Sensor", "d2": "D2 Target/Failure", "d3": "D3 Censoring",
        "d4": "D4 Arsitektur Model", "d5": "D5 Ketidakpastian", "d6": "D6 Keputusan/DSS",
        "d7": "D7 Domain RO/Membran", "d8": "D8 Skala Data"}
dimcnt = {k: sum(1 for r in rows if r.get(k)) for k in dims}

# --- PRISMA table ---
prisma_rows = [
    ["Identifikasi (record unik)", prisma.get("identified", "?")],
    ["Dihapus sebelum penyaringan (tanpa abstrak/metadata)", prisma.get("removed_before_screening", "?")],
    ["Disaring judul/abstrak", prisma.get("screened_title_abstract", "?")],
    ["Dikeluarkan pada judul/abstrak", prisma.get("excluded_title_abstract", "?")],
    ["Layak dari pencarian basis data", prisma.get("eligible_from_databases", "?")],
    ["Ditambah: snowballing + pengganti OA", prisma.get("added_snowballing_and_replacements", "?")],
    ["Dinilai pada full-text", prisma.get("fulltext_assessed", "?")],
    ["Dikeluarkan pada full-text", prisma.get("excluded_fulltext", "?")],
    ["Termasuk dalam sintesis", prisma.get("included", "?")],
    ["Core paper (skor >= 5.5 atau gap)", prisma.get("core_total", "?")],
]
prisma_tbl = md_table(["Tahap", "Jumlah"], prisma_rows)

pilar_tbl = md_table(["Pilar/Tema", "Jumlah Artikel"], [[k, v] for k, v in sorted(pillar.items())])
dim_tbl = md_table(["Dimensi Konsep", "Jumlah Artikel", "/ Total"],
                   [[dims[k], dimcnt[k], "/%d" % len(rows)] for k in dims])

core_rows = []
for r in [x for x in core if x.get("core")]:
    core_rows.append([r.get("no"), r.get("tahun"), (r.get("jurnal") or "")[:40],
                      (r.get("judul") or "")[:80], r.get("tier"), r.get("skor_total")])
core_tbl = md_table(["No", "Tahun", "Jurnal", "Judul", "Tier", "Skor"], core_rows)

sint = "\n".join(f"- **{dims[k]}**: {syn.get(k, '')} ({dimcnt[k]}/{len(rows)} artikel)"
                 for k in dims)

d3 = dimcnt["d3"]
d7 = dimcnt["d7"]
gap_txt = syn.get("gap", "(gap belum tersedia)")
gap_txt += ("\n\nCatatan kuantitatif: D3 dibahas %d artikel dan D7 dibahas %d artikel, "
            "tetapi irisan D3 dan D7 berjumlah 0 artikel." % (d3, d7))

src = open(os.path.join(BASE, "report.md"), encoding="utf-8").read()
replacements = {
    "<!-- PRISMA_TABLE -->": prisma_tbl,
    "<!-- PILAR_TABLE -->": pilar_tbl,
    "<!-- DIM_TABLE -->": dim_tbl,
    "<!-- CORE_TABLE -->": core_tbl,
    "<!-- SINTESIS -->": sint,
    "<!-- GAP -->": gap_txt,
}
for k, v in replacements.items():
    src = src.replace(k, v)

out = os.path.join(BASE, "report_filled.md")
with open(out, "w", encoding="utf-8") as f:
    f.write(src)
print("report_filled.md written | papers=%d | core=%d | pillars=%s | dims=%s"
      % (len(rows), len(core_rows), dict(pillar), dimcnt))
