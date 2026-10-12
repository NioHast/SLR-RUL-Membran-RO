#!/usr/bin/env python3
"""
build_docx.py - Convert the Markdown report into SLR_Laporan.docx (stage 4).

Purpose:
    Read report_filled.md (fallback: report.md) and produce a Word document in
    thesis-report style: Times New Roman 12, bold only for the main title,
    margins 4-4-3-3 cm, 1.5 line spacing, no space before/after, all text black,
    justified (except centered titles), tables without color fill.

INPUT:
    - report_filled.md (if present; output of fill_report.py).
    - report.md        (fallback when report_filled.md has not been created).
OUTPUT:
    - /home/nioha/Downloads/SLR_Laporan.docx
How to run:
        python3 build_docx.py
NOTE:
    The script looks for the Markdown file relative to the location of this file,
    but OUT ("/home/nioha/Downloads/SLR_Laporan.docx") is an ABSOLUTE path; you
    MUST change it to your own working location. Other scripts in the pipeline use
    an absolute BASE (e.g. "/tmp/opencode/slr") which must also be adjusted.
"""

# Build SLR_Laporan.docx: Times New Roman 12, bold only for the main title, margins 4-4-3-3 cm,
# 1.5 line spacing, no space before/after, all black, justified (except centered titles), tables without fill.
import os, re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# --- Input/output paths ---
BASE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(BASE, "report_filled.md")
if not os.path.exists(MD):
    MD = os.path.join(BASE, "report.md")
OUT = "/home/nioha/Downloads/SLR_Laporan.docx"

BLACK = RGBColor(0, 0, 0)
FONT = "Times New Roman"

# --- Set the document's default style (Normal) ---
doc = Document()
normal = doc.styles["Normal"]
normal.font.name = FONT
normal.font.size = Pt(12)
normal.font.color.rgb = BLACK
pf = normal.paragraph_format
pf.line_spacing = 1.5
pf.space_before = Pt(0)
pf.space_after = Pt(0)
# Set the font for Asian/CS characters so it is consistent.
rpr = normal.element.get_or_add_rPr()
rfonts = rpr.get_or_add_rFonts()
rfonts.set(qn("w:eastAsia"), FONT)
rfonts.set(qn("w:cs"), FONT)

# --- Page margins 4-4-3-3 cm ---
sec = doc.sections[0]
sec.top_margin = Cm(4)
sec.left_margin = Cm(4)
sec.right_margin = Cm(3)
sec.bottom_margin = Cm(3)

def strip_md(t):
    """Strip Markdown markers (bold/italic/inline code)."""
    return re.sub(r"\*\*|__|\*|`", "", t)

def add_para(text, center=False, bold=False, size=12):
    """Add one paragraph (optional center/bold) + an empty paragraph after it."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(strip_md(text))
    r.font.name = FONT
    r.font.size = Pt(size)
    r.font.color.rgb = BLACK
    r.bold = bold
    doc.add_paragraph()
    return p

def add_table(rows):
    """Add a 'Table Grid' style table from a list of rows (row 0 = header)."""
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

# --- Read Markdown & render line by line ---
md = open(MD, encoding="utf-8").read()
lines = md.split("\n")
i = 0
while i < len(lines):
    ln = lines[i].rstrip()
    # Detect a Markdown table block: collect lines starting with "|".
    if ln.startswith("| ") and ln.endswith("|"):
        block = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            # Drop separator rows (--- / :--:) that contain no data.
            if not re.match(r"^[-: ]+$", "".join(cells)):
                block.append(cells)
            i += 1
        add_table(block)
        continue
    # Heading & regular paragraph.
    if ln.startswith("# "):
        add_para(ln[2:], center=True, bold=True)
    elif ln.startswith("### "):
        add_para(ln[4:], center=False, bold=False)
    elif ln.startswith("## "):
        add_para(ln[3:], center=False, bold=False)
    elif ln.strip() == "":
        pass
    elif ln.strip() == "---":
        doc.add_page_break()
    else:
        add_para(ln, center=False, bold=False)
    i += 1

# --- Save ---
doc.save(OUT)
print("WROTE", OUT, "paragraphs:", len(doc.paragraphs), "tables:", len(doc.tables))
