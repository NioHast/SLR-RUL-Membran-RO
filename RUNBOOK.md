> 🇬🇧 [English](RUNBOOK.md) | 🇮🇩 [Bahasa Indonesia](RUNBOOK.id.md)

# RUNBOOK - End-to-End Flow

A guide to re-running the ENTIRE SLR pipeline from scratch. It explains the order of steps and
the **interdependencies between folders** (`pipeline/`, `metadata/`, `mirror_data/`, `papers_analysis/`, `docs/`).

## Interdependency Diagram
```
  pipeline/1_search_and_select/  --->  metadata/  (pool, ranked, selected, corpus)
            |
  pipeline/3_journal_classification/  <-- mirror_data/ (SJR/Scopus)  --->  metadata/ (issn, quartile)
            |
  pipeline/2_get_fulltext/  +  pipeline/6_fulltext_extraction_kaggle/  --->  papers_analysis/ (full_text.md/pdf, figures)
            |
  (per-paper analysis: extraction.json, analysis.txt)  --->  metadata/corpus_a.json
            |
  pipeline/4_build_deliverables/  -------------------------------------->  docs/ (xlsx, docx, pdf, html)
            |
  pipeline/5_verify_references/  (verify reference DOIs)
```

## Prerequisites
- **Python 3** + packages: `openpyxl`, `python-docx`, `beautifulsoup4`, `lxml`, `pdfplumber`, `PyMuPDF`, `camelot-py`, `kaggle`.
  ```
  pip install --break-system-packages openpyxl python-docx beautifulsoup4 lxml pdfplumber PyMuPDF "camelot-py[cv]" kaggle
  ```
- **LibreOffice** (headless) for DOCX -> PDF conversion.
- **Kaggle account + API token** (for stage 6): store it in `~/.kaggle/access_token` and set `export KAGGLE_API_TOKEN=$(cat ~/.kaggle/access_token)`. **The token is not stored in this repo.**
- **Important note:** some scripts use **absolute paths** (e.g. `BASE="/tmp/opencode/slr"`). Change them to your own working location. Run according to the README in each subfolder.

## Steps
1. **Corpus search & selection** - `pipeline/1_search_and_select/`
   Harvest metadata (OpenAlex/Crossref), relevance ranking, corpus selection -> `metadata/pool.json`, `ranked.json`, `selected*.json`.
2. **Journal classification** - `pipeline/3_journal_classification/` (+ `mirror_data/`)
   Download the SJR mirror (`download_mirrors.py`), map ISSNs (`issn.py`), assign quartiles (`classify_scopus.py`) -> `metadata/issn_map.json`, `scopus_official.json`. Check OA/license: `check_open_access.py` -> `metadata/open_access_status.json`.
3. **Full-text retrieval & extraction** - `pipeline/2_get_fulltext/` + `pipeline/6_fulltext_extraction_kaggle/`
   Download OA (`download_fulltext.py`/Playwright) then perform full extraction with **Marker** on the Kaggle GPU (kernel + merge) -> `papers_analysis/<folder>/full_text.md`, `figures/`, `meta.json`.
4. **Per-paper analysis (Phase 5)** - produce `papers_analysis/<folder>/extraction.json` + `analysis.txt` -> merged into `metadata/corpus_a.json`.
5. **Build deliverables** - `pipeline/4_build_deliverables/`
   `fill_report.py` -> `build_xlsx.py` -> `build_docx.py` -> `build_article_docx.py` -> (LibreOffice) PDF -> `docs/`.
6. **Reference verification** - `pipeline/5_verify_references/` (`verify_refs.py`).

## Folder Roles at a Glance
| Folder | Role | Type |
|---|---|---|
| `pipeline/` (1-6) | Source code for all stages | CODE |
| `metadata/` | Intermediate data & corpus (JSON) | DATA |
| `mirror_data/` | SJR/Scopus dataset (SCImago) | DATA |
| `papers_analysis/` | Analysis results + (OA) full-text & figures | OUTPUT |
| `docs/` | Final deliverables (xlsx/docx/pdf/html) | OUTPUT |
