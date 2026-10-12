> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# 1_search_and_select/ - Search & Corpus Selection

This folder performs **metadata harvesting** from OpenAlex and selects the SLR core
corpus (relevance ranking + mapping of concept pillars A-G).

## Flow (order of execution)

```
harvest.py  ->  supp.py (optional)  ->  rank.py  ->  select.py
   |                  |                   |             |
 pool.json        pool.json           ranked.json   selected.json
 pool.csv         (expanded)          (score)       (core corpus)
```

1. `harvest.py` - initial harvest of 16 queries.
2. `supp.py` - (optional) add articles from 8 supplementary queries.
3. `rank.py` - score the relevance of each article.
4. `select.py` - select the core corpus + mark pillars.

## Files

### `harvest.py`
- **Purpose:** Send 16 search queries to the OpenAlex API and merge the results into a single set of unique articles (dedup by OpenAlex ID).
- **INPUT:** no file (queries embedded in the script); network source `https://api.openalex.org/works`.
- **OUTPUT:** `pool.json` (all unique articles), `pool.csv` (quick summary).
- **Run:** `python3 harvest.py`

### `supp.py`
- **Purpose:** Run 8 additional queries (data limitations, few-shot prognostics, Indonesian context) then add **new** results to `pool.json` without overwriting existing records.
- **INPUT:** `pool.json`.
- **OUTPUT:** `pool.json` (expanded).
- **Run:** `python3 supp.py`

### `rank.py`
- **Purpose:** Score each article based on pillar keywords (RUL/censoring/DL/RO domain), a bonus for keywords in the title, and a logarithmic citation weight.
- **INPUT:** `pool.json`.
- **OUTPUT:** `ranked.json` (each article gets a `_score` field, already sorted).
- **Run:** `python3 rank.py`

### `select.py`
- **Purpose:** Discard medical-topic/abstract-less articles, mark pillars A-G, then select the core corpus (priority for 4 reference articles, quota of 72 articles).
- **INPUT:** `ranked.json`.
- **OUTPUT:** `selected.json` (core corpus; each article has `pillars`).
- **Run:** `python3 select.py`

> **NOTE:** Scripts in this folder read/write files in the **current working directory**
> (not absolute paths). Run from the correct folder, or adjust the paths.
