---
title: Ngarri Mentor Text Library - Working Contract
type: ai-working-contract
tags: [chalkcode, ai-contract, ngarri, education, curriculum]
created: 2026-08-24
updated: 2026-08-24
status: active
---

## Current reconciliation — 6 September 2026

Apply the current user decisions in the linked handover: preserve sources and human annotations; select strong located examples without quotas; keep draft content out of teacher views; maintain source-version distinctions. Historical script/test availability and provider assumptions below are not proof of current availability or new spending approval.

Read [[ChalkCode/Ngarri Mentor Text Library/Current State and Codex Handover]] first. This dated block supersedes conflicting historical statements below; earlier wording is retained for provenance.


# Ngarri Mentor Text Library - Working Contract

These are the non-negotiable rules for AI-assisted work on the Ngarri Mentor Text Library app. This mirrors `AI_CONTRACT.md` in the project folder — see [[ChalkCode/Ngarri Mentor Text Library/index]] for the relationship between the two.

## Required Reading

Before substantial work, read:

1. [[ChalkCode/Ngarri Mentor Text Library/Project Map]]
2. [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]]
3. [[ChalkCode/Ngarri Mentor Text Library/Research Notes]]
4. [[ChalkCode/Ngarri Mentor Text Library/Architecture]]
5. The relevant feature spec in [[ChalkCode/Ngarri Mentor Text Library/specs]]
6. For any visual, UI or interaction work, [[ChalkCode/Ngarri Mentor Text Library/Design/00 Design Index]]

## Note on This Folder's Authority

As of 2026-08-24, this ChalkCode folder holds **all** instruction documents, rules, and contracts for the project — the project folder (`/Users/phillcantone/Library/Mobile Documents/com~apple~CloudDocs/Family/Phill/AI Coding/Mentor Texts/`) holds only data and code. That project folder keeps a minimal `CLAUDE.md` stub pointing back here for auto-load purposes; it carries no rules content of its own. See [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]], 2026-08-24 entry, for the full rationale.

## Core Rules

1. Do not code or import data until the relevant feature spec exists and has acceptance checks.
2. Keep curriculum vocabulary — the 7 writing traits, 11 reading strategies, 5 PRIDE values and 4 inquiry lenses — as canonical data in the Supabase reference tables. Never redefine, rename, or duplicate the list in application code, scripts, or AI prompts.
3. Keep source-provenance logic (the `teacher_spreadsheet` > `ozlit` > `ai_suggested` hierarchy) in its own domain/service, not scattered through UI code or one-off import scripts.
4. Keep the book domain (title, author, blurb, cover, lifecycle status) separate from the annotation domain (trait/strategy/value/lens tags with provenance). Books own stable metadata; annotations own tagged content. Don't merge the two.
5. Do not hardcode a one-off fix for a single book (e.g. special-casing one title or row) outside the canonical matching data and slug maps.
6. Store every curriculum mapping (e.g. OzLit's `voice` -> `voice_audience`, teacher spreadsheet's "Spelling" -> `conventions`) as an explicit, documented map with a date and reason — never a silent inline rename.
7. Every AI-suggested tag must be explainable: store and be able to show the exact evidence quote and source that produced it, not just the tag.
8. Ngarri's KU/KS curriculum text, `we_will` lines, and `selection_indicators` are fixed reference content — store and display them verbatim, never paraphrased or "improved."
9. Use Australian curriculum terms, spellings, and year-level codes (F, 1-6) throughout; don't substitute US/UK equivalents.
10. Apply canonical slug maps before comparing or merging annotations across sources, so the same trait is never stored under two different names.
11. OzLit-derived rows must carry `source_type='ozlit'` and a traceable `source_name`; teacher-derived rows must carry `source_type='teacher_spreadsheet'`. Provenance is never inferred after the fact.
12. Do not assume a fuzzy title/author match (teacher spreadsheet or OzLit) is the right book. "Technically matches" and "actually the same book/edition" are different questions — every fuzzy match requires human confirmation before its data is used, never auto-applied.
13. Treat the 20-book AI-enrichment spot-check as a hard go/no-go gate: bulk enrichment of the remaining ~233 gap books must not run until Phill has reviewed the sample for evidence quality and zero hallucinated tags.
14. "Good enough" for that gate means the quantitative bar in [[ChalkCode/Ngarri Mentor Text Library/specs/01 AI Enrichment Pass 1]] — zero unproven tags, correct abstention when a book can't be identified, and every slug validated against canon. Don't leave "good enough" undefined.
15. In-app AI enrichment (once the app exists) must run on a school-owned Anthropic API key with a spending cap, never Phill's personal key. A personal key is acceptable only for the one-time bulk migration and should be revoked afterwards.
16. The add-book/admin form must work fully with no AI key configured at all — manual curriculum tagging by a leading teacher is a first-class path, not a fallback. The "run AI research" action only appears when a key is present.
17. OzLit's calibration file (169 books) and the teacher spreadsheet are treated as complete for the books they cover. Do not re-run AI enrichment over a book that already has a human-confirmed teacher or OzLit match for that annotation type.
18. For a book with an OzLit-confirmed match, AI's role is to explain and connect the existing OzLit tag (in Ngarri-friendly language, linked to Ngarri KU/KS text) and write "In this book" notes and teaching ideas — never to independently re-derive or second-guess the tag itself. This is a different AI behaviour from gap-filling on books with no source data at all.
19. The teacher spreadsheet's `Texts` sheet (381 rows) is the trait-tag source; its `Wishlist` sheet (4 rows) must never be treated as current library books or matched against the school collection.
20. Update [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]] when a trade-off or non-obvious rule is chosen.
21. Update [[ChalkCode/Ngarri Mentor Text Library/Project Map]] when architecture or domain ownership changes.
22. Some visual design decisions exist (typography, colour-role conventions, screen composition — see `Design/01 Visual Direction` and `Design/04 Screen Specs`), but no formal design tokens, component library, or finalised colour palette exist yet. Implement only what's documented; pause and ask rather than inventing the undocumented parts (exact colours, spacing scale, motion) for the pilot app build.

## System-Level Change Gate

Every proposed fix must address the reusable class of problem, not only the currently reported book, source, or example.

Before implementation, the AI must state:

- the general rule or category of problem being addressed
- at least three examples the rule should handle
- at least one counterexample the rule should reject or flag
- the data model, policy, or domain service where the rule belongs

A change is incomplete if it only adds a book-specific, row-specific, or source-specific conditional. Tests must cover the rule category, not just one book.

During review, ask: "Would this still work if the next book were a completely different title, from a different source, with a different data gap?"

## Anti-Shortcut Rules

Do not solve future bugs by:

- adding book-specific conditionals in import, matching, or enrichment scripts
- fixing one bad AI-suggested tag without fixing the general evidence/slug validator that let it through
- adding a special case where a data-driven slug map or source-hierarchy rule is required
- special-casing one source's (OzLit vs. teacher spreadsheet) format inside shared annotation logic that the other source also flows through
- treating every AI-suggested tag as acceptable without the evidence-and-slug validator rejecting it first
- assuming every book fits the same shape (every book has a blurb, a single clear year range, an unambiguous match) without checking
- claiming a tag is "verified" or "reviewed" when its status is still `ai_suggested`
- storing API keys, secrets, or credentials in source files, docs, screenshots, or committed output (known outstanding issue: `google_books_api_key.txt` in the project folder, pending fix)
- using OzLit's or the AI's raw suggestion as final without the source-hierarchy and evidence checks running first
- using the Anthropic API in the production app on a personal key, or beyond a spending cap appropriate for the school's actual usage

## Completion Gates

Before a feature or data-import step is considered ready:

- relevant domain rules are represented as data (slug maps, source hierarchy, provenance fields), not inline conditionals
- tests cover the general validation rule, not just one book (see the enrichment script's offline test harness as the pattern)
- every AI-suggested row carries `source_type`, `status`, `confidence`, and evidence
- teacher-facing content shows approved tags only, never raw provenance labels
- docs and decisions are updated ([[ChalkCode/Ngarri Mentor Text Library/Project Map]], [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]])
- relevant Design files are updated once a formal design system exists and visual appearance changes
- no API keys or secrets are present in committed files
