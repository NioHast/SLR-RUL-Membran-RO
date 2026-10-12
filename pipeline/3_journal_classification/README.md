> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# 3_journal_classification/ - Journal Classification (Scopus Quartile)

This folder assigns a Scopus quartile to each corpus journal based on the SCImago
mirror dataset (Scopus derivative), and provides independent verification.

## Flow (order of execution)

```
download_mirrors.py  ->  issn.py  ->  classify_scopus.py  ->  verify_scopus.py
        |                   |                 |                     |
 ../mirror_data/*     issn_map.json    corpus_*.json        scopus_check.json
                                        (classification column)

check_open_access.py  (standalone: check OA status + license)
        |
 open_access_status.json
```

1. `download_mirrors.py` - download the SCImago mirror.
2. `issn.py` - map DOI -> ISSN/venue.
3. `classify_scopus.py` - assign the Scopus quartile per article.
4. `verify_scopus.py` - cross-verify Scopus coverage.
5. `check_open_access.py` - (standalone) check OA + license.

## Files

### `download_mirrors.py`
- **Purpose:** Download all public mirror datasets (SCImago SJR Best Quartile, SJR panel 1999-2025, Scopus title list).
- **INPUT:** none (downloaded from the internet).
- **OUTPUT:** `../mirror_data/sjr_quart.csv`, `../mirror_data/sjr_all.csv`, `../mirror_data/scopus_titles.tsv`.
- **Run:** `python3 download_mirrors.py`

### `issn.py`
- **Purpose:** Fetch the ISSN-L, list of ISSNs, journal name, and DOAJ status for each DOI from OpenAlex.
- **INPUT:** `corpus_*.json`.
- **OUTPUT:** `issn_map.json`.
- **Run:** `python3 issn.py`

### `classify_scopus.py`
- **Purpose:** Assign the `klasifikasi` field of each article: `SJR Best Quartile` (official, ed. 2022) -> fallback SJR 2024 (derived quartile) -> "Belum terverifikasi".
- **INPUT:** `data/issn_map.json`, `../mirror_data/sjr_quart.csv`, `../mirror_data/sjr_all.csv`.
- **OUTPUT:** `data/corpus_*.json` (rewritten with the `klasifikasi` column).
- **Run:** `python3 classify_scopus.py`

### `verify_scopus.py`
- **Purpose:** Independently recompute how many corpus journals are actually indexed in Scopus + their quartile (cross-verification of the classification).
- **INPUT:** `issn_map.json`, `sjr_all.csv` (copy from `../mirror_data/` into this folder first).
- **OUTPUT:** `scopus_check.json`.
- **Run:** `python3 verify_scopus.py`

### `check_open_access.py`
- **Purpose:** Check the Open Access status + license of each article via Unpaywall to determine which ones are safe/legal to include as full-text (OA + CC license).
- **INPUT:** `../../metadata/corpus_a.json` (fallback: `../../source_code/data/corpus_a.json`).
- **OUTPUT:** `open_access_status.json` (in the same folder).
- **Run:** `python3 check_open_access.py` (requires internet).

> **NOTE:** Some scripts in this folder use paths relative to the file location
> (`HERE/data`, `HERE/../mirror_data`), while others use the working directory.
> Other scripts in the pipeline use absolute paths (e.g. `BASE="/tmp/opencode/slr"`)
> that you must adjust yourself.
