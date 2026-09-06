---
title: Ngarri Mentor Text Library - Research Notes
type: research-notes
tags: [chalkcode, ngarri, research-notes, education, curriculum]
created: 2026-08-24
updated: 2026-08-24
status: active
---

## Current reconciliation — 6 September 2026

The supplied four-page Fox text has now been read in full; it contains no illustrations. Prototype content was checked rather than accepted as fact. The user rejected the current Making Connections draft and requested removal of teacher-facing PDF page numbers. These revisions remain outstanding.

Read [[ChalkCode/Ngarri Mentor Text Library/Current State and Codex Handover]] first. This dated block supersedes conflicting historical statements below; earlier wording is retained for provenance.


# Ngarri Mentor Text Library - Research Notes

Source-backed research that this project's rules, slug canon, or enrichment approach rely on. Only load-bearing findings go here — background reading that didn't change a decision doesn't need an entry.

## Ngarri's curriculum framework — the definitive source

Question: The project's own docs disagreed on the actual PRIDE values, inquiry lenses, and reading-strategy lists across `APP_DESIGN.md`, `BOOK_DETAIL_FIELDS.md`, and an earlier `PROJECT_OVERVIEW.md` draft (e.g. PRIDE's fifth value was written as both "Excellence" and, wrongly, "Empathy"). Which list is correct?

Source(s): `Shared Resources/Curriculum - ENGLISH. working copy.pdf` in the project folder — Ngarri's own working curriculum document.

Finding: Confirmed with Phill (2026-07-21): inquiry lenses are Social Responsibility, Environmental Sustainability, The Physical World, Identity/Creativity/Wellbeing (the `APP_DESIGN.md` version was correct). PRIDE's fifth value is Excellence, not Empathy. The reading-strategy list was extracted from the working-copy PDF as the 11-strategy canonical set (see [[ChalkCode/Ngarri Mentor Text Library/Working Contract]] rule 2).

Used in: [[ChalkCode/Ngarri Mentor Text Library/Working Contract]] rule 2 / project-folder `AI_CONTRACT.md` §2 slug canon / all four reference tables in Supabase.

## OzLit calibration file — scope and reliability

Question: How much can OzLit's data be trusted as a source, and what does it actually cover?

Source(s): `reference-data/oz-lit-calibration.json` — 169 books, described as "expert-tagged Australian mentor texts," with writing-trait, reading-strategy, and year-level tags per book.

Finding: OzLit covers 169 books total; fuzzy-matched by title/author against the school's 352-book master list, then every match was human-reviewed and confirmed before use (`match_ozlit.py` -> `ozlit_match_review.csv`). OzLit's own trait slug for Audience/Voice is `voice`, not the app's `voice_audience` — an explicit slug map prevents a silent duplicate. OzLit provides no data at all for PRIDE values, inquiry lenses, or teaching ideas — those need AI enrichment or manual entry for every book, not just the gap books.

Used in: [[ChalkCode/Ngarri Mentor Text Library/Working Contract]] rules 6, 11, 12 / [[ChalkCode/Ngarri Mentor Text Library/Project Map]] Source Hierarchy / Matching domain / project-folder `DECISIONS.md`.

## Fox mockup review — what informed the current book-detail-page structure

Question: An external prototype (Fox, `fox-deploy-olive.vercel.app`) was reviewed for its book-detail-page design. What was worth keeping, and what needed to change before it became the actual design direction?

Source(s): Direct review of the live Fox prototype against real usage scenarios, 2026-06.

Finding: Strong points worth keeping — cover presence, easy-to-find blurb, a "Why use this book?" panel. Problems found: too much evidence hidden behind collapsed accordions (teachers need quick confidence, not a treasure hunt); book-detail-first rather than purpose-first (a teacher arriving from a "Word Choice" search should immediately see why *this* book serves that purpose); the sidebar competed visually with the main teaching evidence; the mobile layout broke at 390px width; weak semantic HTML (generic divs instead of real headings/buttons, hurting accessibility); the nested year-level accordion was more detail than teachers usually need up front (they ask "is this good for Word Choice?" more than "show me Year 3 specifically"); "Save to My Library" was flagged as not core launch scope.

Used in: [[ChalkCode/Ngarri Mentor Text Library/Design/04 Screen Specs]] — the recommended revised structure (hero -> Teaching Purposes -> Curriculum Detail -> Teaching Ideas -> Resources -> Related Books) directly resolves these findings.

## Text-type to year-level alignment (Audience/Voice throughline)

Question: How should the app validate or suggest a year level based on a book's text type (narrative, information, persuasive)?

Source(s): Ngarri's Writing Throughlines document, Audience/Voice page — a "Must do / Can do" table per year level.

Finding: Foundation and Year 1-2 focus on Retell/Narrative and Information texts; persuasive text types (persuasive texts/letters) are introduced from Year 1 onward; Explanation and Procedural text types are introduced progressively from Year 3-4; News article appears from Year 5. This gives the AI enrichment pipeline a cross-check: if a book's text type doesn't fit its assigned year range per this table, that's a flagged mismatch, not an automatic error (the table is guidance, not a hard constraint).

Used in: [[ChalkCode/Ngarri Mentor Text Library/specs/02 Book Detail Page Field Model]] (year-level validation logic) / future AI enrichment pass 2 prompt design.

## Anthropic web-search grounding for anti-hallucination tagging

Question: Can an AI reliably tag a book's writing traits and reading strategies without hallucinating, especially for less well-known titles the model may not have reliable prior knowledge of?

Source(s): Claude API server-side `web_search` tool (max 6 searches per book in `enrich_traits.py`); the model is required to cite a quoted evidence snippet and its source for every tag, and must return `identified: false` with a stated reason when it can't confirm the specific book.

Finding: Grounding alone doesn't guarantee no hallucination — the pipeline also runs a separate validator that rejects any tag with an unknown slug, invalid confidence value, or missing evidence text before it ever reaches the database (24 offline test cases cover this). The remaining open question is whether the *quality* of grounded tagging is good enough in practice, which is exactly what the 20-book spot-check gate is designed to answer — see [[ChalkCode/Ngarri Mentor Text Library/specs/01 AI Enrichment Pass 1]].

Used in: [[ChalkCode/Ngarri Mentor Text Library/Working Contract]] rules 7, 13, 14 / [[ChalkCode/Ngarri Mentor Text Library/Project Map]] Section 1 (AI Enrichment Feasibility Gate) / specs/01 AI Enrichment Pass 1.
