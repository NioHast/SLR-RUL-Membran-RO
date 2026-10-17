#!/usr/bin/env python3
"""
build_presentation.py - Validate and build the self-contained reveal.js deck.

Purpose:
    The deck (docs/SLR_Presentasi.html) is hand-authored with native dark-theme
    visuals (HTML/CSS/SVG) instead of embedded PNGs, so it stays offline and matches
    the presentation design. This script:
      1. validates structure (17 slides), offline safety (no external refs),
         and key numbers;
      2. builds docs/SLR_Presentasi.pdf with headless Chrome.

INPUT:
    - docs/SLR_Presentasi.html
OUTPUT:
    - docs/SLR_Presentasi.pdf
How to run:
        python3 build_presentation.py
NOTE:
    Requires Google Chrome at /usr/bin/google-chrome (or set CHROME env var).
"""
import os
import re
import shutil
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", ".."))
HTML = os.path.join(ROOT, "docs", "SLR_Presentasi.html")
PDF = os.path.join(ROOT, "docs", "SLR_Presentasi.pdf")

s = open(HTML, encoding="utf-8").read()

checks = {
    "sections == 17": s.count("<section") == 17,
    "no external src/href": not re.search(r'(?:src|href)="https?://', s),
    "694 present": "694" in s,
    "485 present": "485" in s,
    "101 assessed present": "101" in s,
    "79 included present": "79" in s,
    "46 Inti present": "46" in s,
    "19 core present": "19" in s,
    "D3 x D7 = 0 present": "D3 × D7" in s or "D3 x D7" in s,
}
ok = True
for name, passed in checks.items():
    print(("  OK   " if passed else "  FAIL ") + name)
    ok = ok and passed
if not ok:
    sys.exit("presentation validation failed")

chrome = os.environ.get("CHROME") or shutil.which("google-chrome") or shutil.which("chromium")
if not chrome:
    sys.exit("Chrome not found; set CHROME=/path/to/chrome")

subprocess.run([
    chrome, "--headless=new", "--no-sandbox", "--disable-gpu",
    "--disable-dev-shm-usage", "--virtual-time-budget=12000",
    "--window-size=1600,900", "--print-to-pdf=" + PDF,
    "file://" + HTML + "?print-pdf",
], check=True, stderr=subprocess.DEVNULL)
print("WROTE", PDF, "| KB:", round(os.path.getsize(PDF) / 1024, 1))
