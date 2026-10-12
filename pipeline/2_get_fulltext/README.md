> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# 2_get_fulltext/ - Full-Text Retrieval

This folder downloads **Open Access** PDFs automatically, then uses Playwright
as a fallback for articles still marked *closed* but whose PDFs are actually
publicly available.

## Flow (order of execution)

```
download_fulltext.py  ->  download_closed_playwright.py
        |                            |
  ../full_text/*.pdf          ../full_text/*.pdf
  fulltext_report.json        closed_playwright_report.json
```

1. `download_fulltext.py` - download all OA PDFs (OpenAlex + Unpaywall).
2. `download_closed_playwright.py` - (fallback) try articles with `closed` status via the browser.

## Files

### `download_fulltext.py`
- **Purpose:** Download Open Access full-text PDFs for the entire corpus from all known OA locations (OpenAlex `best_oa_location` + `locations`, and Unpaywall `best_oa_location` + `oa_locations`).
- **INPUT:** `data/corpus_*.json`.
- **OUTPUT:** `../full_text/00X_*.pdf` and `../full_text/fulltext_report.json` (status ok/skip/closed).
- **Run:** `python3 download_fulltext.py` (safe to repeat; existing files are skipped).

### `download_closed_playwright.py`
- **Purpose:** For each article with `closed` status, open the DOI page with Playwright (Chrome), look for a PDF link/button, and download only if it is truly a public PDF; skip those requiring login.
- **INPUT:** `data/corpus_*.json` + `../full_text/fulltext_report.json`.
- **OUTPUT:** `../full_text/00X_*.pdf` and `../full_text/closed_playwright_report.json`.
- **Run:** `python3 download_closed_playwright.py` (requires Playwright + Chrome).

> **NOTE:** Paths are computed relative to the file location (`HERE/data` -> `../full_text`),
> so the folder structure must be preserved. Other scripts in the pipeline use absolute paths
> (e.g. `BASE="/tmp/opencode/slr"`) that you must adjust yourself.
