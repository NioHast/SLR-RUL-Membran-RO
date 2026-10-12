> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# papers_analysis/ - Per-Paper Analysis

One subfolder per article (101 folders). Folder name:
`NNN_FirstAuthor_Year_Quartile_Title` (NNN = sequence number matching the "No" column in `docs/SLR_Korpus.xlsx`).

## Contents of each folder
Applies to all folders:
- `extraction.json` - structured extraction from the **full-text**: identity, pillar, summary,
  contribution, key findings, **dimensions D1-D8 + rationale (evidence)**, **relevance level**,
  **quality score (Q1-Q8)**, quantitative data, method, limitations, funding/COI, inclusion status.
- `analysis.txt` - narrative analysis (in Indonesian) of the full content.

**ONLY for Open Access articles with a Creative Commons license** (77 folders), the following are added:
- `full_text.pdf` - PDF copy of the full-text (original article).
- `full_text.md` - full-text extraction result via **Marker**: column-aware text + **formulas in LaTeX** + Markdown tables.
- `figures/` - figures/images extracted from the article.
- `meta.json` - Marker output metadata (page count, statistics, etc.).
- `SOURCE.txt` - DOI + license + **required attribution** details.

## Full-Text Policy (WHY some are present and some are not)
This repository includes full-text **only for articles that are Open Access AND licensed under
Creative Commons (CC)** - permitted for redistribution (with attribution).

- **77 of 101 articles** are **OA + CC** -> `fulltext.pdf` **included**.
- The other **24 articles** do **not** include their `fulltext.pdf` because:
  - **closed** (subscription) -> may not be redistributed, or
  - **bronze / no license / "other-oa"** -> free to read but **no redistribution permission**.
  For these articles only the **analysis results** (`extraction.json`, `analysis.txt`) + **DOI** are available.

Attribution: every `fulltext.pdf` remains the property of its original author/publisher; the CC license requires
attribution (see `SOURCE.txt` in each folder).

## How to check OA status/legality
Script: `../pipeline/3_journal_classification/check_open_access.py` (uses the Unpaywall API).
Full results (OA status, license, included/excluded): `../metadata/open_access_status.json`.
