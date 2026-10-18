#!/usr/bin/env python3
"""
build_article_docx.py - Build a journal-style article in .docx (stage 4).

Formatting contract:
  - Times New Roman 10; all paragraphs justified except the title.
  - Foreign (English) terms italicised in the Indonesian prose.
  - Zero paragraph spacing and single line spacing everywhere; the only blank
    line is ONE empty paragraph before each heading (no blank line after it).
  - Figures: centered image + "Gambar N." caption.
  - Tables: real DOCX tables in a three-line scientific style (booktabs:
    top rule, header rule, bottom rule; no vertical/internal rules) with a
    "Tabel N." caption above.

INPUT : pipeline/4_build_deliverables/article.md
OUTPUT: docs/SLR_Artikel_Jurnal.docx
Run   : python3 build_article_docx.py
"""
import os
import re
from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", ".."))
MD = os.path.join(BASE, "article.md")
OUT = os.path.join(ROOT, "docs", "SLR_Artikel_Jurnal.docx")
FIG_DIR = os.path.join(ROOT, "docs", "figures", "png")

FONT = "Times New Roman"
BLACK = RGBColor(0, 0, 0)

doc = Document()
st = doc.styles["Normal"]
st.font.name = FONT
st.font.size = Pt(10)
st.font.color.rgb = BLACK
st.paragraph_format.line_spacing = 1.0
st.paragraph_format.space_before = Pt(0)
st.paragraph_format.space_after = Pt(0)
_rpr = st.element.get_or_add_rPr()
_rf = _rpr.get_or_add_rFonts()
_rf.set(qn("w:eastAsia"), FONT)
_rf.set(qn("w:cs"), FONT)

def add_page_number(section):
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run()
    fld1 = OxmlElement("w:fldChar")
    fld1.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    fld2 = OxmlElement("w:fldChar")
    fld2.set(qn("w:fldCharType"), "end")
    run._r.append(fld1)
    run._r.append(instr)
    run._r.append(fld2)
    run.font.name = FONT
    run.font.size = Pt(10)
    run.font.color.rgb = BLACK


sec0 = doc.sections[0]
sec0.top_margin = Inches(0.8)
sec0.bottom_margin = Inches(0.8)
sec0.left_margin = Inches(0.8)
sec0.right_margin = Inches(0.8)
add_page_number(sec0)

# English / foreign terms italicised in the Indonesian prose (longest first).
FOREIGN = [
    "remaining useful life", "remaining-useful-life", "systematic literature review",
    "decision support system", "long short-term memory", "predictive maintenance",
    "survival analysis", "concept-centric", "clean-in-place", "reverse osmosis",
    "transfer learning", "domain adaptive", "physics-informed", "knowledge-guided",
    "state-of-the-art", "health management", "health index", "data-driven",
    "right-censored", "all-censored", "small-data", "run-to-failure", "core paper",
    "deep learning", "neural network", "convolutional", "hyperparameter", "identifiability",
    "open access", "full-text", "benchmark", "baseline", "snowballing", "prognostics",
    "prognostic", "degradation", "eligibility", "screening", "included", "framework",
    "likelihood", "variational", "transformer", "attention", "explainable", "trade-off",
    "end-of-life", "maintenance", "censored", "censoring", "dataset", "pipeline",
    "abstract", "fouling", "scaling", "Weibull", "Bayesian", "hazard", "review",
    "query", "fault", "Cox",
    "RUL", "SLR", "CIP", "DSS", "CMMS", "PRISMA", "PICOC", "OpenAlex", "Crossref",
    "Scopus", "IEEE",
]
FOREIGN_RE = re.compile(
    r"(" + "|".join(re.escape(t) for t in sorted(FOREIGN, key=len, reverse=True)) + r")",
    re.IGNORECASE,
)

FIG_RE = re.compile(r"^\{\{FIG:([^|]+)\|([^|]*)\|([0-9.]+)\}\}$")
TABLE_RE = re.compile(r"^\{\{TABLE:(.+)\}\}$")

fig_no = 0
table_no = 0


def _run(p, text, size, bold=False, italic=False):
    r = p.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    r.font.color.rgb = BLACK
    r.bold = bold
    r.italic = italic
    return r


def add_runs(p, text, size=10, bold=False, italic=False, foreign=True):
    """Add text runs, italicising foreign terms when `foreign` is True."""
    if not foreign:
        _run(p, text, size, bold, italic)
        return
    pos = 0
    for m in FOREIGN_RE.finditer(text):
        if m.start() > pos:
            _run(p, text[pos:m.start()], size, bold, italic)
        _run(p, m.group(0), size, bold, True)
        pos = m.end()
    if pos < len(text):
        _run(p, text[pos:], size, bold, italic)


def para(text, size=10, align=WD_ALIGN_PARAGRAPH.JUSTIFY, bold=False,
         italic=False, foreign=True, indent=True):
    p = doc.add_paragraph()
    p.alignment = align
    pf = p.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    pf.line_spacing = 1.0
    if indent:
        pf.first_line_indent = Cm(0.75)
    add_runs(p, text, size, bold, italic, foreign)
    return p


def blank():
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    pf.line_spacing = 1.0


def heading(text, level):
    blank()  # exactly one empty paragraph before a heading
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf = p.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    pf.line_spacing = 1.0
    if level == 2:
        add_runs(p, text, 11, bold=True, italic=False)
    else:
        add_runs(p, text, 10.5, bold=True, italic=False)


def add_figure(name, caption, width_cm):
    global fig_no
    path = os.path.join(FIG_DIR, name)
    if not os.path.exists(path):
        para("[Gambar tidak ditemukan: %s]" % name)
        return
    fig_no += 1
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(path, width=Cm(min(float(width_cm), 7.9)))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_before = Pt(0)
    cap.paragraph_format.space_after = Pt(0)
    cap.paragraph_format.line_spacing = 1.0
    _run(cap, "Gambar %d. " % fig_no, 9, bold=True)
    _run(cap, caption, 9)


def _set_table_width(t, rows):
    """Fit the table to the 16.8 cm text width, proportional to content length."""
    h0 = str(rows[0][0])
    if h0.startswith("Tahap PRISMA"):
        widths = [5.4, 2.5]
    elif h0.startswith("Dimensi Konsep"):
        widths = [4.1, 2.0, 1.8]
    elif len(rows[0]) == 2:
        widths = [5.4, 2.5]
    elif len(rows[0]) == 4:
        widths = [0.8, 1.2, 5.1, 0.8]
    else:
        widths = [7.9 / len(rows[0])] * len(rows[0])
    for j, w in enumerate(widths):
        t.columns[j].width = Cm(w)
        for cell in t.columns[j].cells:
            cell.width = Cm(w)
    tblPr = t._tbl.tblPr
    tblW = OxmlElement("w:tblW")
    tblW.set(qn("w:w"), "5000")
    tblW.set(qn("w:type"), "pct")
    tblPr.append(tblW)


def _booktabs(table):
    """Three-line scientific table: top rule, header rule, bottom rule only."""
    tbl = table._tbl
    tblPr = tbl.tblPr
    for old in tblPr.findall(qn("w:tblBorders")):
        tblPr.remove(old)
    borders = OxmlElement("w:tblBorders")

    def edge(name, sz, val="single"):
        e = OxmlElement("w:%s" % name)
        e.set(qn("w:val"), val)
        e.set(qn("w:sz"), str(sz))
        e.set(qn("w:space"), "0")
        e.set(qn("w:color"), "000000")
        borders.append(e)

    edge("top", 12)
    edge("left", 0, "none")
    edge("bottom", 12)
    edge("right", 0, "none")
    edge("insideH", 0, "none")
    edge("insideV", 0, "none")
    tblPr.append(borders)

    for cell in table.rows[0].cells:
        tcPr = cell._tc.get_or_add_tcPr()
        tcB = tcPr.find(qn("w:tcBorders"))
        if tcB is None:
            tcB = OxmlElement("w:tcBorders")
            tcPr.append(tcB)
        e = OxmlElement("w:bottom")
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "8")
        e.set(qn("w:space"), "0")
        e.set(qn("w:color"), "000000")
        tcB.append(e)


def add_table(rows, caption):
    global table_no
    if not rows:
        return
    table_no += 1
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_before = Pt(0)
    cap.paragraph_format.space_after = Pt(0)
    cap.paragraph_format.line_spacing = 1.0
    cap.paragraph_format.keep_with_next = True
    _run(cap, "Tabel %d. " % table_no, 9, bold=True)
    _run(cap, caption, 9)

    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = True
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = t.cell(i, j)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            _run(p, str(val), 7.2, bold=(i == 0))
    _set_table_width(t, rows)
    _booktabs(t)
    for row in t.rows:
        trPr = row._tr.get_or_add_trPr()
        trPr.append(OxmlElement("w:cantSplit"))
    hdr = t.rows[0]._tr.get_or_add_trPr()
    hdr.append(OxmlElement("w:tblHeader"))


def render_body(md):
    lines = md.split("\n")
    i = 0
    pending_caption = ""
    in_refs = False
    while i < len(lines):
        ln = lines[i].rstrip()
        m = TABLE_RE.match(ln.strip())
        if m:
            pending_caption = m.group(1).strip()
            i += 1
            continue
        if ln.startswith("| ") and ln.endswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not re.match(r"^[-: ]+$", "".join(cells)):
                    block.append(cells)
                i += 1
            add_table(block, pending_caption)
            pending_caption = ""
            continue
        m = FIG_RE.match(ln.strip())
        if m:
            add_figure(m.group(1), m.group(2), m.group(3))
            i += 1
            continue
        if ln.startswith("### "):
            heading(ln[4:], 3)
        elif ln.startswith("## "):
            if ln[3:].strip().lower().startswith("daftar pustaka"):
                in_refs = True
            heading(ln[3:], 2)
        elif ln.startswith("# "):
            blank()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            _run(p, ln[2:], 14, bold=True)
        elif ln.startswith("- "):
            p = doc.add_paragraph(style="List Bullet")
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            add_runs(p, ln[2:], 10)
        elif ln.strip() == "":
            pass
        else:
            para(ln, 10, foreign=not in_refs)
        i += 1


def set_columns(section, n=2):
    sectPr = section._sectPr
    cols = sectPr.find(qn("w:cols"))
    if cols is None:
        cols = OxmlElement("w:cols")
        sectPr.append(cols)
    cols.set(qn("w:num"), str(n))
    cols.set(qn("w:space"), "360")


frontmatter = ""
body = ""
if os.path.exists(MD):
    raw = open(MD, encoding="utf-8").read()
    if "<!--BODY-->" in raw:
        frontmatter, body = raw.split("<!--BODY-->", 1)
    else:
        frontmatter, body = raw, ""

    for ln in frontmatter.split("\n"):
        s = ln.strip()
        if not s:
            continue
        if s.startswith("# "):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            _run(p, s[2:], 14, bold=True)          # title: not italicised
        elif s.startswith("## "):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            _run(p, s[3:], 11, italic=True)
        elif s.startswith("**") and s.endswith("**") and len(s) > 4:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            _run(p, s.strip("*"), 10)
        else:
            m = re.match(r"^\*\*(Abstrak\.|Abstract\.|Kata kunci:|Keywords:)\*\*\s*(.*)$", s)
            if m:
                label, rest = m.group(1), m.group(2)
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.0
                is_english = label.startswith(("Abstract", "Keywords"))
                _run(p, label + " ", 10, bold=True, italic=is_english)
                # English abstract/keywords: fully italic, no per-word italics
                add_runs(p, rest, 10, italic=is_english, foreign=not is_english)
            else:
                para(s, 10)

    newsec = doc.add_section(WD_SECTION.CONTINUOUS)
    newsec.top_margin = sec0.top_margin
    newsec.bottom_margin = sec0.bottom_margin
    newsec.left_margin = sec0.left_margin
    newsec.right_margin = sec0.right_margin
    set_columns(newsec, 2)
    render_body(body)

doc.save(OUT)
print("WROTE", OUT, "| paragraphs:", len(doc.paragraphs), "| tables:", len(doc.tables),
      "| figures:", fig_no, "| table captions:", table_no)
