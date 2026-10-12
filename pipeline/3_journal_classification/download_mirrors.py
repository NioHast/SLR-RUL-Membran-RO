#!/usr/bin/env python3
"""
download_mirrors.py
-------------------
Download ALL public mirror datasets used by this SLR pipeline into the
../mirror_data/ folder (next to the source_code/ folder).

All these sources are public & require no credentials. See mirror_data/README.md
for license + attribution details.

INPUT:
    - No input file (only downloads from the internet).
OUTPUT:
    - ../mirror_data/sjr_quart.csv     (SCImago 2022 ed.: 'SJR Best Quartile' column).
    - ../mirror_data/sjr_all.csv       (SCImago panel 1999-2025).
    - ../mirror_data/scopus_titles.tsv (list of Scopus titles).
How to run:
        python3 download_mirrors.py
NOTE:
    The destination folder is computed relative to the location of this file
    (HERE/../mirror_data), so the folder structure must be kept. Other scripts in
    the pipeline use absolute paths (e.g. BASE="/tmp/opencode/slr") which you MUST
    change to your own working location.
"""

import os, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
MIR  = os.path.join(os.path.dirname(HERE), "mirror_data")
os.makedirs(MIR, exist_ok=True)

# Local filename -> public source URL.
FILES = {
    # SCImago 2022 ed. - contains the 'SJR Best Quartile' column (official quartile derived from Scopus)
    "sjr_quart.csv": "https://huggingface.co/datasets/inria-soda/carte-benchmark/resolve/main/data_raw/journal_sjr.csv",
    # SCImago panel 1999-2025 (SJR + ISSN, without a quartile column)
    "sjr_all.csv":   "https://raw.githubusercontent.com/Michael-E-Rose/SCImagoJournalRankIndicators/master/all.csv",
    # List of Scopus titles (Active/Inactive status + coverage), from Source List 2021
    "scopus_titles.tsv": "https://raw.githubusercontent.com/dhimmel/scopus/main/data/titles.tsv",
}

def main():
    """Download each file that does not yet exist (safe to repeat / idempotent)."""
    for name, url in FILES.items():
        dst = os.path.join(MIR, name)
        # Skip if the file already exists and is not empty.
        if os.path.exists(dst) and os.path.getsize(dst) > 0:
            print(f"[skip] {name} sudah ada ({os.path.getsize(dst)} bytes)")
            continue
        print(f"[get ] {name}  <-  {url}")
        try:
            urllib.request.urlretrieve(url, dst)
            print(f"       ok {os.path.getsize(dst)} bytes")
        except Exception as e:
            print(f"       GAGAL: {e}")
    print("\nSelesai. File di:", MIR)

if __name__ == "__main__":
    main()
