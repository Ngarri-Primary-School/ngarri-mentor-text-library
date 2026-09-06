---
title: Ngarri Mentor Text Library - Project Map
type: project-map
tags: [chalkcode, ai-project, ngarri, education, curriculum, project-map]
created: 2026-08-24
updated: 2026-08-24
status: active
---

## Current reconciliation — 6 September 2026

Use the current handover for actual recovery status, outstanding teacher feedback and next action. Existing plan structure is retained; checked historical tasks do not establish that their files were recovered. There is no three-connection cap and no compulsory full-framework coverage.

Read [[ChalkCode/Ngarri Mentor Text Library/Current State and Codex Handover]] first. This dated block supersedes conflicting historical statements below; earlier wording is retained for provenance.


# Ngarri Mentor Text Library - Project Map

This map explains what the app does, where rules belong, and how the system should be built in sections. It is the single authoritative build plan and status log, superseding the old `AI_PROJECT_HANDOFF_NEXT_STEPS.md` roadmap (now retired from the project folder — see [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]], 2026-08-24).

For visual design, use [[ChalkCode/Ngarri Mentor Text Library/Design/00 Design Index]] before coding. For system/database architecture, use [[ChalkCode/Ngarri Mentor Text Library/Architecture]].

## Purpose

Ngarri Primary School has a curated collection of mentor texts — books chosen because they model specific writing techniques, comprehension strategies, and school values. That knowledge currently lives in teachers' heads and scattered notes. The app lets teachers search the collection by teaching purpose (a writing trait, reading strategy, PRIDE value, or inquiry lens) rather than by year level alone, and see exactly why a book fits.

Two collections exist; keep them separate. **School Library** (`School Library/` in the project folder, 343 canonical books after duplicate resolution, originally 342/352) is the primary app content and the sole focus through launch. **Personal Collection** (`Personal Collection/`, ~129 books, Phill's own) is explicitly lower priority — not part of the current build.

The riskiest assumption is that AI web-search-grounded tagging can enrich the books with no human-sourced data, without a single hallucinated tag. The 20-book spot-check is the first go/no-go gate — bulk enrichment (and the app build that depends on full data coverage) should not proceed past it until Phill has reviewed and approved the sample.

The project should help answer:

- Which books in the library best teach a specific writing trait or reading strategy?
- Which books connect to a PRIDE value or an inquiry lens?
- Is this book's tagging teacher-confirmed, OzLit-confirmed, or still an AI suggestion awaiting review?
- What does the school actually own, with a verified blurb and cover?

## What Success Looks Like

**For a classroom teacher:** open the app, filter to Year 5 / Inferring / Picture Book, see relevant books with covers and blurbs, click one to read the full detail page — curriculum throughline, how this specific book teaches that strategy, a ready-made teaching idea, related books — all in under a minute.

**For a leading teacher:** a new book arrives. Open the app, click "Add Book", type the title — the app pre-fills what it can. Add the blurb, tick the writing traits already known, done in 10-15 minutes. Annotation deepens over time.

**For the school:** the mentor text library becomes a living, searchable resource, not a spreadsheet or sticky notes on a shelf. When a teacher leaves, their knowledge of the collection stays in the system.

## Core Domains

| Domain | Owns | Must Not Own |
|---|---|---|
| Book Data | title, author, illustrator, verified blurb, cover, lifecycle status, `source_row` traceability to the master list | curriculum tags, tag provenance |
| Curriculum Reference Data | canonical writing-trait, reading-strategy, PRIDE-value, and inquiry-lens definitions, including verbatim KU/KS text, held in Supabase reference tables | book-specific judgements |
| Annotation & Provenance | book-to-tag links (many-to-many, one row per tag), `source_type`/`status`/`confidence`/evidence per tag | curriculum vocabulary definitions, book metadata |
| Source Hierarchy / Matching | teacher-spreadsheet and OzLit fuzzy-matching, human-confirmed match review, canonical slug maps | the tag content itself |
| AI Enrichment Pipeline | web-search-grounded tag generation, evidence/slug validation, abstention, the spot-check gate, resumable bulk runs | database writes without validation, teacher/OzLit row overwrites |
| Database / Access Layer (Supabase) | schema, row-level security (public read, service-role write only), migrations | UI, product judgement |
| Future Public App | purpose-first search, book detail display of approved content only, no teacher login | raw provenance display, admin writes |
| Future Admin/Leader Area | add/edit books, manual curriculum tagging, AI-suggestion review queue, passcode gate | teacher-facing public routes |
| Visual Design | typography, colour roles, screen composition (partially decided — see Design/) | domain rules, data, business logic |

## Information Flow

1. Source books are listed from the master CSV; duplicates are found and resolved.
2. Blurbs and covers are sourced and verified per book.
3. Teacher spreadsheet and OzLit records are fuzzy-matched against the master list; a human confirms each match.
4. Confirmed matches are combined into a canonical import, applying slug maps so the same trait isn't stored under two names.
5. The Supabase schema is created; reference data and the canonical import (books + confirmed annotations) are loaded.
6. AI Enrichment fills the remaining gap books, gated by the spot-check — nothing bulk-runs until approved.
7. (Future) The public app reads only approved-status content for search and book detail.
8. (Future) The admin app writes new books and tags via the service role, feeding each new book back through the same match/tag/review pattern as steps 3-6.

## Part 1 / Part 2 Boundary and Shared Foundations

This project has two deliberately separate modes of work. They should share domain rules and validation logic, but they should not share the same user experience or operational assumptions.

**Part 1 - one-time migration / database creation:** the large, script-driven process for the current School Library collection. This includes duplicate resolution, title/author normalisation, blurb verification, cover lookup/download, teacher-spreadsheet matching, OzLit matching, canonical import generation, AI gap enrichment where justified, SQL generation, and final database validation. It is allowed to be technical and batch-oriented because Phill/developer sessions are the operators.

**Part 2 - ongoing curation app:** the small-batch workflow for learning specialists adding 1-10 newly purchased books at a time. This must be calm, teacher-friendly, passcode-gated, and usable without an AI key configured. The app may offer metadata lookup, cover/blurb lookup, duplicate warnings, and optional AI suggestions, but leader-entered data is first-class and AI suggestions must remain in review until explicitly approved.

### Part 1 Completion Definition

Part 1 is complete only when the current School Library database is clean, loaded, searchable by reliable curriculum tags, and documented well enough that Part 2 can reuse the same rules instead of reconstructing them. The practical completion checklist is:

- verify the canonical migration state: 343 books, duplicate decisions applied, blurbs/covers present, teacher/OzLit annotations imported, and row counts matching the migration reports
- resolve the partial-coverage question: check whether any book has writing-trait data but no reading-strategy data, or reading-strategy data but no writing-trait data, and decide whether those books belong in enrichment scope
- run the persisted offline tests for `School Library/Migration/enrich_traits.py` before any live API enrichment
- run the 20-book AI Enrichment Pass 1 sample only after an Anthropic key is available
- manually review the sample CSV for wrong-book matches, weak evidence, over-tagging, non-canonical slugs, missing abstentions, and overconfident confidence values
- improve the prompt, validator, abstention rules, or evidence requirements if the sample exposes a reusable failure category
- run bulk enrichment only after Phill explicitly approves the spot-check
- generate SQL from saved enrichment output, apply it to Supabase, and verify post-import counts against generated statements
- produce a final Part 1 validation report covering total books, books with writing traits, books with reading strategies, books still missing tags, AI abstentions, human-review counts, and known caveats before pilot app work

### Shared Foundations To Build During Part 1

These foundations should be extracted or formalised during Part 1 because they carry directly into Part 2 and reduce future dependence on ad hoc AI judgement:

| Foundation | Part 1 Use | Part 2 Carry-Forward |
|---|---|---|
| Normalisation utilities | Clean titles/authors, compare source rows, reduce duplicate false positives | Detect possible duplicate books when a leader enters a new title/author |
| Canonical slug validation | Reject non-canonical AI or source slugs before SQL generation | Validate every admin-entered or AI-suggested curriculum tag before saving |
| Source hierarchy service | Preserve teacher-spreadsheet > OzLit > AI gap-fill rules during import | Prevent AI suggestions from overwriting leader-entered or already-approved data |
| Evidence validator | Require quoted evidence/source for every AI-suggested tag | Power the Needs Review queue with inspectable evidence for each suggestion |
| Blurb quality checker | Apply publisher/source quality rules across the existing collection | Flag weak, short, mismatched, or catalogue-style blurbs for leader review |
| Cover/no-cover handling | Verify current covers and document fallback behaviour | Provide a polished no-cover state for future newly added books |
| Review item data shape | Store `source_type`, `status`, `confidence`, evidence, and review state consistently | Feed the admin review screen without changing the database model later |
| App-ready database queries/views | Audit search/detail coverage after import | Back teacher search results, book detail pages, admin queues, and missing-data views |

The important rule is that scripts may be one-time, but the domain decisions inside them should not be one-off. Normalisation, slug maps, source hierarchy, evidence requirements, overwrite prevention, and review statuses are project foundations, not migration trivia.

### Boundary Checks

Use these checks whenever deciding where new work belongs:

- If the task processes many existing books and produces migration reports or SQL, it belongs to Part 1.
- If the task helps a learning specialist add a small number of newly purchased books, it belongs to Part 2.
- If the task defines what counts as a valid book, tag, source, evidence snippet, status, or overwrite rule, it belongs in shared foundations and should be reusable by both parts.
- If a script contains a rule the future app also needs, extract or document the rule rather than leaving it hidden inside that script.
- If the future app starts to look like a bulk migration dashboard, split the workflow back apart; small-batch curation is a different product experience from one-time data creation.

## Build Sections

Faithful record of the original 14-step ordered work plan, reorganised into build sections with real completion status. Historical script/count details are preserved here rather than compressed away, since future sessions rely on them.

### Section 1 - Freeze the Current Direction

- **Status: complete**, 2026-06-25.
- Established: purpose-first search, year-level-secondary filtering, normalized annotation tables (not boolean columns), internal/admin-only source provenance. Superseded docs archived.

### Section 2 - Planning Foundations

- Create the migration working folder, governance docs, schema design.
- **Status: complete.** `School Library/Migration/` created 2026-06-25. Project-folder governance docs (`AI_CONTRACT.md` etc.) written 2026-08-03, then retired in favour of this ChalkCode folder becoming the sole instruction-document location, 2026-08-24.

### Section 3 - Resolve Duplicates

- **Status: complete**, corrected 2026-07-27.
- `find_duplicates.py` found 21 candidate pairs (`duplicate_resolution.csv`). All reviewed: 11 Little People Big Dreams pairs kept separate (different books in the series), 1 false positive rejected (Diary of a Worm vs Diary of a Wombat), 9 genuine duplicates removed — #1 (kept #309, Two-Hearted Numbat, correct co-author + verified blurb), #61 (kept #58, Wolf in the Snow), #62 (kept #59, Amazing Animal Journeys), #63 (kept #60, The Watertower), #70 (kept #300, Fantastic Mr Fox), #308 (kept #91, Stellarphant), #307 (kept #155, The Biscuit Maker), #271 (kept #270, Fing), #284 (kept #290, Don't Let the Pigeon Drive the Bus).
- **Correction, 2026-07-27:** an earlier log entry wrongly assumed rows #61-63 needed retitling — investigation showed the "missing" titles (Shortcut/Click Clack Moo/Diary of a Worm) already existed correctly and uniquely at #64-66; #61-63 were just accidental exact duplicates needing removal, no title fix. Similarly "#67 vs #300 Fantastic Mr Fox" was a misread — #67 is "Wild Australian Life" and never was a duplicate.
- No `book_copies`/multi-copy table needed — every pair resolved to one canonical record.

### Section 4 - Ingest Teacher Spreadsheet

- **Status: complete**, 2026-07-30.
- `match_teacher_traits.py` matched all 91 tagged books (of 381 rows in the `Texts` sheet) against the master list — 89 exact, 2 fuzzy (both confirmed correct once 2 title typos were fixed). All 91 rows confirmed in `teacher_spreadsheet_match_review.csv`.
- Source structure: `Texts` sheet, 381 book rows; `Wishlist` sheet, 4 rows, excluded (not current library books). Trait columns: Ideas, Audience/Voice, Organisation, Word Choice, Sentence Fluency, Conventions, Spelling, Presentation — `Spelling` maps to `Conventions` (confirmed by Phill, 2026-07-30; see Decisions Log), not a separate app trait.

### Section 5 - Build OzLit Matching Review

- **Status: complete**, 2026-07-30.
- `match_ozlit.py` fuzzy-matched all 169 OzLit books against the master list — 55 exact + 1 fuzzy (spelling variant, confirmed same book) = 56 confirmed matches; 1 title-only match correctly rejected ("Stuck" — same title, two different authors/books); 112 OzLit books have no match in the school's 352-book collection. Output: `ozlit_match_review.csv`.
- (An earlier estimate in the original handoff doc guessed ~45 exact matches before the matching script was built and fuzzy-matching applied — 56 is the correct, final, confirmed figure.)

### Section 6 - Finish Blurb Resolution

- **Status: complete**, 2026-07-29.
- `apply_replacements.py` built per spec, plus one correction: its "AUTO_VERIFIED means already correct" assumption was wrong for 86 rows in the 189-341 range where the verified blurb had never actually been written into the master list — fixed and re-applied. 7 rows (#61-67) safety-skipped due to a stale row/title misalignment (see Section 3 correction) — resolved separately, no blurb action needed.
- Remaining 112 flagged/unresolved blurbs completed via 4 parallel background agents searching Readings.com.au and fallback retailer sites (2026-07-29 overnight run) — 100 high-confidence, 6 held for manual review, 0 left blank. **All 352 books have a blurb.** Full audit: `overnight_blurb_lookup_audit.csv`.

### Section 7 - Produce Canonical Import Preview

- **Status: complete**, 2026-07-30.
- `build_canonical_preview.py` combined every Section 3-6 decision. Outputs: `canonical_books_preview.csv` (343 books), `writing_trait_annotations_preview.csv` (391 rows — teacher spreadsheet takes priority, OzLit fills gaps only where the teacher spreadsheet didn't already tag that trait), `reading_strategy_annotations_preview.csv` (260 rows — OzLit only, the teacher spreadsheet has no reading-strategy data), `migration_validation_report.md`.
- One slug mismatch caught and fixed: OzLit's `voice` renamed to the app's `voice_audience` via an explicit map, preventing a silent duplicate trait.
- **253 of 343 books have zero rows in both `writing_trait_annotations` and `reading_strategy_annotations` combined** and are flagged `needs_ai_enrichment` — this is the AI Enrichment Pass 1 target set (see Section 9 below and [[ChalkCode/Ngarri Mentor Text Library/specs/01 AI Enrichment Pass 1]]).
- **Open question, not yet resolved:** the "253" figure counts books with zero rows across *both* categories combined. A book could plausibly have OzLit reading-strategy data but zero writing-trait data (or vice versa) and NOT be flagged `needs_ai_enrichment`, since its row count isn't zero — meaning it would be silently skipped by the current Pass 1 scope even though it's genuinely missing a category. This has not been checked against the live data. See Hard Questions below.

### Section 8 - Database (Supabase)

- **Status: live**, since 2026-07-30. Free-tier project, region `ap-southeast-2` (Sydney). Full schema, RLS, reference and annotation tables loaded — see [[ChalkCode/Ngarri Mentor Text Library/Architecture]] for the live layout. Security advisor: zero findings. Performance advisor: informational only, addressed with added indexes.

### Section 9 - AI Enrichment Pass 1 (Writing Traits & Reading Strategies)

- Fill the 253 gap books' writing-trait and reading-strategy data via web-search-grounded AI tagging, gated by a human-reviewed spot-check.
- **Status:** script built and offline-tested 2026-08-03; **20-book spot-check completed 2026-08-25 with zero API key** (Claude researched it directly via web search, validated through the script's own code — see [[ChalkCode/Ngarri Mentor Text Library/specs/01 AI Enrichment Pass 1]]). **Now awaiting Phill's review of the spot-check CSV.** The remaining ~233-book bulk run still needs either a repeat of the manual approach or a real API key (Anthropic or, pending the provider question below, OpenAI).

### Section 10 - Pilot App

- Build the smallest useful slice: purpose-first filters, result cards, book detail page, no-cover fallback, starting with 30-50 pilot books (recommended: the ~90 books with trustworthy human-sourced tags — see Suggested First Vertical Slice below). Do not wait for every blurb/cover to be perfect before testing search.
- Pilot test queries: Word Choice, Voice/Audience, Inferring, Determination, Environmental Sustainability, Australian picture books. Success criterion: a teacher can find a useful set of books for a teaching purpose in under a minute.
- **Status: not started.**

### Section 11 - Leader/Admin Area

- Add/edit books, review AI suggestions, edit annotations, approve/reject fields, upload resources, manage missing covers — protected admin area within the one app, not a separate app.
- Must be fully usable with no AI key configured — manual tagging is first-class (see [[ChalkCode/Ngarri Mentor Text Library/Working Contract]] rule 16; [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]] 2026-08-24).
- **Status: not started.** See [[ChalkCode/Ngarri Mentor Text Library/specs/04 Leader Admin Area]].

### Section 12 - AI Enrichment Pass 2 (Remaining Gaps)

- PRIDE values, inquiry lenses, teaching ideas, why-use bullets — for all 343 books (no book currently has any data for these fields at all, unlike traits/strategies which have partial human coverage).
- Only use AI for fields not already filled by teacher data or OzLit (OzLit has no PRIDE/inquiry/teaching-idea data at all, so this pass covers every book). AI should write "In this book" notes, generate teaching ideas, suggest PRIDE/inquiry tags only with specific evidence, and leave fields blank when uncertain. AI must never invent blurbs, overwrite teacher-entered tags, override OzLit for traits/strategies/year levels without review, or paraphrase Ngarri KU/KS text.
- **Status: not started.**

### Section 13 - Cover Cleanup

- Do not block launch on missing covers. Use downloaded cover where available, a polished no-cover template otherwise, admin queue for the rest. Note: `download_covers.py` currently skips `No_Cover` rows, so they won't retry automatically — needs a deliberate re-run or cleanup pass, not an automatic fix.
- **Status: not started** (not urgent — all 343 canonical books already have a real cover as of 2026-07-30 data setup; this section covers any future gaps as the collection grows).

### Section 14 - Launch Readiness

Before school-wide launch (no login for teachers, decided 2026-07-27):

- teacher-facing app is public with no login, by design
- admin passcode gate built and tested on `/admin` routes
- Supabase RLS policies tested — public read on teacher-facing tables, writes restricted to passcode-checked admin routes only
- API keys removed from docs and local committed files (known outstanding issue: `google_books_api_key.txt` in plaintext in the project folder — see [[ChalkCode/Ngarri Mentor Text Library/Working Contract]] Anti-Shortcut Rules)
- school-owned Anthropic API account created with a monthly spending cap, replacing any personal key (only needed if in-app AI enrichment is enabled — the app must work without it)
- backup/export process documented
- copyright use of covers/resources considered — specifically, PDF hosting for any full-text or teaching-resource files is pending copyright clearance with school admin under a Copyrite licence (not yet resolved)
- pilot teachers have tested real planning tasks

## Suggested First Vertical Slice

Build the pilot app's search and book-detail screens against only the ~90 books with human-confirmed data first, before the AI-enriched 253 are merged in. This validates the search experience on trustworthy data before scaling across the full collection.

## Hard Questions To Resolve Later

- **AI provider: Anthropic vs. OpenAI.** The school has a ChatGPT Pro subscription (2026-08-25) — separate from OpenAI API access/billing, which would need its own setup. If the school's OpenAI API access is confirmed and preferred over a dedicated Anthropic account, the enrichment pipeline (both the one-time Pass 1 script and the future ongoing per-book pipeline) could be rewritten against OpenAI's API instead — the validation/evidence/slug-canon/abstention rules are provider-agnostic, only the API-call layer changes. Not yet decided; "Codex" itself is a coding assistant, not the integration point — the actual target would be OpenAI's model API. See [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]], 2026-08-25.
- **Data-model gap:** does any book have partial annotation coverage (e.g. OzLit reading-strategy data but zero writing-trait data) that the "253 gap books" `needs_ai_enrichment` flag would silently miss, since it only fires on zero rows across both categories combined? Not yet checked against live data (see Section 7 note above).
- Should the school set up its own Anthropic API account before or after the pilot app ships?
- How will the ~6 books still flagged `needs_review` on their blurbs get resolved?
- Should AI Enrichment Pass 2 happen before or after the pilot app is in front of real teachers?
- Colours and visual branding — deferred (typography is decided; exact palette is not — see Design/01 Visual Direction).
- "Similar books" / related-books logic — to be experimented with during build, not yet designed.
- Whether incomplete books (still mid-enrichment) should display differently to teachers.
- Whether to add a free-text search bar in addition to the purpose-first filter dropdowns.
