---
title: Ngarri Mentor Text Library - Decisions Log
type: decisions-log
tags: [chalkcode, decisions-log, ngarri, education, curriculum]
created: 2026-08-24
updated: 2026-08-24
status: active
---

## Current reconciliation — 6 September 2026

New user decisions and recovery findings are recorded in the linked handover. Earlier claims that the Mac project log is the sole current authority, and reports of available 20-book output, are historical; do not use them to bypass the present evidence and review gates.

Read [[ChalkCode/Ngarri Mentor Text Library/Current State and Codex Handover]] first. This dated block supersedes conflicting historical statements below; earlier wording is retained for provenance.


# Ngarri Mentor Text Library - Decisions Log

Record important product, data and architecture decisions here so future AI sessions apply the same logic instead of re-deciding or accidentally contradicting something already settled.

**The project folder's `DECISIONS.md`** (`/Users/phillcantone/Library/Mobile Documents/com~apple~CloudDocs/Family/Phill/AI Coding/Mentor Texts/DECISIONS.md`) is the full, authoritative decisions log. This file is the Obsidian-side summary for the ChalkCode template pattern — condensed, newest first. Keep it in sync, but treat the project-folder file as the source of truth for anything cited by its `AI_CONTRACT.md`.

## 2026-08-24 - Separate one-time migration from ongoing curation, but extract shared foundations

Decision: Treat Part 1 as a one-time, script-driven migration/database-creation pipeline for the existing School Library collection, and Part 2 as a small-batch, teacher-friendly curation app for learning specialists adding 1-10 new books at a time. The two parts should share normalisation, slug validation, source hierarchy, evidence validation, blurb quality rules, review-item shape, and app-ready query/view logic, but they should not share the same operational interface or assumptions.

Rationale: The existing collection needs batch tooling, audit reports, SQL generation, and careful migration gates; future book additions need a calm passcode-gated workflow that works without AI and never publishes AI suggestions without review. Keeping the modes separate prevents the future app from becoming a bulk migration console, while extracting shared foundations prevents one-time scripts from becoming the only place core domain rules live. See [[ChalkCode/Ngarri Mentor Text Library/Project Map]] Part 1 / Part 2 Boundary and Shared Foundations.

## 2026-08-25 - 20-book spot-check run with no API key at all

Decision: Rather than wait for an Anthropic key, Claude did the spot-check itself using its own `WebSearch`/`WebFetch` tools (available in this chat session, unrelated to the API), following the exact rules already written into the script's system prompt, and piping the results through the script's own validator/CSV functions rather than hand-writing them.

Rationale: The spot-check's purpose is validating the *prompt and rules*, which don't require the specific API path to test — only a human review of the CSV does. Zero validation warnings across 20 books (39 writing-trait tags, 10 reading-strategy tags, 1 correctly-empty book, 0 abstentions) confirms the rules are sound. This does not replace eventually needing a key for the unattended 233-book bulk run, or for testing the actual script's API-call path (retries, resumability) at least once — see [[ChalkCode/Ngarri Mentor Text Library/specs/01 AI Enrichment Pass 1]] for full detail and the "Spot-Check Run" section.

## 2026-08-25 - AI provider question opened: school's ChatGPT Pro vs. Anthropic API

Decision: Not yet decided — logged as an open question, not a change. The school has purchased ChatGPT Pro, which does not itself include OpenAI API access (separate product/billing). If API access is confirmed, the enrichment pipeline could in principle run on OpenAI's models instead of Anthropic's, since the validation/evidence/slug/abstention rules are provider-agnostic and only the API-call layer would change. "Codex" is a coding assistant, not the integration point for an unattended per-book pipeline — the actual target would be OpenAI's model API directly.

Rationale: Worth investigating since it may remove the "no personal API key" tension entirely if the school already has usable API billing — but shouldn't block today's spot-check (done without any API, via Claude's own web search in this session) or get decided casually. See [[ChalkCode/Ngarri Mentor Text Library/Project Map]] Hard Questions.

## 2026-08-24 - Give the offline test suite a permanent home; fix a test that couldn't have caught its own bug

Decision: Move `enrich_traits.py`'s offline test suite out of ephemeral scratchpad files into a permanent project-folder file, `School Library/Migration/test_enrich_traits.py`, with an explicit regression assertion for the correct `source_type='ai_suggested'` value.

Rationale: The suite previously only ever existed in scratchpad locations that don't persist across sessions — when the 2026-08-03 `source_type` bug was fixed, the attempt to update and rerun the scratchpad test file failed silently, so the fix was verified only ad hoc, not by the persisted suite. Worse, the original test's assertion for that field checked for the *presence* of the buggy value, so it was written to match the bug rather than catch it — it could never have failed even before the fix. Verified 2026-08-24: all 24 checks (including the new regression assertion) pass against the current code. See [[ChalkCode/Ngarri Mentor Text Library/specs/01 AI Enrichment Pass 1]] for detail.

## 2026-08-24 - Migrate the 4 remaining context docs; merge rather than duplicate

Decision: `SCHOOL_LIBRARY_CONTEXT.md` and `BLURB_VERIFICATION_CONTEXT.md` are retired without becoming standalone Obsidian files — both were stale mid-project (2026-06-24/25) status snapshots duplicating later, more current content, and one repeated an error already corrected in this log (the wrong "#68-70 duplicates #65-67" claim). Their few non-redundant facts were merged into `Architecture.md`. `BLURB_SOURCING_WORKFLOW.md`'s procedural content (source priority, scoring method, quality standards) was merged into `specs/05 Ongoing Book Enrichment Pipeline.md` since it's a standing procedure the ongoing pipeline reuses, not historical migration detail. `PERSONAL_COLLECTION_CONTEXT.md` was moved to its own top-level ChalkCode folder (`Personal Collection`), not nested inside this one, because its own content explicitly states it's a different project not to be merged with the school library.

Rationale: the goal was "all instructions in Obsidian," not "one file per source file" — merging where content was genuinely redundant, and respecting the Personal Collection's own stated project boundary, keeps the vault from re-accumulating the same doc-sprawl problem this whole migration exists to fix.

## 2026-08-24 - Obsidian folder holds all instructions; project folder holds only data and code

Decision: Move every instructional/rules/roadmap document (the governance docs written 2026-08-03, plus the pre-existing `README.md`, `APP_DESIGN.md`, `BOOK_DETAIL_FIELDS.md`, `PROJECT_OVERVIEW.md`, `AI_PROJECT_HANDOFF_NEXT_STEPS.md`, `APP_READINESS_CHECKLIST.md`) into this ChalkCode folder, fully replacing them there. The project folder keeps only data, scripts, schema, and a minimal `CLAUDE.md` stub that points here for auto-load purposes.

Rationale: Phill wants one clean separation — Obsidian for instructions, the project folder for data and code — rather than two governance systems that could silently drift apart, which is exactly the failure mode these docs exist to prevent. Content was read in full and faithfully migrated (not summarised or dropped) to `Architecture.md`, `Project Map.md`, `Decisions Log.md`, `Research Notes.md`, `Design/`, and `specs/` in this folder.

## 2026-08-24 - No personal API keys in school infrastructure; AI enrichment is optional in the app

Decision: The production app's per-book AI research must run on a school-owned Anthropic API account with a spending cap, never Phill's personal key. The admin add-book form must work fully with no key configured at all — manual tagging is a first-class path, and the AI research action only appears when a key is present. The one-time bulk migration may use a disposable personal key since nothing later depends on it.

Rationale: A personal key on school infrastructure puts charges on Phill's card and breaks the app if he ever leaves and revokes it. Manual tagging as a first-class fallback also means the app never depends on AI to function at all.

## 2026-08-24 - Use persistent AI working-control docs in both the project folder and the ChalkCode vault

Decision: Create `AI_CONTRACT.md`/`ARCHITECTURE.md`/`DECISIONS.md`/`PROJECT_MAP.md`/`specs/` in the project folder (2026-08-03), then mirror them into this ChalkCode folder using the standard template (2026-08-24).

Rationale: The binding rules (source hierarchy, canonical slugs, provenance model, no-hallucination requirement) were scattered across prose docs and chat history with nothing an AI session loads automatically. The Codex anti-rot workflow calls for persistent rules before code; this project already had the code and data built, so the docs were retrofitted rather than written first — worth doing anyway before Phase 2's app build starts.

## 2026-07-30 - OzLit is authoritative for matched books; AI explains rather than re-tags

Decision: For any book with a human-confirmed OzLit match, AI's job is to explain the existing OzLit tag in Ngarri-friendly language, connect it to Ngarri KU/KS reference data, and generate "In this book" notes and teaching ideas — never to independently second-guess or re-derive the tag.

Rationale: Ngarri already uses OzLit and treats it as reliable for writing traits, year level, and reading strategies. Letting AI re-judge already-confirmed data would create unnecessary conflict and rework for no accuracy gain.

## 2026-07-27 - Duplicate resolution: 9 confirmed duplicates removed, 11 series pairs kept separate

Decision: Of 21 candidate duplicate pairs found by `find_duplicates.py`, remove 9 genuine duplicates (see Project Map Section 3 for the full pair list), keep 11 Little People Big Dreams series pairs as separate books, and reject 1 false positive (Diary of a Worm vs Diary of a Wombat).

Rationale: Fuzzy title/author matching surfaces same-series and same-author false positives alongside genuine duplicates; each candidate needs human judgement, not automatic merging. This step also corrected an earlier misread (rows #61-63 don't need retitling, they're plain duplicates; #67 was never a Fantastic Mr Fox duplicate).

## 2026-07-30 - Enrichment pass 1 scope: traits/strategies first, not everything at once

Decision: The first AI enrichment pass covers only writing traits and reading strategies for the 253 gap books. PRIDE values, inquiry lenses, teaching ideas and why-use bullets are deferred to a second pass.

Rationale: Writing traits and reading strategies power the core search; focused prompt-tuning on the highest-value fields first, accepting the grounding cost is paid twice across two passes.

## 2026-07-30 - Enrichment grounding: verified blurb + live web search; hybrid spot-check gate

Decision: Every AI-generated tag must be grounded in the verified blurb plus live web search (publisher/review pages), with a quoted evidence snippet and source. A ~20-book human-reviewed sample must be approved before any bulk run; all AI output imports as `ai_suggested`.

Rationale: Model memory alone is unreliable for obscure titles; this is a hard no-hallucination requirement. The spot-check catches prompt-quality problems before they multiply across 233 books.

## 2026-07-30 - Supabase project: free tier, ap-southeast-2 (Sydney)

Decision: Use a free-tier Supabase project in the Sydney region.

Rationale: $0 cost for a single-school app; Sydney is the closest available region to the school.

## 2026-07-30 - RLS model: public read-only; all writes via service_role server-side

Decision: Every table has row-level security enabled with public `SELECT` only. No `INSERT`/`UPDATE`/`DELETE` grants for the anon or authenticated roles; all writes go through the service role, server-side only.

Rationale: Implements "no teacher login, single admin passcode" at the database layer, not just the UI — the public anon key is safe to ship in the app frontend.

## 2026-07-30 - Slug canon: `voice_audience` is the trait slug

Decision: OzLit's `voice` and the throughlines JSON's `audience_voice` both map to the canonical `voice_audience` slug, via an explicit, documented map.

Rationale: Three sources spelled the same writing trait three different ways; silently merging them without a rename would have created phantom duplicate traits in the annotation tables.

## 2026-07-27 - No login for teachers at all; app is public; admin keeps one shared passcode

Decision: Drop teacher login entirely. The teacher-facing app is public with no authentication. The leader/admin area uses a single shared passcode, not per-user accounts or OAuth.

Rationale: Removes the Google Workspace OAuth-approval risk and login friction entirely; the book data isn't sensitive, only the write path needs protecting, and RLS plus a passcode-gated server route covers that.

## 2026-07-22 - Simplifications: no monorepo, no Edge Functions, no embeddings, no book_copies table

Decision: Build one Next.js app with a `lib/` folder, not a monorepo. Run enrichment as local scripts / API routes, not Supabase Edge Functions. Use the structured `reference-data/*.json` lookups instead of an embeddings pipeline. Defer a `book_copies`/multi-copy tracking table.

Rationale: A planning review found these were premature abstractions for a solo-maintained, single-school app at this scale.

## 2026-06 (predates the direction freeze) - Pivot from manual spreadsheet work to building the app first

Decision: Stop manually completing spreadsheet annotations for the existing collection; build the web app first, and let it automate blurb sourcing and AI curriculum tagging instead.

Rationale: The same annotation work would need to be redone through the app anyway once it existed — manual spreadsheet completion was unsustainable and duplicative. This is the originating decision behind the whole two-phase (data setup, then app) structure.

## 2026-06-25 - No `ozlit_books` reference table; OzLit matches flow directly into annotation rows

Decision: Do not build a separate `ozlit_books` table to hold matched OzLit records, despite early design docs proposing one. OzLit-sourced data is written directly into the annotation tables during canonical import, with `source_type='ozlit'` provenance.

Rationale: Once `build_canonical_preview.py` existed to combine confirmed matches directly into annotation rows, a separate intermediate table added no value — the confirmed-match CSV (`ozlit_match_review.csv`) already serves as the audit trail.
