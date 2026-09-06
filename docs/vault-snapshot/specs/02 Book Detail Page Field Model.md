---
title: "Feature Spec - Book Detail Page Field Model"
type: feature-spec
tags: [chalkcode, ngarri, feature-spec, data-model]
created: 2026-08-24
updated: 2026-08-24
status: draft
---

## Current reconciliation — 6 September 2026

Numeric connection counts are guidance, not minimums or caps. Every connection needs a located book example and exact curriculum reference. Draft inquiry questions may be reviewed without a separate official list. Counterexample discussions must not be imported as positive value-embodiment tags. The linked handover records these superseding distinctions.

Read [[ChalkCode/Ngarri Mentor Text Library/Current State and Codex Handover]] first. This dated block supersedes conflicting historical statements below; earlier wording is retained for provenance.


# Feature Spec - Book Detail Page Field Model

Migrated from the project folder's `BOOK_DETAIL_FIELDS.md`, 2026-08-24 — the field-by-field data and selection-rule model for every section of the book detail page. This is a data-model spec, read before either the Pilot App (Project Map Section 10) or AI Enrichment Pass 2 (Section 12) is built.

## Problem

Every book detail page field needs a precise definition of what data it holds and, for AI-generated fields, an explicit rule for when tagging that field is actually justified — so enrichment doesn't produce vague, over-broad, or unjustified tags.

## Non-Goals

- Search/filter UI and result-card fields — see [[ChalkCode/Ngarri Mentor Text Library/specs/03 Teacher Search and Results]].
- The mechanics of running enrichment (API calls, source order, confidence logic) — see [[ChalkCode/Ngarri Mentor Text Library/specs/05 Ongoing Book Enrichment Pipeline]].
- The one-time AI Enrichment Pass 1 script itself — see [[ChalkCode/Ngarri Mentor Text Library/specs/01 AI Enrichment Pass 1]].

## Behaviour Rules

Every field carries a status: `blank` (insufficient knowledge, awaiting human input) | `imported_teacher` | `imported_ozlit` | `ai_suggested` (needs review) | `teacher_reviewed` | `teacher_added` | `teacher_added` (override). Nothing blocks publishing because a field is blank — the app should surface blank fields clearly so teachers/leaders know where input is needed. AI-generated annotations also carry a confidence level (High/Medium/Low).

**A. Book metadata** (one record per book, in `books`): cover_image, title, author, illustrator, publisher, year_published, text_type, genre, year_level_min/max (Foundation stored as 0), is_australian, blurb (verbatim from a verified source, never AI-generated), ozlit_calibrated flag.

**B. "Why use this book?" panel** — 3-5 bullets, each a short sentence (<=15 words) explaining one pedagogical reason to use the book. Can be left blank; teachers can add bullets directly.

**C. Writing traits** — tag 1-3 of the 7 traits, one "In this book" note per applicable year level. Selection rule: tag only traits where this book is *noticeably stronger* than a simpler alternative — where a student couldn't learn the skill as well from a less complex text. If no specific craft technique can be identified, don't tag it. For OzLit-listed books, OzLit's trait assignment is the primary source; AI confirms and supplements rather than deciding independently (see [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]], 2026-07-30 OzLit entry). KU/KS text must be verbatim from the Writing Throughlines PDF — AI's only role on a trait card is the "In this book" callout.

**D. Reading strategies** — tag 1-3 strategies, one "In this book" note per applicable year level. Selection rule: tag only strategies the text actively *demands* — where meaning would be lost or significantly reduced without applying it. Most picture books support all strategies to some degree; tag only where the text makes the strategy unavoidable. OzLit-listed books use OzLit's assignment as primary source.

**E. PRIDE values** — tag 1-2 values, one "In this book" note each. Selection rule: before tagging, a specific character decision, story event, or moment embodying the value must be identifiable. If the connection can only be made by generalising ("this story is broadly about resilience"), don't tag it — leave blank for teacher input. No OzLit calibration exists for this section at all.

**F. Inquiry lenses** — tag 1-2 lenses, one "In this book" note each. Selection rule: must connect the book to one of the lens's specific Big Questions (from reference data). If no specific Big Question and how it's addressed can be articulated, don't tag it. No OzLit calibration exists for this section.

**G. Teaching ideas** — 2-5 ideas per book, can be left blank or partial. If knowledge of the book's specific craft is insufficient, generic strategy-level ideas may be generated but must be flagged `is_generic: true`. Fields: title, description, time_minutes, grouping (Individual/Pairs/Small group/Whole class), difficulty (Entry/Medium/Discussion/Extension), colour_tag (links visually to the trait/strategy it supports).

**H. Resources (sidebar)** — attached PDFs/docs/links, added manually by teachers/leaders, not AI-generated. Type: PDF/DOC/VIDEO/LINK.

**I. Related books (sidebar)** — cross-links grouped by relationship type (same reading strategy, same author, similar themes), generated once enough books exist in the database — not available until the collection has real coverage.

## Edge Cases

- A book with a thin blurb and no other identifiable evidence — most sections should end up sparse or blank, not padded with generic content.
- A book with OzLit coverage for traits/strategies but genuinely no clear PRIDE/inquiry-lens connection — leave those two sections blank; OzLit coverage in one category says nothing about another.
- A teaching idea that's genuinely just a strategy-level idea, not specific to this book's actual scenes — must be flagged `is_generic`, never presented as book-specific when it isn't.
- A trait/strategy year-level assignment that doesn't fit the throughlines' actual progression for that skill (e.g. complex figurative language tagged at F-2, when the throughlines show it isn't introduced until Year 3) — this is a mismatch that should be caught, not silently accepted.

## Acceptance Checks

- Every populated field has a status and, where AI-generated, a confidence level.
- No writing-trait or reading-strategy card displays KU/KS text that has been paraphrased rather than copied verbatim from the source PDF.
- No PRIDE value or inquiry lens is tagged without an identifiable specific in-book moment or Big Question connection.
- Generic teaching ideas are visibly distinguishable from book-specific ones.
- Source/provenance fields (`source_type`, `confidence`, `status`, `reviewed_by`, `reviewed_at`) exist on every annotation row but are never rendered as teacher-facing labels.
