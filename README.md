> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# SLR: Remaining Useful Life (RUL) Prediction of Reverse Osmosis Membranes with Survival Analysis & Deep Learning

A Systematic Literature Review (SLR) of **101 articles** on RUL prediction for reverse
osmosis (RO)/desalination membranes, with emphasis on **censored data (right-censored)**
and **small data scales**, as the basis for a thesis research in Information Systems.

**Author:** Muhammad Nio Hastungkoro (Student ID 30000226410017) - Master of Information Systems,
Graduate School, Universitas Diponegoro. Contact: mnioh@students.undip.ac.id

## Repository Structure
| Folder | Contents |
|---|---|
| `docs/` | Main deliverables: SLR protocol, corpus (Excel), report, journal article, presentation, decision log. |
| `papers_analysis/` | Per-paper analysis results (`extraction.json` + `analysis.txt`) for 101 articles. |
| `pipeline/` | Pipeline source code (search, journal classification, document building, reference verification). |
| `metadata/` | Intermediate data/JSON: master corpus, ISSN & journal quartile mapping, search statistics. |
| `pipeline/6_fulltext_extraction_kaggle/` | Kaggle kernel code (full-text extraction with Marker on GPU). |
| `mirror_data/` | SJR/Scopus data (SCImago) used for quartile classification (source: README.md). |

## Method (summary)
Kitchenham & Charters (procedure) + PRISMA 2020 (reporting) + Webster & Watson (concept matrix)
+ Wohlin (snowballing). Hybrid search; quartile classification via SCImago/SJR (Scopus derivative).
Full-text extraction uses **Marker** (on Kaggle T4 GPU); per-paper analysis uses the Q1-Q8
quality rubric, strict-requirement dimensions (D1-D8), and relevance levels (Core-Method / Core-Domain /
Core-Method+Domain / Supporting / Context).

## Key Findings
- Corpus: **101 articles** (Q1/Q2/Q3). The censoring dimension (D3) is discussed by 28 articles.
- **Method x domain intersection (Core-Method+Domain) is only 2 articles** -> a real research gap.

## How to Reproduce
1. `pipeline/1_search_and_select/`: harvest metadata (OpenAlex/Crossref) -> `metadata/`.
2. `pipeline/3_journal_classification/`: quartile classification (SCImago) + `mirror_data/`.
3. `pipeline/2_get_fulltext/` + `pipeline/6_fulltext_extraction_kaggle/`: obtain & extract full-text (Marker via Kaggle GPU).
4. `pipeline/4_build_deliverables/`: build `docs/` (Excel, Word, PDF, presentation).
(See the README in each folder. Scripts use the absolute path `/tmp/opencode/slr`; adjust as needed.)

## Copyright Notes (IMPORTANT)
- **Open Access + Creative Commons license (77 of 101 articles)** -> full-text (`fulltext.pdf`)
  **included** because the license permits redistribution (with **attribution**; see `SOURCE.txt` in each folder).
- **The rest (24 articles: closed / bronze / unclear license)** -> **analysis results only**
  (`extraction.json`, `analysis.txt`) + **DOI**, since there is no redistribution permission.
- OA/license status is checked automatically: `pipeline/3_journal_classification/check_open_access.py`
  (Unpaywall API) -> results in `metadata/open_access_status.json`.
- The code that obtains & extracts full-text is included (`pipeline/`, including `pipeline/6_fulltext_extraction_kaggle/`) so it is **reproducible**.

## Data Attribution
Journal quartiles/classification are sourced from **SCImago (SJR)** - https://www.scimagojr.com (Scopus derivative).
Data mirror: see `mirror_data/README.md`.

## License
- **Code (author-made): MIT-0** - free to use, **no attribution** (see `LICENSE`).
- **Author-made content (documents, analysis results, metadata): CC0 1.0** - public domain, **no attribution** (see `LICENSE-CONTENT`).
- **Third-party data/articles: their own licenses remain** (SCImago = CC BY-NC; OA articles per their license) - see `NOTICE`.
- Summary: *My code & content: MIT-0/CC0 (no attribution). Third-party data (SCImago, OA articles) retain their licenses.*

> This is a research artifact. Issues/PRs may not be monitored.
