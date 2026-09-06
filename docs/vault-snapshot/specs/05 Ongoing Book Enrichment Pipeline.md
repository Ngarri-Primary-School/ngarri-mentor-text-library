---
title: "Feature Spec - Ongoing Book Enrichment Pipeline"
type: feature-spec
tags: [chalkcode, ngarri, feature-spec, ai-enrichment]
created: 2026-08-24
updated: 2026-08-24
status: draft
---

## Current reconciliation — 6 September 2026

Evidence must include the actual text or an adequate checked source for the specific teaching claim; a blurb alone cannot establish writing craft. Select only strong connections without quotas. Old script availability, provider and third-party source behaviour claims are historical, not current verified commitments.

Read [[ChalkCode/Ngarri Mentor Text Library/Current State and Codex Handover]] first. This dated block supersedes conflicting historical statements below; earlier wording is retained for provenance.


# Feature Spec - Ongoing Book Enrichment Pipeline

Migrated from `APP_DESIGN.md` (Enrichment Pipeline section), 2026-08-24. This is the **future in-app** pipeline that runs per-book when a leader adds one — distinct from the one-time historical migration pass in [[ChalkCode/Ngarri Mentor Text Library/specs/01 AI Enrichment Pass 1]], though the tagging rules (evidence-grounded, abstain-when-uncertain, gap-fill only) carry over.

## Problem

When a leader adds a new book, the app should automatically look up its cover, blurb, and suggest curriculum tags, without the leader having to do that research manually — while never publishing anything unreviewed.

## Non-Goals

- The one-time 253-book migration — see [[ChalkCode/Ngarri Mentor Text Library/specs/01 AI Enrichment Pass 1]] (already built, different script, different scale).
- The review UI itself — see [[ChalkCode/Ngarri Mentor Text Library/specs/04 Leader Admin Area]].
- Field-level selection rules for what counts as a valid tag — see [[ChalkCode/Ngarri Mentor Text Library/specs/02 Book Detail Page Field Model]].

## Behaviour Rules

**Trigger:** runs as a Next.js API route when a book is saved via the Add Book form (see [[ChalkCode/Ngarri Mentor Text Library/specs/04 Leader Admin Area]]). Only runs if an AI key is configured (see [[ChalkCode/Ngarri Mentor Text Library/Working Contract]] rule 16).

**Blurb sourcing procedure** — merged 2026-08-24 from the retired `BLURB_SOURCING_WORKFLOW.md`, which remains the fuller standing reference for this exact procedure applied to any future book, not only the historical 342-book migration:

1. **Google Books JSON API** (automated) — primary source, roughly 85% hit rate on the original collection. Query as `intitle:X+inauthor:Y`; author must be normalised from "Surname, First" to "First Surname" before querying; match using Jaccard token similarity on title + author (title weighted 65%, author 35%). Confirmed misses: small-press Australian titles (EK Books, Magabala, Windy Hollow, Berbay) are often absent.
2. **Readings.com.au** (manual only) — best for Australian picture books, carries the most accurate publisher blurbs. **Cannot be automated** — search results are JavaScript-rendered, confirmed by testing. Search `https://www.readings.com.au/search/results?q=[title]+[author]`, copy the publisher's own description text directly.
3. **The StoryGraph** (manual cross-check only) — blocks server-side requests (403). Browser/extension only.
4. **Goodreads** (search snippets only) — `site:goodreads.com "[Title]" "[Author]"`. If the snippet matches the primary blurb, high confidence; if it contradicts, flag for review.

**Confirmed unusable sources:** Open Library (no description fields for Australian picture books), Booktopia and Penguin AU (AI-paraphrased marketing copy, not publisher text), generic Google Search snippets, Fantastic Fiction (blocks automated fetch).

**Blurb confidence/verification logic:** clean Google Books match -> accept, mark verified; title/author mismatch flagged -> verify manually before accepting; short description (<120 chars) -> likely insufficient, check Readings.com.au for a fuller version; catalogue-language phrasing detected -> replace, not a publisher blurb; no API result -> manual Readings.com.au lookup; two sources agree -> accept, high confidence; only one source found -> accept but note the source used; sources disagree -> flag for leader review.

**Blurb quality standard:** must be the publisher's own text (not AI-paraphrased or catalogue copy), describes story/content not awards or reviews, doesn't refer to the author in third person, doesn't include "perfect for ages X-Y" or award-shortlist language. Long descriptions (including structured/bullet-point content) are kept in full, not trimmed — the app displays a truncated preview with an expand option.

**Known-error check:** before accepting any blurb, check the project folder's `Blurb Verification/Known_Errors_DO_NOT_REPEAT.csv` for previously confirmed factual errors on that book (e.g. wrong plot, wrong protagonist, wrong format) — this is a live record of mistakes not to repeat, not something to copy into this spec.

**Curriculum tagging:** uses the Claude API. Inputs: blurb, title, author, text type. First checks teacher-entered data, then OzLit, then uses AI only for genuine gaps (matches the source hierarchy in [[ChalkCode/Ngarri Mentor Text Library/Architecture]]). Outputs normalized annotation rows plus teaching ideas, never boolean book-table fields. All AI suggestions go to Needs Review — never auto-published.

**Teacher spreadsheet awareness:** the historical `Ngarri PS_ Mentor library writers traits.xlsx` is a one-time migration source, not something the ongoing pipeline re-checks per new book — new books obviously won't be in that spreadsheet.

**API key handling:** Google Books API key stored as an environment variable, never in project docs or committed files (known outstanding issue in the legacy project folder — see [[ChalkCode/Ngarri Mentor Text Library/Working Contract]] Anti-Shortcut Rules).

## Edge Cases

- A book with no ISBN and an ambiguous title/author match — blurb lookup should fail gracefully to "flagged for review", not guess at a similarly-titled different book.
- StoryGraph blocking the server-side request — must fall back to Goodreads automatically, not surface as a pipeline failure to the leader.
- A book already partially tagged by the leader on the Add Book form — AI must fill only the fields the leader left blank, never overwrite what was explicitly entered.
- No AI key configured — the pipeline should no-op cleanly, not error; the book remains fully usable with leader-entered fields only.

## Acceptance Checks

- A book added via the form with no ISBN still gets a best-effort blurb lookup or a clear "needs manual blurb" flag, never a silently blank blurb.
- No AI-suggested tag ever overwrites a leader-entered tag for the same book.
- The pipeline runs to completion (or a clean no-op) whether or not an AI key is configured — never a hard failure either way.
- Every AI-suggested output includes a confidence level and lands in "Needs Review", matching [[ChalkCode/Ngarri Mentor Text Library/specs/02 Book Detail Page Field Model]]'s status model.
