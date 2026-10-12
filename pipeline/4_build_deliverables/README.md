> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# 4_build_deliverables/ - Building Deliverables (Report, Excel, Article)

This folder turns the corpus data + synthesis into the final deliverables: a Word report,
an Excel spreadsheet, and a 2-column journal article.

## Flow (order of execution)

```
fill_report.py  ->  build_docx.py        ->  SLR_Laporan.docx
      |                                          
 report_filled.md                               

build_xlsx.py          ->  SLR_Korpus.xlsx
build_article_docx.py  ->  SLR_Artikel_Jurnal.docx
```

1. `fill_report.py` - fill markers in `report.md` -> `report_filled.md`.
2. `build_docx.py` - `report_filled.md` -> `SLR_Laporan.docx`.
3. `build_xlsx.py` - corpus + synthesis -> `SLR_Korpus.xlsx`.
4. `build_article_docx.py` - `article.md` -> `SLR_Artikel_Jurnal.docx`.

## Script files

### `fill_report.py`
- **Purpose:** Replace HTML markers in `report.md` (`<!-- PRISMA -->`, `<!-- PILAR -->`, `<!-- DIMENSI -->`, `<!-- TABLES -->`, `<!-- SINTESIS -->`, `<!-- GAP -->`) with tables/text containing the actual numbers.
- **INPUT:** `BASE/corpus_*.json`, `BASE/harvest_stats.json`, `BASE/synthesis.json`, `BASE/report.md`.
- **OUTPUT:** `BASE/report_filled.md`.
- **Run:** `python3 fill_report.py`

### `build_xlsx.py`
- **Purpose:** Build the 6-sheet `SLR_Korpus.xlsx` (Korpus, Ringkasan & Status, Matriks Konsep, Sintesis & Gap, Peta Teori, Konsep Kunci); sort by quartile then year, highlight the reference paper (Gao), D1-D8 checkmark matrix.
- **INPUT:** `BASE/corpus_*.json`, `BASE/harvest_stats.json`, `BASE/synthesis.json`.
- **OUTPUT:** `/home/nioha/Downloads/SLR_Korpus.xlsx`.
- **Run:** `python3 build_xlsx.py`

### `build_docx.py`
- **Purpose:** Convert the Markdown report into `SLR_Laporan.docx` (Times New Roman 12, margins 4-4-3-3 cm, 1.5 spacing, tables without fill).
- **INPUT:** `report_filled.md` (fallback `report.md`).
- **OUTPUT:** `/home/nioha/Downloads/SLR_Laporan.docx`.
- **Run:** `python3 build_docx.py`

### `build_article_docx.py`
- **Purpose:** Build the 2-column `.docx` journal article: 1-column front matter, 2-column body (separated by the `<!--BODY-->` marker).
- **INPUT:** `BASE/article.md`.
- **OUTPUT:** `/home/nioha/Downloads/SLR_Artikel_Jurnal.docx`.
- **Run:** `python3 build_article_docx.py`

## Text/data sources (not scripts)
- `report.md` - report template containing markers (filled by `fill_report.py`).
- `synthesis.json` - narrative synthesis per dimension + research gap + theory + concepts.
- `article.md` - journal article manuscript (separated by `<!--BODY-->`).
- The presentation prompt now lives in [`../prompts/presentation.md`](../prompts/presentation.md).

> **NOTE:** Scripts in this folder use **ABSOLUTE** paths. `BASE="/tmp/opencode/slr"`
> and `OUT="/home/nioha/Downloads/..."` MUST be changed to your own location
> before running.
