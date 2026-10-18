#!/usr/bin/env python3
"""
build_article_docx.py - Build a 2-column journal article in .docx format (stage 4).

Purpose:
    Read article.md (with a "<!--BODY-->" separator) and produce a Word document
    in journal-article style: the front matter (title/authors/abstract/keywords)
    is rendered in 1 column, while the body is rendered in 2 columns.
    Figure markers {{FIG:file.png|caption|width_cm}} are rendered as centered
    images with an automatic "Gambar N." caption.

INPUT:
    - pipeline/4_build_deliverables/article.md
OUTPUT:
    - docs/SLR_Artikel_Jurnal.docx
How to run:
        python3 build_article_docx.py
"""
import os
import re
from docx import Document
from docx.shared import Pt, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", ".."))
MD = os.path.join(BASE, "article.md")
OUT = os.path.join(ROOT, "docs", "SLR_Artikel_Jurnal.docx")
FIG_DIR = os.path.join(ROOT, "docs", "figures", "png")

doc = Document()
st = doc.styles["Normal"]
st.font.name = "Times New Roman"
st.font.size = Pt(10)
sec0 = doc.sections[0]
sec0.top_margin = Inches(0.8)
sec0.bottom_margin = Inches(0.8)
sec0.left_margin = Inches(0.8)
sec0.right_margin = Inches(0.8)

fig_no = 0
FIG_RE = re.compile(r"^\{\{FIG:([^|]+)\|([^|]*)\|([0-9.]+)\}\}$")


def strip_md(t):
    return re.sub(r"\*\*|__|\*|`", "", t)


def _copy_margins(sec):
    sec.top_margin = sec0.top_margin
    sec.bottom_margin = sec0.bottom_margin
    sec.left_margin = sec0.left_margin
    sec.right_margin = sec0.right_margin


def _switch(ncols):
    sec = doc.add_section(WD_SECTION.CONTINUOUS)
    _copy_margins(sec)
    set_columns(sec, ncols)
    return sec


def add_table_from_rows(rows, fs=7.5):
    if not rows:
        return
    _switch(1)
    t = doc.add_table(rows=1, cols=len(rows[0]))
    t.style = "Light Grid Accent 1"
    for j, h in enumerate(rows[0]):
        c = t.rows[0].cells[j]
        c.text = str(h)
        for p in c.paragraphs:
            for r in p.runs:
                r.bold = True
                r.font.size = Pt(fs)
    for row in rows[1:]:
        cells = t.add_row().cells
        for j, v in enumerate(row):
            cells[j].text = str(v)
            for p in cells[j].paragraphs:
                for r in p.runs:
                    r.font.size = Pt(fs)
    _switch(2)


def set_columns(section, n=2):
    sectPr = section._sectPr
    cols = sectPr.find(qn("w:cols"))
    if cols is None:
        cols = OxmlElement("w:cols")
        sectPr.append(cols)
    cols.set(qn("w:num"), str(n))
    cols.set(qn("w:space"), "360")


def add_figure(name, caption, width_cm):
    global fig_no
    path = os.path.join(FIG_DIR, name)
    if not os.path.exists(path):
        doc.add_paragraph("[Gambar tidak ditemukan: %s]" % name)
        return
    fig_no += 1
    _switch(1)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(path, width=Cm(float(width_cm)))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cr = cap.add_run("Gambar %d. %s" % (fig_no, caption))
    cr.font.size = Pt(8)
    cr.italic = True
    _switch(2)


def render_body(md):
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if ln.startswith("| ") and ln.endswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not re.match(r"^[-: ]+$", "".join(cells)):
                    block.append(cells)
                i += 1
            add_table_from_rows(block)
            continue
        m = FIG_RE.match(ln.strip())
        if m:
            add_figure(m.group(1), m.group(2), m.group(3))
            i += 1
            continue
        if ln.startswith("- "):
            p = doc.add_paragraph(style="List Bullet")
            p.add_run(strip_md(ln[2:]))
        elif ln.startswith("### "):
            p = doc.add_paragraph()
            r = p.add_run(strip_md(ln[4:]))
            r.bold = True
            r.italic = True
            r.font.size = Pt(10.5)
        elif ln.startswith("## "):
            p = doc.add_paragraph()
            r = p.add_run(strip_md(ln[3:]))
            r.bold = True
            r.font.size = Pt(11)
        elif ln.startswith("# "):
            p = doc.add_paragraph()
            r = p.add_run(strip_md(ln[2:]))
            r.bold = True
            r.font.size = Pt(12)
        elif ln.strip() == "":
            pass
        else:
            doc.add_paragraph(strip_md(ln))
        i += 1


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
            r = p.add_run(s[2:])
            r.bold = True
            r.font.size = Pt(16)
        elif s.startswith("## "):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(s[3:])
            r.italic = True
            r.font.size = Pt(11)
        elif s.startswith("**") and s.endswith("**"):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(s.strip("*"))
            r.font.size = Pt(11)
        else:
            m = re.match(r"^\*\*(Abstrak\.|Abstract\.|Kata kunci:|Keywords:)\*\*\s*(.*)$", s)
            if m:
                p = doc.add_paragraph()
                r1 = p.add_run(m.group(1) + " ")
                r1.bold = True
                p.add_run(m.group(2))
            else:
                doc.add_paragraph(re.sub(r"\*\*|__|\*|`", "", s))
    newsec = doc.add_section(WD_SECTION.CONTINUOUS)
    newsec.top_margin = sec0.top_margin
    newsec.bottom_margin = sec0.bottom_margin
    newsec.left_margin = sec0.left_margin
    newsec.right_margin = sec0.right_margin
    set_columns(newsec, 2)
    render_body(body)
else:
    doc.add_heading("Article (isi belum tersedia)", 1)

doc.save(OUT)
print("WROTE", OUT, "| paragraphs:", len(doc.paragraphs), "| tables:", len(doc.tables),
      "| figures:", fig_no)
