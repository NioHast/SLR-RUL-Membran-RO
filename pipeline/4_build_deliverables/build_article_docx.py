#!/usr/bin/env python3
"""
build_article_docx.py - Build a 2-column journal article in .docx format (stage 4).

Purpose:
    Read article.md (with a "<!--BODY-->" separator) then produce a Word document
    in journal-article style: the front matter (title/authors/abstract/keywords)
    is rendered in 1 column, while the body is rendered in 2 columns.

INPUT:
    - BASE/article.md (BASE = "/tmp/opencode/slr").
OUTPUT:
    - /home/nioha/Downloads/SLR_Artikel_Jurnal.docx
How to run:
        python3 build_article_docx.py
NOTE:
    BASE="/tmp/opencode/slr" and OUT="/home/nioha/Downloads/SLR_Artikel_Jurnal.docx"
    are ABSOLUTE paths; you MUST change them to your own working location before running.
"""

# Build a 2-column journal-style article docx from a markdown file.
import os, re
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# --- Input/output paths ---
BASE="/tmp/opencode/slr"
MD=os.path.join(BASE,"article.md")
OUT="/home/nioha/Downloads/SLR_Artikel_Jurnal.docx"

# --- Document & default styles ---
doc=Document()
st=doc.styles["Normal"]; st.font.name="Times New Roman"; st.font.size=Pt(10)
# Page margins ±2 cm.
sec0=doc.sections[0]
sec0.top_margin=Inches(0.8); sec0.bottom_margin=Inches(0.8)
sec0.left_margin=Inches(0.8); sec0.right_margin=Inches(0.8)

def add_table_from_rows(rows, fs=8):
    """Add a table (bold header, font `fs`) from a list of rows."""
    if not rows: return
    t=doc.add_table(rows=1, cols=len(rows[0])); t.style="Light Grid Accent 1"
    for j,h in enumerate(rows[0]):
        c=t.rows[0].cells[j]; c.text=str(h)
        for p in c.paragraphs:
            for r in p.runs: r.bold=True; r.font.size=Pt(fs)
    for row in rows[1:]:
        cells=t.add_row().cells
        for j,v in enumerate(row):
            cells[j].text=str(v)
            for p in cells[j].paragraphs:
                for r in p.runs: r.font.size=Pt(fs)

def set_columns(section, n=2):
    """Set the number of columns on `section` via the w:cols XML element."""
    sectPr=section._sectPr
    cols=sectPr.find(qn('w:cols'))
    if cols is None:
        cols=OxmlElement('w:cols'); sectPr.append(cols)
    cols.set(qn('w:num'), str(n))
    cols.set(qn('w:space'), "360")

def render_body(md):
    """Render the Markdown body into the document (called inside the 2-column section)."""
    lines=md.split("\n"); i=0
    while i < len(lines):
        ln=lines[i].rstrip()
        # Markdown table block.
        if ln.startswith("| ") and ln.endswith("|"):
            block=[]
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells=[c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not re.match(r"^[-: ]+$", "".join(cells)): block.append(cells)
                i+=1
            add_table_from_rows(block); continue
        # Heading & paragraph.
        if ln.startswith("## "):
            p=doc.add_paragraph(); r=p.add_run(ln[3:]); r.bold=True; r.font.size=Pt(11)
        elif ln.startswith("# "):
            p=doc.add_paragraph(); r=p.add_run(ln[2:]); r.bold=True; r.font.size=Pt(12)
        elif ln.strip()=="":
            pass
        else:
            doc.add_paragraph(ln)
        i+=1

# --- Read article.md: split front matter and body at the <!--BODY--> marker ---
frontmatter=""; body=""
if os.path.exists(MD):
    raw=open(MD,encoding="utf-8").read()
    if "<!--BODY-->" in raw:
        frontmatter, body = raw.split("<!--BODY-->",1)
    else:
        frontmatter, body = raw, ""
    # Front matter (title/authors/abstract/keywords) is rendered full width (1 column)
    for ln in frontmatter.split("\n"):
        s=ln.strip()
        if not s: continue
        if s.startswith("# "):
            p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
            r=p.add_run(s[2:]); r.bold=True; r.font.size=Pt(16)
        elif s.startswith("## "):
            p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
            r=p.add_run(s[3:]); r.italic=True; r.font.size=Pt(11)
        elif s.startswith("**") and s.endswith("**"):
            p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
            r=p.add_run(s.strip("*")); r.font.size=Pt(11)
        else:
            doc.add_paragraph(s)
    # New section (continuous), 2 columns, for the body.
    newsec=doc.add_section(WD_SECTION.CONTINUOUS)
    newsec.top_margin=sec0.top_margin; newsec.bottom_margin=sec0.bottom_margin
    newsec.left_margin=sec0.left_margin; newsec.right_margin=sec0.right_margin
    set_columns(newsec, 2)
    render_body(body)
else:
    doc.add_heading("Article (isi belum tersedia)",1)

# --- Save ---
doc.save(OUT)
print("WROTE",OUT,"paragraphs:",len(doc.paragraphs),"tables:",len(doc.tables))
