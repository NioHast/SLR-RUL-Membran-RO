> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# pipeline/ - Source Code (reproducible)

Code to re-run the SLR from scratch. Grouped in order:

| Folder | Function | Detail |
|---|---|---|
| `1_search_and_select/` | Harvest metadata (OpenAlex/Crossref), relevance ranking, corpus selection (`harvest.py`, `rank.py`, `select.py`, `supp.py`). | Per-file detail: see [`README.md`](1_search_and_select/README.md) |
| `2_get_fulltext/` | Obtain Open Access full-text (`download_fulltext.py`) + Playwright fallback (`download_closed_playwright.py`). | Per-file detail: see [`README.md`](2_get_fulltext/README.md) |
| `3_journal_classification/` | Download SJR mirrors (`download_mirrors.py`), fetch ISSN (`issn.py`), Scopus quartile classification (`classify_scopus.py`, `verify_scopus.py`). | Per-file detail: see [`README.md`](3_journal_classification/README.md) |
| `4_build_deliverables/` | Build outputs: `fill_report.py`, `build_xlsx.py`, `build_docx.py`, `build_article_docx.py` + text sources (`report.md`, `synthesis.json`, `article.md`). | Per-file detail: see [`README.md`](4_build_deliverables/README.md) |
| `5_verify_references/` | Verify reference DOIs via Crossref (`verify_refs.py`). |
| `6_fulltext_extraction_kaggle/` | Kaggle kernel/notebook for full-text extraction with Marker (GPU). See the README in the subfolder. |
| `prompts/` | Versioned AI prompt templates used to produce the analysis & deliverables. See [`README.md`](prompts/README.md). |

Per-file detail: see `README.md` in each subfolder. Per-file detail: see [`README.md`](5_verify_references/README.md) |

## Notes
- Scripts use **absolute paths** (e.g. `BASE=/tmp/opencode/slr`); adjust to your own location.
- Input/output data (JSON) is in `../metadata/`; SJR mirror in `../mirror_data/`.
- Python dependencies: `openpyxl`, `python-docx`, `beautifulsoup4`, `lxml`, `pdfplumber`, `PyMuPDF`, `camelot`.
- PDF conversion uses LibreOffice (headless).
