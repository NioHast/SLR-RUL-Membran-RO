> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# 5_verify_references/ - Reference Verification

This folder verifies the existence of supporting references by matching
their titles against Crossref and displaying the resulting DOIs.

## Flow (order of execution)

```
verify_refs.py   ->   (print to screen / stdout)
```

There are no inter-file dependencies in this folder.

## Files

### `verify_refs.py`
- **Purpose:** Search each reference title (the `refs` list embedded in the script) in Crossref and display the year, journal, title, and DOI of the search results (top 2 candidates per title).
- **INPUT:** no file (the title list is embedded in the script); network source `https://api.crossref.org/works`.
- **OUTPUT:** prints to stdout only (writes no file).
- **Run:** `python3 verify_refs.py`

> **NOTE:** This script uses no file paths, so no absolute paths need to be
> changed. Other scripts in the pipeline use absolute paths
> (e.g. `BASE="/tmp/opencode/slr"`) that you must adjust yourself.
