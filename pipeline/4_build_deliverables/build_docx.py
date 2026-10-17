#!/usr/bin/env python3
"""
build_docx.py - Convert the Markdown report into docs/SLR_Laporan.docx (stage 4).

Purpose:
    Read report_filled.md (fallback: report.md) and produce a Word document in
    thesis-report style: Times New Roman 12, bold only for the main title,
    margins 4-4-3-3 cm, 1.5 line spacing, no space before/after, all text black,
    justified (except centered titles), tables without color fill.

    Figure markers of the form {{FIG:file.png|caption|width_cm}} are rendered as
    centered images (from docs/figures/png/) with an automatic "Gambar N." caption.

INPUT:
    - report_filled.md (if present; output of fill_report.py).
    - report.md        (fallback).
OUTPUT:
    - docs/SLR_Laporan.docx
How to run:
        python3 build_docx.py
"""
import os
import re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", ".."))
MD = os.path.join(BASE, "report_filled.md")
if not os.path.exists(MD):
    MD = os.path.join(BASE, "report.md")
OUT = os.path.join(ROOT, "docs", "SLR_Laporan.docx")
FIG_DIR = os.path.join(ROOT, "docs", "figures", "png")

BLACK = RGBColor(0, 0, 0)
FONT = "Times New Roman"

doc = Document()
normal = doc.styles["Normal"]
normal.font.name = FONT
normal.font.size = Pt(12)
normal.font.color.rgb = BLACK
pf = normal.paragraph_format
pf.line_spacing = 1.5
pf.space_before = Pt(0)
pf.space_after = Pt(0)
rpr = normal.element.get_or_add_rPr()
rfonts = rpr.get_or_add_rFonts()
rfonts.set(qn("w:eastAsia"), FONT)
rfonts.set(qn("w:cs"), FONT)

sec = doc.sections[0]
sec.top_margin = Cm(4)
sec.left_margin = Cm(4)
sec.right_margin = Cm(3)
sec.bottom_margin = Cm(3)


def strip_md(t):
    return re.sub(r"\*\*|__|\*|`", "", t)


def add_para(text, center=False, bold=False, size=12):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(strip_md(text))
    r.font.name = FONT
    r.font.size = Pt(size)
    r.font.color.rgb = BLACK
    r.bold = bold
    return p


def add_bullet(text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(strip_md(text))
    r.font.name = FONT
    r.font.size = Pt(12)
    r.font.color.rgb = BLACK


def add_table(rows):
    if not rows:
        return
    t = doc.add_table(rows=1, cols=len(rows[0]))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, h in enumerate(rows[0]):
        cell = t.rows[0].cells[j]
        p = cell.paragraphs[0]
        r = p.add_run(strip_md(str(h)))
        r.font.name = FONT
        r.font.size = Pt(11)
        r.font.color.rgb = BLACK
    for row in rows[1:]:
        cells = t.add_row().cells
        for j, v in enumerate(row):
            p = cells[j].paragraphs[0]
            r = p.add_run(strip_md(str(v)))
            r.font.name = FONT
            r.font.size = Pt(11)
            r.font.color.rgb = BLACK
    doc.add_paragraph()


FIG_RE = re.compile(r"^\{\{FIG:([^|]+)\|([^|]*)\|([0-9.]+)\}\}$")
fig_no = 0


def add_figure(name, caption, width_cm):
    global fig_no
    path = os.path.join(FIG_DIR, name)
    if not os.path.exists(path):
        add_para("[Gambar tidak ditemukan: %s]" % name)
        return
    fig_no += 1
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.add_run().add_picture(path, width=Cm(float(width_cm)))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_after = Pt(8)
    cr = cap.add_run("Gambar %d. %s" % (fig_no, caption))
    cr.font.name = FONT
    cr.font.size = Pt(10)
    cr.font.color.rgb = BLACK
    cr.italic = True


md = open(MD, encoding="utf-8").read()
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
        add_table(block)
        continue
    m = FIG_RE.match(ln.strip())
    if m:
        add_figure(m.group(1), m.group(2), m.group(3))
        i += 1
        continue
    if ln.startswith("# "):
        add_para(ln[2:], center=True, bold=True)
    elif ln.startswith("### "):
        add_para(ln[4:], center=False, bold=True)
    elif ln.startswith("## "):
        add_para(ln[3:], center=False, bold=True)
    elif ln.startswith("- "):
        add_bullet(ln[2:])
    elif ln.strip() == "":
        pass
    elif ln.strip() == "---":
        doc.add_page_break()
    else:
        add_para(ln, center=False, bold=False)
    i += 1

doc.save(OUT)
print("WROTE", OUT, "| paragraphs:", len(doc.paragraphs), "| tables:", len(doc.tables),
      "| figures:", fig_no)
