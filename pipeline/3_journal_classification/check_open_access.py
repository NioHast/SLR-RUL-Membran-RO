#!/usr/bin/env python3
"""
check_open_access.py
--------------------
Check the OPEN ACCESS status + LICENSE of each corpus article via the Unpaywall
API, to determine which articles are SAFE & LEGAL to include with their full text.

Criteria for "safe to include": oa_status OA AND has a Creative Commons license (cc-*).
- gold/hybrid/green + cc-* license  -> may be included (with attribution).
- bronze / no license                -> NOT included (free to read, but no redistribution permission).
- other-oa                          -> NOT included (unclear license).
- closed                            -> NOT included.

INPUT:
    - ../../metadata/corpus_a.json (fallback: ../../source_code/data/corpus_a.json).
OUTPUT:
    - open_access_status.json (OA status + license per DOI, in the same folder).
How to run:
        python3 check_open_access.py   (requires internet)
NOTE:
    The corpus path is computed relative to the location of this file; adjust it
    if your folder structure differs. Other scripts in the pipeline use absolute
    paths (e.g. BASE="/tmp/opencode/slr") which you MUST change to your own working
    location.
"""

import json, urllib.request, urllib.parse, time, os

EMAIL = "mnioh@students.undip.ac.id"
HERE = os.path.dirname(os.path.abspath(__file__))
# Look for corpus_a.json in metadata/, then fall back to source_code/data/.
CORPUS = os.path.join(HERE, "..", "..", "metadata", "corpus_a.json")
if not os.path.exists(CORPUS):
    CORPUS = os.path.join(HERE, "..", "..", "source_code", "data", "corpus_a.json")
OUT = os.path.join(HERE, "open_access_status.json")

def fetch(doi, tries=2):
    """Call Unpaywall for one DOI; retry `tries` times on failure."""
    url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={EMAIL}"
    for _ in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "slr-oa-check"})
            return json.load(urllib.request.urlopen(req, timeout=30))
        except Exception:
            time.sleep(1)
    return {}

def analyze(doi):
    """Determine whether the article is OA + Creative Commons licensed (safe to include)."""
    d = fetch(doi)
    locs = [l for l in ([d.get("best_oa_location")] + (d.get("oa_locations") or [])) if l]
    licenses = sorted({l.get("license") for l in locs if l.get("license")})
    is_cc = any(str(x).lower().startswith("cc-") for x in licenses)
    status = d.get("oa_status")
    include = bool(d.get("is_oa")) and is_cc
    return {
        "doi": doi,
        "is_oa": d.get("is_oa"),
        "oa_status": status,
        "licenses": licenses,
        "include_fulltext": include,
        "reason": "OA + lisensi Creative Commons" if include else
                  ("OA tanpa lisensi jelas (bronze/other-oa)" if d.get("is_oa") else "closed"),
    }

def main():
    corpus = json.load(open(CORPUS, encoding="utf-8"))
    out = {}
    for r in corpus:
        doi = r.get("doi")
        if not doi:
            continue
        info = analyze(doi)
        info["no"] = r.get("no")
        info["judul"] = r.get("judul")
        out[doi] = info
        time.sleep(0.15)  # polite delay so as not to overload the API
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    inc = sum(1 for v in out.values() if v["include_fulltext"])
    print(f"total {len(out)} | boleh disertakan (OA+CC): {inc} | tidak: {len(out)-inc}")
    print("Output:", OUT)

if __name__ == "__main__":
    main()
