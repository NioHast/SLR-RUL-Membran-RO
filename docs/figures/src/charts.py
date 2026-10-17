#!/usr/bin/env python3
"""
charts.py - Generate the data-driven SLR figures (fig06-fig12).

Reads the single source of truth metadata/corpus_a.json and writes PNG (300 dpi)
+ SVG into ../png and ../svg. Run from anywhere:

    python3 charts.py

Figures produced:
  fig02_slr_process          SLR method flow (Kitchenham + PRISMA + Wohlin)
  fig03_pipeline_dataflow    reproducible pipeline stages
  fig04_method_architecture  Bayesian LSTM-SURV + DSS architecture
  fig06_censoring_timeline   right-censoring concept (schematic)
  fig07_pillar_distribution  articles per pillar A-G
  fig08_dimension_coverage   articles per dimension D1-D8
  fig09_tier_funnel          694 -> 485 -> 101 -> 52 Inti -> 20 core + gap
  fig10_pillar_dimension_heatmap  pillar x dimension matrix
  fig11_year_trend           articles per publication year
  fig12_quality_distribution quality score histogram
"""
import json
import os
import collections
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CORPUS = os.path.join(ROOT, "metadata", "corpus_a.json")
PNG = os.path.abspath(os.path.join(HERE, "..", "png"))
SVG = os.path.abspath(os.path.join(HERE, "..", "svg"))
os.makedirs(PNG, exist_ok=True)
os.makedirs(SVG, exist_ok=True)

BLUE = "#1F4E78"
ORANGE = "#D97706"
TEAL = "#0F766E"
GRAY = "#6B7280"
LIGHT = "#E8EDF3"

plt.rcParams.update({
    "font.family": "DejaVu Serif",
    "font.size": 9,
    "axes.edgecolor": "#333333",
    "axes.linewidth": 0.8,
    "axes.grid": True,
    "grid.color": "#E5E7EB",
    "grid.linewidth": 0.6,
    "figure.facecolor": "white",
})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(PNG, name + ".png"), dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(os.path.join(SVG, name + ".svg"), bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  ok", name)


def snake_flow(rows, title, fname, accent=None):
    """Draw a snake grid of boxes with arrows (matplotlib).

    rows: list of rows (top to bottom); each row is a list of labels in
    *visual* left-to-right order. Travel alternates L->R and R->L so the
    connectors stay vertical. `accent` is a set of labels drawn in orange.
    """
    accent = accent or set()
    ncols = max(len(r) for r in rows)
    bw, bh, gx, gy = 1.5, 0.82, 1.72, 1.12
    fig, ax = plt.subplots(figsize=(1.0 + ncols * 1.55, 0.95 + len(rows) * 1.0))
    ax.set_xlim(-0.2, (ncols - 1) * gx + bw + 0.2)
    ax.set_ylim(-(len(rows) - 1) * gy - bh / 2 - 0.12, bh / 2 + 0.12)
    ax.axis("off")

    coords = {}
    for ri, row in enumerate(rows):
        lr = ri % 2 == 0
        offset = 0.0 if lr else (ncols - len(row)) * gx
        for ci, label in enumerate(row):
            x = offset + ci * gx
            y = -ri * gy
            coords[(ri, label)] = (x, y)
            hot = label in accent
            edge = ORANGE if hot else BLUE
            face = ORANGE if hot else "#EAF0F6"
            txt = "white" if hot else "#1F2937"
            ax.add_patch(FancyBboxPatch(
                (x, y - bh / 2), bw, bh,
                boxstyle="round,pad=0.02,rounding_size=0.09",
                linewidth=1.0, edgecolor=edge, facecolor=face, zorder=2))
            ax.text(x + bw / 2, y, textwrap.fill(label, 16),
                    ha="center", va="center", fontsize=7.3, color=txt, zorder=3)
        seq = list(row) if lr else list(reversed(row))
        for a, b in zip(seq, seq[1:]):
            x1, y1 = coords[(ri, a)]
            x2, y2 = coords[(ri, b)]
            if lr:
                start, end = (x1 + bw, y1), (x2, y2)
            else:
                start, end = (x1, y1), (x2 + bw, y2)
            ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=10,
                                         color="#4B5563", lw=1.0, shrinkA=1, shrinkB=1, zorder=1))
    for ri in range(len(rows) - 1):
        lr = ri % 2 == 0
        a = rows[ri][-1] if lr else rows[ri][0]
        next_lr = (ri + 1) % 2 == 0
        b = rows[ri + 1][0] if next_lr else rows[ri + 1][-1]
        x1, y1 = coords[(ri, a)]
        x2, y2 = coords[(ri + 1, b)]
        ax.add_patch(FancyArrowPatch((x1 + bw / 2, y1 - bh / 2), (x2 + bw / 2, y2 + bh / 2),
                                     arrowstyle="-|>", mutation_scale=10,
                                     color="#4B5563", lw=1.0, shrinkA=1, shrinkB=1, zorder=1))
    ax.set_title(title, fontsize=9.5, pad=4)
    save(fig, fname)


def fig02_slr_process():
    rows = [
        ["1. Protocol\nRQ, PICOC, IC/EC", "2. Search\nOpenAlex, 16 queries",
         "3. Deduplication\nn = 694", "4. Title/abstract\nn = 485"],
        ["8. Synthesis\nWebster-Watson", "7. Quality appraisal\nscore 0-10",
         "6. Extraction\nQ1-Q8, D1-D8", "5. Full-text\nn = 101"],
        ["9. Research gap", "10. Reporting\nPRISMA 2020"],
    ]
    snake_flow(rows, "Alur metode SLR (Kitchenham + PRISMA + Wohlin)", "fig02_slr_process")


def fig03_pipeline():
    rows = [
        ["Stage 1\nharvest -> rank -> select", "Stage 3\nISSN + quartile",
         "Stage 2\ndownload full text", "Stage 6\nMarker (Kaggle GPU)"],
        ["Stage 5\nverify references", "Stage 4\nbuild xlsx/docx/pdf",
         "Phase 5\nextraction (LLM)", "assemble\nphase2_assemble.py"],
    ]
    snake_flow(rows, "Pipeline reproducible: 1 -> 3 -> 2+6 -> analisis -> 4 -> 5",
               "fig03_pipeline_dataflow", accent={"Phase 5\nextraction (LLM)"})


def fig04_architecture():
    rows = [
        ["Sensor BWRO\nTMP, flow, TDS, suhu, pH", "Normalisasi\nASTM D4516",
         "Data waktu-ke-kejadian\n(T_i, d_i, X_i)", "Bayesian + LSTM-SURV\nPersamaan 4-5",
         "Weibull -> RUL + CI\nPersamaan 1-3"],
        ["Tindakan perawatan", "CIP / ganti / lanjut", "tau*", "Aturan biaya\nPersamaan 7"],
    ]
    snake_flow(rows, "Arsitektur dua lapis: prediksi RUL dan keputusan DSS",
               "fig04_method_architecture", accent={"Weibull -> RUL + CI\nPersamaan 1-3"})


def load_corpus():
    with open(CORPUS, encoding="utf-8") as f:
        return json.load(f)


def fig06_censoring():
    """Schematic timeline: observed event vs right-censored units."""
    fig, ax = plt.subplots(figsize=(7.2, 2.8))
    rows = [
        ("Unit A (event observed, d=1)", 0, 8.0, "event", "Event at t=8<br/>observed"),
        ("Unit B (study ends, d=0)", 0, 10.0, "censor", "Study end t=10<br/>right-censored"),
        ("Unit C (preventive CIP, d=0)", 0, 6.0, "censor", "Preventive CIP t=6<br/>right-censored"),
    ]
    for i, (label, start, end, kind, note) in enumerate(rows):
        y = len(rows) - i
        ax.plot([start, end], [y, y], color=BLUE, lw=2.2, solid_capstyle="round", zorder=2)
        ax.plot([start], [y], marker="o", ms=6, color=BLUE, zorder=3)
        if kind == "event":
            ax.plot([end], [y], marker="X", ms=9, color=ORANGE, zorder=4)
        else:
            ax.plot([end], [y], marker=">", ms=8, color=GRAY, zorder=4)
        ax.text(end + 0.2, y, note, va="center", fontsize=8, color="#333333")
        ax.set_ylabel("")
    ax.set_yticks([len(rows) - i for i in range(len(rows))])
    ax.set_yticklabels([r[0] for r in rows], fontsize=8.5)
    ax.set_xlabel("Waktu operasi efektif (jam/hari)")
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0.4, len(rows) + 0.8)
    ax.grid(axis="y", visible=False)
    ax.set_title("Ilustrasi data tersensor kanan (right-censored)", fontsize=10, pad=8)
    save(fig, "fig06_censoring_timeline")


def fig07_pillar(rows):
    cnt = collections.Counter((r.get("pilar") or "?")[:1] for r in rows)
    labels = ["A", "B", "C", "D", "E", "F", "G"]
    names = {
        "A": "A. Survival &\ncensored",
        "B": "B. Deep\nlearning RUL",
        "C": "C. Bayesian &\nuncertainty",
        "D": "D. Small-data /\ntransfer",
        "E": "E. Membrane /\nRO",
        "F": "F. DSS &\npredictive maint.",
        "G": "G. Indonesia /\nwater context",
    }
    vals = [cnt.get(k, 0) for k in labels]
    fig, ax = plt.subplots(figsize=(7.4, 3.4))
    colors = [BLUE if v == max(vals) else "#4B7BA8" for v in vals]
    bars = ax.bar(labels, vals, color=colors, width=0.62)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.4, str(v), ha="center", va="bottom", fontsize=9, fontweight="bold")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels([names[k] for k in labels], fontsize=7.5)
    ax.set_ylabel("Jumlah artikel")
    ax.set_title("Sebaran artikel per pilar (n = 101)", fontsize=10, pad=8)
    ax.set_ylim(0, max(vals) + 4)
    ax.grid(axis="x", visible=False)
    save(fig, "fig07_pillar_distribution")


def fig08_dimension(rows):
    dims = [
        ("D1", "Data /\nsensor", "d1"),
        ("D2", "Target /\nfailure", "d2"),
        ("D3", "Censoring", "d3"),
        ("D4", "Arsitektur\nmodel", "d4"),
        ("D5", "Ketidak-\npastian", "d5"),
        ("D6", "Keputusan\n/ DSS", "d6"),
        ("D7", "Domain\nRO", "d7"),
        ("D8", "Skala\ndata", "d8"),
    ]
    vals = [sum(1 for r in rows if r.get(k)) for _, _, k in dims]
    fig, ax = plt.subplots(figsize=(7.4, 3.4))
    colors = [ORANGE if k == "d3" else BLUE for _, _, k in dims]
    bars = ax.bar([d[0] for d in dims], vals, color=colors, width=0.62)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 1.2, str(v), ha="center", va="bottom", fontsize=9, fontweight="bold")
    ax.set_xticks(range(len(dims)))
    ax.set_xticklabels([d[1] for d in dims], fontsize=7.5)
    ax.set_ylabel("Jumlah artikel")
    ax.set_title("Cakupan dimensi konsep D1-D8 (n = 101)", fontsize=10, pad=8)
    ax.set_ylim(0, max(vals) + 12)
    ax.grid(axis="x", visible=False)
    ax.annotate("D3 censoring paling tipis relatif\nterhadap kebutuhan domain RO",
                xy=(2, vals[2]), xytext=(3.1, vals[2] + 28), fontsize=7.5, color=ORANGE,
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.0))
    save(fig, "fig08_dimension_coverage")


def fig09_funnel():
    stages = [
        ("Identified (OpenAlex)", 694),
        ("Screened (title/abstract)", 485),
        ("Included in synthesis", 101),
        ("Inti (core evidence)", 52),
        ("Core papers", 20),
    ]
    fig, ax = plt.subplots(figsize=(7.2, 3.3))
    labels = [s[0] for s in stages]
    vals = [s[1] for s in stages]
    y = list(range(len(stages)))[::-1]
    colors = [BLUE, "#3F6E9C", "#5E8CB8", "#8FB0CC", ORANGE]
    bars = ax.barh(y, vals, color=colors, height=0.58)
    for b, v in zip(bars, vals):
        ax.text(v + 8, b.get_y() + b.get_height() / 2, str(v), va="center", fontsize=9, fontweight="bold")
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8.5)
    ax.set_xlabel("Jumlah artikel")
    ax.set_xlim(0, 780)
    ax.set_title("Penyaringan korpus dan penentuan paper inti", fontsize=10, pad=8)
    ax.grid(axis="y", visible=False)
    ax.text(0.98, 0.06, "Gap: D3 (censoring) x D7 (RO) = 0 artikel",
            transform=ax.transAxes, ha="right", va="bottom",
            fontsize=8, color=ORANGE, fontweight="bold")
    save(fig, "fig09_tier_funnel")


def fig10_heatmap(rows):
    pillars = ["A", "B", "C", "D", "E", "F", "G"]
    dims = ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8"]
    grid = []
    for p in pillars:
        grid.append([sum(1 for r in rows if (r.get("pilar") or "")[:1] == p and r.get(d)) for d in dims])
    fig, ax = plt.subplots(figsize=(7.2, 3.9))
    im = ax.imshow(grid, cmap="Blues", aspect="auto")
    ax.set_xticks(range(len(dims)))
    ax.set_xticklabels([d.upper() for d in dims], fontsize=8.5)
    ax.set_yticks(range(len(pillars)))
    ax.set_yticklabels(pillars, fontsize=8.5)
    ax.set_xlabel("Dimensi konsep")
    ax.set_ylabel("Pilar")
    ax.set_title("Matriks konsep Webster-Watson: pilar x dimensi (jumlah artikel)", fontsize=9.5, pad=8)
    for i in range(len(pillars)):
        for j in range(len(dims)):
            v = grid[i][j]
            ax.text(j, i, str(v), ha="center", va="center", fontsize=7.5,
                    color="white" if v > max(max(x) for x in grid) * 0.55 else "#1F2937")
    ax.grid(False)
    cbar = fig.colorbar(im, ax=ax, fraction=0.035, pad=0.02)
    cbar.ax.tick_params(labelsize=7)
    save(fig, "fig10_pillar_dimension_heatmap")


def fig11_year(rows):
    cnt = collections.Counter(r.get("tahun") for r in rows if r.get("tahun"))
    years = sorted(cnt)
    vals = [cnt[y] for y in years]
    fig, ax = plt.subplots(figsize=(7.4, 3.2))
    ax.plot(years, vals, color=BLUE, marker="o", ms=4.5, lw=1.8)
    ax.fill_between(years, vals, color=LIGHT)
    for x, v in zip(years, vals):
        if v >= max(vals) * 0.6:
            ax.text(x, v + 0.5, str(v), ha="center", fontsize=7.5)
    ax.set_xlabel("Tahun publikasi")
    ax.set_ylabel("Jumlah artikel")
    ax.set_title("Tren publikasi korpus (2015-2026)", fontsize=10, pad=8)
    ax.set_xlim(min(years) - 0.5, max(years) + 0.5)
    save(fig, "fig11_year_trend")


def fig12_quality(rows):
    ks = [r.get("kualitas_skor") for r in rows if r.get("kualitas_skor") is not None]
    fig, ax = plt.subplots(figsize=(6.6, 2.9))
    bins = range(4, 11)
    ax.hist(ks, bins=bins, color=BLUE, edgecolor="white", rwidth=0.88)
    ax.set_xlabel("Skor kualitas (Q1-Q8, skala 0-10)")
    ax.set_ylabel("Jumlah artikel")
    ax.set_title("Sebaran skor kualitas studi (n = %d)" % len(ks), fontsize=10, pad=8)
    ax.set_xticks(list(bins))
    save(fig, "fig12_quality_distribution")


def main():
    rows = load_corpus()
    print("charts.py | corpus:", len(rows))
    fig02_slr_process()
    fig03_pipeline()
    fig04_architecture()
    fig06_censoring()
    fig07_pillar(rows)
    fig08_dimension(rows)
    fig09_funnel()
    fig10_heatmap(rows)
    fig11_year(rows)
    fig12_quality(rows)
    print("done: 7 charts -> png/ + svg/")


if __name__ == "__main__":
    main()
