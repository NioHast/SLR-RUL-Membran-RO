#!/usr/bin/env python3
"""
build_presentation.py - Refresh the reveal.js deck (docs/SLR_Presentasi.html).

Idempotent. It keeps the single-file, offline deck in sync with the corpus and
figures: updates stale numbers/strings, refreshes the search string, and embeds
selected figures from docs/figures/png as base64 data URIs (no CDN, no external
requests, still one self-contained HTML file).

Run:  python3 build_presentation.py
"""
import base64
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", ".."))
HTML = os.path.join(ROOT, "docs", "SLR_Presentasi.html")
FIG = os.path.join(ROOT, "docs", "figures", "png")

s = open(HTML, encoding="utf-8").read()


def data_uri(name):
    with open(os.path.join(FIG, name), "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")


def img_tag(name, style):
    return '<img class="fig" data-fig="%s" src="%s" style="%s">' % (name, data_uri(name), style)


def has(name):
    return 'data-fig="%s"' % name in s


def ensure_before(anchor, name, style):
    global s
    if has(name) or anchor not in s:
        return
    block = '<div style="text-align:center;margin:6px 0">\n      %s\n    </div>\n    ' % img_tag(name, style)
    s = s.replace(anchor, block + anchor, 1)


def ensure_replace(old, name, style):
    global s
    if has(name) or old not in s:
        return
    block = '<div style="text-align:center;margin:6px 0">\n      %s\n    </div>' % img_tag(name, style)
    s = s.replace(old, block, 1)


# 1) PRISMA slide: CSS funnel -> real PRISMA figure
funnel = '''    <div class="funnel">
      <div class="row"><div class="fill" style="--w:100%">Identifikasi, 694 record unik (24 query OpenAlex/Crossref)</div></div>
      <div class="row"><div class="fill" style="--w:70%">Disaring judul/abstrak, 485 kandidat relevan</div></div>
      <div class="row"><div class="fill o" style="--w:34%">Termasuk, 101 artikel (semua pilar A\u2013G tercakup)</div></div>
    </div>'''
if not has("fig01_prisma_flow.png") and funnel in s:
    s = s.replace(funnel, '<div style="text-align:center;margin:2px 0">\n      %s\n    </div>'
                  % img_tag("fig01_prisma_flow.png", "max-height:70vh;max-width:92%"), 1)

# 2) figures
ensure_before('    <div class="stat">', "fig06_censoring_timeline.png", "max-height:24vh;max-width:84%")
ensure_replace('    <p class="muted" style="margin-top:14px">Kombinasi keempat referensi ini membentuk kerangka metodologis yang saling melengkapi untuk pelaksanaan dan pelaporan SLR di bidang Sistem Informasi dan rekayasa perangkat lunak.</p>',
               "fig02_slr_process.png", "max-height:32vh;max-width:88%")
ensure_before('    <div class="foot" style="border-color:#2c3d52">', "fig09_tier_funnel.png", "max-height:26vh;max-width:70%")
ensure_replace('    <div class="foot" style="border-top:none"></div>',
               "fig04_method_architecture.png", "max-height:26vh;max-width:92%")

# 3) text/number fixes (idempotent)
s = s.replace("24 query OpenAlex/Crossref", "16 query OpenAlex")
s = s.replace("Proses awal memakai OpenAlex/Crossref dengan 24 query.",
              "Eksekusi memakai OpenAlex/Crossref dengan 16 query; string Scopus disiapkan untuk replikasi.")
s = s.replace("Basis data: Scopus, IEEE Xplore, ScienceDirect, ACM DL, AIS eLibrary, Web of Science; pelengkap nasional: Garuda, SINTA.",
              "Basis data (direncanakan): Scopus, IEEE Xplore, ScienceDirect, ACM DL, AIS eLibrary, WoS; nasional: Garuda, SINTA. Eksekusi korpus ini: OpenAlex/Crossref (16 query) + snowballing.")
s = s.replace('''TITLE-ABS-KEY(
 ("remaining useful life" OR RUL OR prognos*)
 AND (censored OR "survival analysis" OR Weibull)
 AND ("deep learning" OR LSTM OR Bayesian)
)''','''TITLE-ABS-KEY(
 ("remaining useful life" OR "RUL" OR prognos*
  OR "predictive maintenance" OR "PHM")
 AND (censor* OR "survival analysis"
  OR Weibull OR "time-to-event")
 AND ("deep learning" OR "neural network"
  OR LSTM OR transformer OR "Bayesian")
)
AND PUBYEAR &gt; 2014''')
s = s.replace("Domain RO/membran (D7) dan censoring (D3) termasuk dimensi paling tipis; irisan metode+domain hanya 2 artikel.",
              "Domain RO (D7, 24 artikel) dan censoring (D3, 28 artikel) terputus: irisan D3 x D7 = 0 artikel.")
s = s.replace("Dari 101 artikel: tidak satu pun memenuhi keempatnya. D3 (censoring) hanya 28 artikel (27.7%); irisan metode+domain (Inti-Metode+Domain) hanya 2 artikel.",
              "Dari 101 artikel: tidak satu pun memenuhi keempatnya. D3 (censoring) = 28 artikel, D7 (RO) = 24 artikel, dan irisan D3 x D7 = 0 artikel.")
s = s.replace("Irisan metode+domain (<b>Inti-Metode+Domain</b>) hanya <b>2 artikel</b> \u2192 gap nyata.",
              "Irisan metode+domain <b>2 artikel</b>, dan irisan censoring (D3) x domain RO (D7) = <b>0 artikel</b> \u2192 gap nyata.")
s = s.replace("<td>, </td>", "<td>-</td>")

# 4) style
if "\n  .fig{" not in s:
    s = s.replace("  table.mini th{color:var(--navy-200);}\n</style>",
                  "  table.mini th{color:var(--navy-200);}\n  .fig{background:#fff;border-radius:10px;padding:6px;box-shadow:0 6px 18px rgba(0,0,0,.35);}\n</style>")

open(HTML, "w", encoding="utf-8").write(s)

external = re.findall(r'(?:src|href)="https?://[^"]+"', s)
print("WROTE", HTML, "| KB:", round(len(s.encode()) / 1024, 1),
      "| external refs:", len(external),
      "| figures:", len(re.findall(r'data-fig="', s)),
      "| sections:", s.count("<section"))
