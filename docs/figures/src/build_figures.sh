#!/usr/bin/env bash
# build_figures.sh - Rebuild every figure in docs/figures/ from source.
#
# Requirements:
#   - mermaid-cli  : npm i -g @mermaid-js/mermaid-cli   (binary: mmdc)
#   - matplotlib   : pip install matplotlib
#   - Chromium/Chrome at /usr/bin/google-chrome (or edit puppyeteer.json)
#
# Usage:
#   bash build_figures.sh
#   MMDC=/path/to/mmdc bash build_figures.sh
set -euo pipefail
cd "$(dirname "$0")"

MMDC="${MMDC:-mmdc}"

for f in *.mmd; do
  base="${f%.mmd}"
  echo "[mermaid] ${base}"
  "$MMDC" -i "$f" -o "../png/${base}.png" -p puppeteer.json -b white -s 3
  "$MMDC" -i "$f" -o "../svg/${base}.svg" -p puppeteer.json -b white
done

echo "[matplotlib] charts.py"
python3 charts.py

echo "Done. Output: ../png/*.png and ../svg/*.svg"
