#!/usr/bin/env python3
"""
select_eligibility.py - Formal eligibility screen for the SLR corpus.

Purpose:
    Apply the protocol's eligibility gate to the 101 assessed records and write
    an auditable decision ledger. The gate is:
      IC1 peer-reviewed primary study
      IC2 English
      IC3 2015-2026 (seminal pre-2015 via snowballing)
      IC4 primary topic = RUL / prognostics / survival / degradation-to-failure /
          predictive maintenance of an engineered asset
      IC5 contributes to >=1 RQ (censoring; DL/uncertainty; small-data; decision)
      IC6 evidence sufficient (abstract available; full-text availability flagged)

    Records whose primary topic is fouling/performance/water-quality prediction,
    materials/membrane synthesis, process control, or that are reviews are
    excluded with an explicit reason code.

INPUT:
    - metadata/corpus_a.json            (101 assessed records)
    - papers_analysis/<NNN>_*/full_text.pdf (to flag full-text availability)
OUTPUT:
    - metadata/corpus_a.json            (adds `included` + `exclusion_reason`)
    - metadata/corpus_included.json     (79)
    - metadata/corpus_excluded.json     (22)
    - metadata/eligibility_log.csv      (101 rows, auditable)
    - metadata/selection_summary.json   (counts for PRISMA)
How to run:
        python3 select_eligibility.py
"""
import csv
import glob
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", ".."))
META = os.path.join(ROOT, "metadata")

# Curated decisions from the topic gate (IC4) + study type. Each exclusion is
# listed with a reason code so the decision can be audited paper by paper.
EXCLUSIONS = {
    15: ("EC-R", "Review artikel (bukan studi primer) tentang fouling prediction/control."),
    18: ("EC-T", "Topik: optimasi dosing koagulan (process control), bukan RUL/prognostik."),
    20: ("EC-T", "Topik: prediksi laju alir/fouling UF (performance prediction), bukan RUL."),
    21: ("EC-T", "Topik: prediksi fouling membran (MLR/ANN/SVM), bukan RUL."),
    22: ("EC-T", "Topik: prediksi kualitas air umpan, bukan RUL."),
    23: ("EC-T", "Topik: pemodelan numerik modul membran, bukan RUL."),
    25: ("EC-R", "Review aplikasi AI untuk separasi membran, bukan studi primer."),
    26: ("EC-R", "Review hybrid models/digital twin, bukan studi primer."),
    27: ("EC-T", "Topik: prediksi fouling membran, bukan RUL."),
    29: ("EC-T", "Topik: prediksi fouling oil-water (physics-informed ML), bukan RUL."),
    32: ("EC-R", "Review aplikasi AI di water treatment/desalinasi, bukan studi primer."),
    40: ("EC-D", "Konteks: pengolahan air asam tambang, di luar fokus aset RO/desalinasi."),
    52: ("EC-R", "Review ML di MBR, bukan studi primer."),
    53: ("EC-R", "Review ML/AI untuk nanofiltration, bukan studi primer."),
    59: ("EC-T", "Topik: sintesis material membran (cellulose acetate), bukan RUL."),
    60: ("EC-T", "Topik: prediksi TMP (performance), bukan RUL."),
    71: ("EC-T", "Topik: modifikasi material membran (graphene/silica), bukan RUL."),
    82: ("EC-T", "Topik: prediksi silt density index, bukan RUL."),
    84: ("EC-T", "Topik: modifikasi material membran (CA/PEG/TiO2), bukan RUL."),
    88: ("EC-T", "Topik: prediksi fouling MBR, bukan RUL."),
    93: ("EC-T", "Topik: material membran MXene, bukan RUL."),
    100: ("EC-T", "Topik: desain modul UF (pemodelan numerik), bukan RUL."),
}

CORPUS = os.path.join(META, "corpus_a.json")
rows = json.load(open(CORPUS, encoding="utf-8"))


def has_fulltext(no):
    hits = glob.glob(os.path.join(ROOT, "papers_analysis", "%03d_*" % no, "full_text.pdf"))
    return bool(hits)


included, excluded = [], []
log = []
for r in rows:
    no = r["no"]
    ft = has_fulltext(no)
    if no in EXCLUSIONS:
        code, reason = EXCLUSIONS[no]
        r["included"] = False
        r["exclusion_reason"] = "%s: %s" % (code, reason)
        excluded.append(r)
        decision, ecode = "excluded", code
    else:
        r["included"] = True
        r["exclusion_reason"] = ""
        included.append(r)
        decision, ecode = "included", ""
    log.append({
        "no": no,
        "doi": r.get("doi") or "",
        "tahun": r.get("tahun") or "",
        "pilar": r.get("pilar") or "",
        "tier": r.get("relevansi") or "",
        "included": "yes" if r["included"] else "no",
        "decision": decision,
        "exclusion_code": ecode,
        "reason": r["exclusion_reason"],
        "full_text_available": "yes" if ft else "no",
        "judul": r.get("judul") or "",
    })

json.dump(rows, open(CORPUS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(included, open(os.path.join(META, "corpus_included.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(excluded, open(os.path.join(META, "corpus_excluded.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

with open(os.path.join(META, "eligibility_log.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(log[0].keys()))
    w.writeheader()
    w.writerows(log)

from collections import Counter
tiers = Counter(r.get("relevansi") for r in included)
summary = {
    "assessed": len(rows),
    "excluded": len(excluded),
    "included": len(included),
    "exclusion_codes": dict(Counter(v[0] for v in EXCLUSIONS.values())),
    "tiers_included": dict(tiers),
    "inti_included": sum(v for k, v in tiers.items() if k.startswith("Inti")),
    "full_text_available_included": sum(1 for r in included if has_fulltext(r["no"])),
    "full_text_available_excluded": sum(1 for r in excluded if has_fulltext(r["no"])),
    "criteria": "IC1-IC6 (topic gate: RUL/prognostics only); see docs/SLR_Protocol.txt",
}
json.dump(summary, open(os.path.join(META, "selection_summary.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(json.dumps(summary, ensure_ascii=False, indent=2))
