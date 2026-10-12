> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# mirror_data/ - SJR/Scopus Data (SCImago)

Public data used for **journal quartile classification**. All files in this folder are
**public copies (mirrors)** of SCImago/Scopus data, downloaded so that the SLR pipeline can run
**automatically without login/credentials**. Official sources: **SCImago** (https://www.scimagojr.com) and
**Scopus** (Elsevier).

> **Attribution required when cited:**
> SCImago. (n.d.). *SJR - SCImago Journal & Country Rank.* Retrieved from https://www.scimagojr.com

## Contents
- `sjr_quart.csv` - SCImago ed. 2022 (column **"SJR Best Quartile"**, Q1-Q4).
- `sjr_all.csv` - SCImago panel 1999-2025 (SJR + ISSN).
- `scopus_titles.tsv` - Scopus title list 2021.

## Source & Details for Each File
**1) `sjr_quart.csv`**
- Contents: SCImago journal ranking + the "SJR Best Quartile" column (Q1-Q4), ISSN, SJR, H-index, Coverage, Categories, Areas.
- Edition: **SCImago 2022** | Size: ~8 MB, 27,955 rows.
- Mirror: https://huggingface.co/datasets/inria-soda/carte-benchmark (file `data_raw/journal_sjr.csv`).
- Raw URL: `https://huggingface.co/datasets/inria-soda/carte-benchmark/resolve/main/data_raw/journal_sjr.csv`
- Origin: part of the INRIA research team's (SODA) benchmark dataset.
- License: SCImago data (CC BY-NC; non-commercial, with attribution).

**2) `sjr_all.csv`**
- Contents: SCImago panel 1999-2025 (Title, field, year, SJR, h-index, avg_citations, Issn, Sourceid) - WITHOUT a quartile column.
- Size: ~84 MB, 1,024,562 rows.
- Mirror: https://github.com/Michael-E-Rose/SCImagoJournalRankIndicators
- Raw URL: `https://raw.githubusercontent.com/Michael-E-Rose/SCImagoJournalRankIndicators/master/all.csv`
- Note: used to (a) detect new journals, (b) derive per-field quartiles for the latest year when not present in `sjr_quart.csv`.
- License: SCImago data (CC BY-NC), compiled by third-party researchers.

**3) `scopus_titles.tsv`**
- Contents: Scopus title list (scopus_id, title_name, ISSN print/electronic, Active or Inactive, Coverage, ASJC, etc.).
- Edition: **Scopus Source List 2021** | Size: ~5.7 MB, 82,234 rows.
- Mirror: https://github.com/dhimmel/scopus (file `data/titles.tsv`).
- Raw URL: `https://raw.githubusercontent.com/dhimmel/scopus/main/data/titles.tsv`
- Note: only a reference for indexed status; version 2021 (old).
- License: Scopus data (Elsevier) - derived dataset for research.

## Important Notes
- Third-party mirrors may be **outdated / incomplete**. For formal citations, still refer to the original sources (SCImago/Scopus) + access date.
- For 100% official Scopus data (coverage + latest active status), a "Scopus Source List" is needed (download via a Scopus account/subscription) - cannot be automated.
- How to re-download: `python3 ../pipeline/3_journal_classification/download_mirrors.py`.
- Mirror download date in this package: **2026-10-11** (Asia/Jakarta).
