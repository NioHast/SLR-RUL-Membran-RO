"""
verify_refs.py - Verify reference DOIs via Crossref (stage 5).

Purpose:
    For each reference title (the `refs` list embedded in the script), find the
    top match in Crossref and then display the year, journal, title, and DOI of
    the search result. Used to make sure the supporting references actually exist
    and that their DOIs are correct.

INPUT:
    - Reads no file (the reference title list is embedded in the script).
    - Network source: https://api.crossref.org/works
OUTPUT:
    - Prints to stdout only (writes no file).
How to run:
        python3 verify_refs.py
NOTE:
    This script does not use file paths at all, so there is no absolute path to
    change. Other scripts in the pipeline use absolute paths
    (e.g. BASE="/tmp/opencode/slr") which you MUST change to your own working location.
"""

import urllib.request, urllib.parse, json, time

def q(title):
    """Search for `title` in Crossref; return a list of tuples (title, doi, journal, year)."""
    u="https://api.crossref.org/works?rows=2&select=title,DOI,container-title,issued,author&query.bibliographic="+urllib.parse.quote(title)
    req=urllib.request.Request(u,headers={"User-Agent":"refcheck/1.0 (mailto:student@example.org)"})
    try:
        d=json.load(urllib.request.urlopen(req,timeout=40))
    except Exception as e:
        return [("ERR",str(e),"","")]   # return the error so it still shows in the output
    out=[]
    for it in d["message"]["items"]:
        t=(it.get("title") or ["?"])[0]
        doi=it.get("DOI","")
        cont=(it.get("container-title") or [""])[0]
        yr=(it.get("issued",{}).get("date-parts",[[None]])[0][0])
        # Truncate the text length so it looks tidy in the terminal.
        out.append((t[:80],doi,cont[:45],yr))
    return out

# --- List of reference titles to verify ---
refs=[
 "Censored lifetime learning Optimal Bayesian age-replacement policies",
 "Identifiability of cure models Li Taylor Sy",
 "LSTM and Transformers based methods for Remaining Useful Life Prediction considering Censored Data",
 "AI-based remaining useful life prediction of seawater desalination membranes",
 "Prediction of Membrane Failure in a Water Purification Plant Using Nonhomogeneous Poisson Process Models",
 "Recycling end-of-life brackish water reverse osmosis membranes Oxidative conservation characterisation",
]

# --- Run the search for each reference ---
for r in refs:
    print("QUERY:",r)
    for t,doi,cont,yr in q(r): print(f"   -> {yr} | {cont} | {t} | DOI:{doi}")
    print()
    time.sleep(0.5)  # polite delay so as not to overload the API
