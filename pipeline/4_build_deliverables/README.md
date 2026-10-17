> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# 4_build_deliverables/ - Building Deliverables

Turns corpus data + synthesis into the final deliverables. All outputs are written
into `docs/` (no absolute paths).

## Flow (order)

```
docs/figures/src/build_figures.sh   -> docs/figures/png/*.png + svg/*.svg
fill_report.py                      -> report_filled.md
build_docx.py                       -> docs/SLR_Laporan.docx  (+ PDF via LibreOffice)
build_xlsx.py                       -> docs/SLR_Korpus.xlsx   (7 sheets)
build_article_docx.py               -> docs/SLR_Artikel_Jurnal.docx (+ PDF)
build_presentation.py               -> docs/SLR_Presentasi.html (+ PDF via Chrome)
```

## Scripts

| Script | Purpose | Input -> Output |
|---|---|---|
| `fill_report.py` | Fill markers with real numbers from the single source of truth | `metadata/corpus_a.json`, `prisma_flow.json`, `core_papers.json`, `synthesis.json`, `report.md` -> `report_filled.md` |
| `build_docx.py` | Thesis-style report (TNR 12, margins 4-4-3-3, 1.5 spacing) + figures | `report_filled.md` -> `docs/SLR_Laporan.docx` |
| `build_xlsx.py` | 7-sheet workbook (adds "Paper Inti & Skor") | corpus + synthesis + core -> `docs/SLR_Korpus.xlsx` |
| `build_article_docx.py` | 2-column journal article + figures | `article.md` -> `docs/SLR_Artikel_Jurnal.docx` |
| `build_presentation.py` | Idempotent: embed figures (base64, offline) + sync numbers | `docs/SLR_Presentasi.html` -> rewritten in place |

## Figure markers
`report.md` and `article.md` support `{{FIG:file.png|caption|width_cm}}`; files are
resolved from `docs/figures/png/` and rendered with an automatic `Gambar N.` caption.
Wide tables and figures in the article span both columns via section breaks.

## Text/data sources
- `report.md` - report template with markers (filled by `fill_report.py`).
- `synthesis.json` - narrative synthesis per dimension + gap + theory + concepts.
- `article.md` - journal article manuscript (separated by `<!--BODY-->`).
- Presentation prompt: [`../prompts/presentation.md`](../prompts/presentation.md).
- Style contract: [`../prompts/deliverable_style.md`](../prompts/deliverable_style.md).
