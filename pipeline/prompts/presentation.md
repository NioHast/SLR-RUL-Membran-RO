# Prompt: presentation deck (reveal.js)

> Replaces the former `pipeline/4_build_deliverables/presentation_brief.md`. Visual styling
> lives in `pipeline/prompts/deliverable_style.md` (do not duplicate it here).

| Field | Value |
|---|---|
| **Purpose** | Build the SLR presentation (reveal.js) that communicates the whole study academically |
| **Model** | LLM subagent (OpenCode) |
| **Version / Date** | v1 - 2026-10-12 |
| **Params** | not recorded (see `docs/AI_USAGE.md`) |
| **Input** | the filled report and the corpus workbook (`SLR_Korpus.xlsx`) |
| **Output** | one self-contained HTML file `SLR_Presentasi.html` (+ PDF) |
| **Human check** | author review |

## Content rules
- Bahasa Indonesia; technical terms may stay English. **No em dash (`—`).**
- Dense but not rambling: <= 6 points per slide. Use **real corpus numbers** (read them, never hardcode).
- Add short **speaker notes** per slide (`<aside class="notes">`).

## Slide structure (required)
1. **Judul**: SLR title, student name, NIM, Study Program (Information Systems), year.
2. **Agenda**: list of sections.
3. **Latar belakang & urgensi**: why this SLR is needed (3 points).
4. **Tujuan & Research Questions**: RQ1-RQ4.
5. **Metode (ringkas)**: Kitchenham + PRISMA 2020 + Webster & Watson + Wohlin snowballing.
6. **Strategi pencarian**: databases + example search string + PICOC (brief).
7. **Alur PRISMA**: numbers for identification -> screening -> eligibility -> included (from report/dataset).
8. **Hasil: sebaran pilar A-G**: bar chart + short explanation.
9. **Hasil: matriks konsep D1-D8**: bar of article counts per dimension.
10. **Sintesis per dimensi**: main findings (D1-D8, brief).
11. **Research Gap**: state the main gap (quote from "Sintesis & Gap Final").
12. **Kontribusi & implikasi**: what the thesis offers.
13. **Kesimpulan**: 3-4 points.
14. **Referensi kunci**: 5-8 key references (short DOI).
15. **Penutup**: thanks / Q&A + contact.

## Output
- One self-contained HTML file using reveal.js from CDN; openable offline (CDN allowed, no build step).
- For visual style (theme, palette, 16:9, fonts, progress bar, speaker-note format) follow `deliverable_style.md`.
