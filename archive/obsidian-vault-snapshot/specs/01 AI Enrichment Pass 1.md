---
title: "Feature Spec - AI Enrichment Pass 1"
type: feature-spec
tags: [chalkcode, ngarri, feature-spec, ai-enrichment]
created: 2026-08-24
updated: 2026-08-24
status: in-progress
---

## Current reconciliation — 6 September 2026

Original script, regression suite and 20-book output claims below are historical and unrecovered. Do not treat them as an available or approved benchmark. Preserve imported annotations; prepare/recover the benchmark and obtain review before any collection-wide run.

Read [[ChalkCode/Ngarri Mentor Text Library/Current State and Codex Handover]] first. This dated block supersedes conflicting historical statements below; earlier wording is retained for provenance.


# Feature Spec - AI Enrichment Pass 1

Writing traits and reading strategies for the 253 books that have neither teacher-spreadsheet nor OzLit data. Mirrors `specs/2026-07-30-ai-enrichment-pass-1.md` in the project folder, in ChalkCode template form.

## Problem

253 of the library's 343 books have zero writing-trait or reading-strategy tags, so they're effectively invisible to the app's core purpose-first search. These gaps need filling without introducing a single hallucinated tag.

## Non-Goals

- PRIDE values, inquiry lenses, teaching ideas, and why-use bullets — deferred to a second AI enrichment pass covering all 343 books, not just the 253 gap books.
- Re-tagging or reviewing any of the 90 books that already have teacher-spreadsheet or OzLit data — this pass only fills gaps.
- Building the in-app admin review queue — that's owned by the future Leader/Admin Area (Project Map Section 7). This spec covers the one-time migration script only.

## Behaviour Rules

- Only the 253 books flagged `needs_ai_enrichment` in the canonical import are eligible.
- Every tag must carry a real quoted evidence snippet and its source (the verified blurb, or a web-search result).
- The model must set `identified: false` and abstain from tagging entirely if it cannot confirm the specific book (title + author + illustrator match, not a same-titled different book).
- Only the canonical slugs (7 writing traits, 11 reading strategies) may be emitted; anything else is rejected before import, not silently dropped after.
- Year levels are only recorded when there's actual evidence for them — never inferred "from vibes."
- Confidence (`high`/`medium`/`low`) must reflect the actual strength of the evidence found, not default to `high`.
- A 20-book random sample must be generated, reviewed by Phill, and explicitly approved before any of the remaining ~233 books are processed.
- The final SQL import is generated from the saved raw response log, not by re-calling the API — what Phill approved in the CSV is exactly what gets imported.

## Edge Cases

- A book the model can partially identify but isn't confident about (e.g. a common title with multiple editions) — must abstain, not guess.
- A book with a thin or generic blurb that gives no real evidence for any trait — should return few or zero tags, not padded-out generic ones.
- The bulk run crashing partway through — must resume from the last completed book, not restart or duplicate work, and must not silently lose the books already processed.
- A book that legitimately fits many traits — all genuinely evidenced tags should be kept, not artificially capped.
- The model returning a plausible-sounding but non-canonical slug (e.g. "imagination" instead of "ideas") — must be rejected by the validator, not passed through.

## Acceptance Checks

- The spot-check CSV exists and is reviewed and explicitly approved by Phill before any bulk API call is made.
- Zero imported rows reference any of the 90 books that already had teacher-spreadsheet or OzLit data.
- Every imported row has a valid canonical slug, `source_type` and `status` both set to `ai_suggested`, and non-empty evidence text.
- Books the model abstained on remain untagged in the database and are counted and reported, so they can be queued for manual tagging later.
- The offline validation test suite (`School Library/Migration/test_enrich_traits.py`, 24 checks covering slug rejection, abstention, evidence requirements, SQL quoting, and crash-resume logic) passes. **Verified 2026-08-24: all 24 checks pass against the current code.**
- Post-import row counts match the number of statements the sqlgen step produced — nothing silently lost or duplicated.

## Test Suite History (a caught process gap, not just a fact)

The offline test suite existed only as an ephemeral scratchpad file in an earlier session — never committed anywhere durable. When the `source_type='ai'` bug (see [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]]) was fixed on 2026-08-03, the attempt to update and rerun that scratchpad file silently failed (the path no longer existed in the new session), so the fix was only confirmed by an ad hoc inline check at the time — **not** by the persisted suite. Worse: the original suite's assertion for this field checked for the *presence* of the buggy `'ai'` literal, so even if it had been rerun unmodified, it would not have caught the bug — it was written to match the bug, not to reject it.

Fixed 2026-08-24: the suite now lives permanently at `School Library/Migration/test_enrich_traits.py` (real code, real project folder — not Obsidian), with an explicit regression assertion for the correct `'ai_suggested'` value and an explicit assertion that the buggy `'ai',` literal is absent. Run it before any bulk enrichment run, and after any future edit to `enrich_traits.py`.

## Spot-Check Run: Completed Without Any API Key (2026-08-25)

Rather than wait on an Anthropic key, Claude (this session) did the 20-book spot-check itself:

1. Selected the identical 20-book sample the script would pick (`random.seed(42)`, same `load_books_needing_enrichment()` call) — the same set Phill would have reviewed either way.
2. Researched each book via its own `WebSearch`/`WebFetch` tools (a different capability from the Anthropic API — no key required), following the exact rules from the script's `SYSTEM_PROMPT`: evidence required for every tag, only canonical slugs, confidence must reflect real evidence strength, abstain rather than guess.
3. Ran every result through the script's own `validate_result()` and `flatten_for_csv()` functions — not hand-written output — so the review CSV is provably built by the same validator the real pipeline uses. **Zero validation warnings.**
4. Wrote the real output files: `ai_trait_spot_check.csv` and `ai_trait_spot_check_raw.jsonl` in `School Library/Migration/` — identical format to what `--mode sample` produces.

**Result:** 39 writing-trait tags + 10 reading-strategy tags across 20 books (avg 2.45 tags/book). 1 book ("From my Head to my Toes, I Say What Goes" — a consent/values book) correctly returned zero writing-trait/reading-strategy tags since no craft-specific evidence was found — expected behaviour per rule 6, not a failure. 0 books abstained as unidentifiable.

**Now awaiting Phill's review of `ai_trait_spot_check.csv`** — same human gate the spec always required. Once approved, the remaining ~233 books need either the same manual approach repeated (slow, no key) or a real API key for `--mode bulk` (fast, ~$10-20) — see the AI-provider question (Anthropic vs. the school's OpenAI access) in [[ChalkCode/Ngarri Mentor Text Library/Project Map]] Hard Questions. See [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]] for the full decision record.
