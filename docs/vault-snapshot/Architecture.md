---
title: Ngarri Mentor Text Library - Architecture
type: architecture
tags: [chalkcode, ngarri, architecture, supabase, nextjs]
created: 2026-08-24
updated: 2026-08-24
status: active
---

## Current reconciliation — 6 September 2026

The database is restored and the recorded access correction is applied. Older blanket public-read, complete-provenance and local schema-authority claims below must be checked against the recovered schema and deployment evidence. The production reviewer app is not implemented.

Read [[ChalkCode/Ngarri Mentor Text Library/Current State and Codex Handover]] first. This dated block supersedes conflicting historical statements below; earlier wording is retained for provenance.


# Ngarri Mentor Text Library - Architecture

System design, live database layout, and the data pipeline. This is a project-specific extra document beyond the ChalkCode core template (see [[ChalkCode/Ngarri Mentor Text Library/index]]), migrated 2026-08-24 from the project folder's own `ARCHITECTURE.md` and `APP_DESIGN.md`, now the sole copy. The DDL authority remains the live file `School Library/Migration/schema.sql` in the project folder — this document describes its shape.

## System Overview

```
[Data pipeline: local Python scripts]          [Live database]              [Future app]
School Library/Migration/*.py        --SQL-->  Supabase (Postgres)  <-----  Next.js on Vercel
  blurbs, covers, matching, imports,           project dahilwcsbtstfbokbxws   public teacher UI +
  AI enrichment (spot-check gated)             ap-southeast-2 (Sydney), free  passcode admin area
```

## Tech Stack

| Layer | Technology | Notes |
|---|---|---|
| Database + Auth + Storage | Supabase (PostgreSQL) | Free tier to start; pauses after 1 week inactivity on free — upgrade to Pro ($25/month) when the school adopts it |
| App Framework | Next.js | |
| Hosting | Vercel | Free Hobby tier to start; Pro ($20/month) when the school officially adopts it |
| Background jobs | Local Python scripts (one-time migration) / Next.js API route (1-2 book additions) | Enrichment volume is low (343 books once, then 1-2 at a time) — Supabase Edge Functions add deployment complexity not justified at this scale |
| AI tagging | Claude API (Anthropic) | Curriculum tag suggestions; school-owned key with spending cap in production, never personal (decision 2026-08-24) |

## Database (live since 2026-07-30)

- **Supabase project:** `dahilwcsbtstfbokbxws`, region `ap-southeast-2`, free tier.
- **Core table:** `books` (343 rows) — title/author/illustrator, verified blurb + `blurb_status`, cover fields, lifecycle `status`, and `source_row` (unique int) preserving traceability to the master CSV. GIN index on title for search.
- **Reference tables** (read-only vocabularies, seeded from `reference-data/*.json`): `writing_traits`, `writing_trait_detail`, `reading_strategies`, `reading_strategy_detail`, `pride_values`, `inquiry_lenses`. Ngarri curriculum text stored **verbatim** in `text[]` columns (`ku_verbatim`, `ks_verbatim`, `we_will`, `selection_indicators`, ...).
  - Note: early design docs (`APP_DESIGN.md`) proposed an `ozlit_books` reference table to hold matched OzLit records directly. That table was **not** built — OzLit matches instead flow straight into the annotation tables during canonical import, with provenance recorded via `source_type='ozlit'`. Don't assume `ozlit_books` exists.
- **Annotation tables** (normalized many-to-many, one row per book-tag pair — NOT boolean columns): `writing_trait_annotations`, `reading_strategy_annotations`, `pride_value_annotations`, `inquiry_lens_annotations`, `teaching_ideas`, `why_use_bullets`, `teaching_resources`. Every row carries provenance (`source_type`, `source_name`, `confidence`, `status`, `reviewed_by/at`).
- **Uniqueness:** e.g. `unique (book_id, trait_slug, year_level)` — prevents duplicate tags and accidental cross-source double-writes.
- **Indexes:** covering indexes on all annotation FK/slug columns (added 2026-07-30/08-03 after advisor review).

### Access model (RLS)

- All tables: RLS enabled, **public SELECT only** (anon key). No INSERT/UPDATE/DELETE grants for `anon`/`authenticated` — this is how "no teacher login" stays safe.
- All writes go through the `service_role` key, server-side only (migration scripts now; passcode-checked `/admin` API routes later). The service key never ships to a browser.
- Publishable key (safe for the app frontend): `sb_publishable_oZSkItRfh0Y3yLqixzwa0g_nvjr-Iye`.

### Provenance fields, actually implemented

The live schema's provenance fields are: `source_type`, `source_name`, `confidence`, `status`, `reviewed_by`, `reviewed_at`. Early design docs (`AI_PROJECT_HANDOFF_NEXT_STEPS.md` §6, `BOOK_DETAIL_FIELDS.md`) also proposed separate `source_url` and `review_status` fields — these were **simplified into the single `status` field** in the schema actually built (status values below double as review state). Don't assume `source_url`/`review_status` exist as separate columns; if source URLs need capturing per tag (e.g. for AI enrichment evidence), fold them into `source_name` as done in the enrichment script's SQL generation, or treat as a future schema addition.

Allowed `source_type`: `teacher_spreadsheet` | `ozlit` | `ai_suggested` | `teacher_override`.
Allowed `status`: `blank` | `imported_teacher` | `imported_ozlit` | `ai_suggested` | `teacher_reviewed` | `teacher_added` | `rejected`.

## Source Hierarchies

Three distinct hierarchies apply to different field groups — don't conflate them.

**Writing traits, reading strategies, year levels:**
1. Teacher-entered Ngarri spreadsheet data (highest priority for fields already filled in)
2. OzLit data (`reference-data/oz-lit-calibration.json`)
3. AI annotation using Ngarri reference JSONs (gap-fill only, evidence-grounded)
4. Manual teacher/admin override

**PRIDE values and inquiry lenses** (OzLit has no data for these at all — only two rungs before AI):
1. Teacher-entered Ngarri spreadsheet data, if available
2. AI annotation using Ngarri reference JSONs
3. Manual teacher/admin override

**Blurbs:**
1. Publisher site
2. Author site
3. Goodreads or professional review source
4. Google Books API
5. Manual fallback sources such as Readings.com.au

## Data Pipeline (Migration Scripts)

All in `School Library/Migration/` unless noted. Each is a run-once/run-again-safe local Python script; there are no server-side pipeline components by design.

| Script | Role |
|---|---|
| `../fetch_blurbs.py`, `../verify_blurbs.py`, `../recheck_quality.py`, `../apply_replacements.py` | Blurb sourcing/verification pipeline (School Library root) |
| `../download_covers.py` | Cover downloads to `School Library/Covers/`. Skips `No_Cover` rows — they won't retry automatically, needs deliberate re-run |
| `find_duplicates.py` | Duplicate candidate report -> human decisions in `duplicate_resolution.csv` |
| `match_teacher_traits.py` | Fuzzy-match teacher spreadsheet rows -> human review CSV |
| `match_ozlit.py` | Fuzzy-match OzLit calibration books -> human review CSV |
| `build_canonical_preview.py` | Combines all decided data -> `canonical_books_preview.csv` + annotation preview CSVs + validation report. Applies slug maps and teacher-priority rules; makes no new judgment calls |
| `schema.sql` | Full DDL — the schema authority |
| `enrich_traits.py` | AI enrichment pass 1 (sample -> spot-check gate -> bulk -> sqlgen). See [[ChalkCode/Ngarri Mentor Text Library/specs/01 AI Enrichment Pass 1]] |
| `test_enrich_traits.py` | Offline regression suite for `enrich_traits.py` (24 checks, no API/DB needed). Run before any bulk enrichment run and after any edit to the script — see the test-suite history note in [[ChalkCode/Ngarri Mentor Text Library/specs/01 AI Enrichment Pass 1]] for why this matters |

Pattern for DB imports: scripts generate SQL text; chunks are applied via the Supabase MCP `apply_migration`; success verified by count queries (never assume a client-side network error means server-side failure — check state first).

## Future App (Decided Shape, Not Yet Built)

- **One Next.js app** on Vercel. No monorepo, no `/packages` split — shared logic in `lib/` (`/lib/database`, `/lib/enrichment`, `/lib/ai-tagger`). Routes: `/app/books` (public teacher browse/search/detail), `/app/admin` (leader review/edit/add).
  - A two-app split (`teacher-app` + `leader-app`, separate Vercel deployments sharing one Supabase project) was the original proposal and remains possible if the leader app ever needs isolated deployment risk from the teacher app — deliberately not adopted for the first build; revisit only if a real need emerges.
- **No Supabase Edge Functions** — enrichment stays in local scripts / API routes.
- **No embeddings** — `reference-data/writing-throughlines.json` is a structured lookup.
- Public teacher UI (purpose-first search -> book detail), no login.
- `/admin` area behind a single shared passcode; all admin writes via server-side service-role calls. Includes the review queue where `ai_suggested` rows get approved.
- In-app AI enrichment is **optional**: it runs only if an Anthropic key (school-owned, spend-capped — never personal) is configured server-side; without one, manual tagging in the admin form is the fully supported path.

## Boundary Rules

- Domain vocabulary (slugs, statuses) lives in the database reference tables; code and prompts must import/echo it, never redefine it.
- `reference-data/*.json` is read-only input — pipeline scripts read it, never write it.
- Curriculum text passes through the system verbatim end-to-end.
- The teacher-facing app reads approved content; raw provenance stays internal/admin-only.

## Reference Data → Field Mapping

Which JSON file feeds which book-detail-page fields, and how to use it. Merged 2026-08-24 from the retired `SCHOOL_LIBRARY_CONTEXT.md`.

| JSON File | Fields It Feeds | How to Use |
|---|---|---|
| `writing-throughlines.json` | Writing traits: which traits, year levels, "In this book" notes, KU/KS display text | Load all 7 traits with year progressions. KU/KS is verbatim from this file — never paraphrase it. |
| `reading-strategies.json` | Reading strategies: which strategies, year levels, "In this book" notes, KU/KS display text | Same pattern as writing traits. Tag only strategies the text *demands*. |
| `pride-values.json` | PRIDE values: which values, "In this book" notes | Tag only when a specific story moment embodies the value — must cite a character decision or event, not a general theme. |
| `inquiry-lenses.json` | Inquiry lenses: which lenses, Big Question addressed, "In this book" notes | Must connect to a specific Big Question from this file. If none fits, leave blank. |
| `oz-lit-calibration.json` | Writing traits + reading strategies for any OzLit-matched book | Highest-priority source for matched books — AI confirms and supplements rather than deciding independently (see [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]], 2026-07-30 OzLit entry). |

## Legacy Migration File Formats

Historical audit-trail files from the blurb verification pipeline (in `School Library/Blurb Verification/`), preserved on disk but not actively maintained now that all 352 books have a verified blurb. If a future session needs to interpret them: batch `.xlsx` files share the schema `Row | Title | Author | Current_Blurb | Verification_Status | Corrected_Blurb | Source_Used | Date_Verified | Notes`, with `Verification_Status` values `Verified` | `ERROR - Corrected` | `Verified - Assumed Accurate` | `MINOR UPDATE` | `Not Started` | `DUPLICATE - See Row N`. `Blurb_Verification_Master_Status.csv` is explicitly outdated — use the batch files and `Blurb_Fetch_Raw.csv` instead.

## Books With Local Full-Text Available

14 school library books have local PDF/EPUB files available (tracked in `reference-data/available-texts.json`), useful for enrichment cross-referencing (trait identification, reading-strategy tagging) beyond just the blurb: #34 The Important Book, #71 The Twits, #90 Hello Harvest Moon, #93 Whoever You Are, #157 Frederick, #232/#233/#235/#237/#239 (Saxby's Dingo/Koala/Kookaburra/Emu/Big Red Kangaroo series), #240 The Boy Who Loved Words, #242 The Giving Tree, #282 The Treasure Box, #296 Owl Moon.

## Source Documents for Reference Data

Which physical/PDF documents feed which reference tables, and extraction priority — from the original data-model design work.

| Document | Priority | What to extract | Notes |
|---|---|---|---|
| `Completed English Writing Throughlines.pdf` (in `Shared Resources/`) | High | Verbatim Key Understanding + Key Skill per writing trait per year level | No paraphrasing — feeds `writing_trait_detail` |
| `Curriculum - ENGLISH. working copy.pdf` | High | Verbatim KU + KS per reading strategy per year level | This is the definitive source for the 11-strategy canonical list (see [[ChalkCode/Ngarri Mentor Text Library/Research Notes]]) |
| `PRIDE School Values (1).pdf` | High | Full definition per value + key questions/indicators | Ngarri's specific framing matters — don't substitute generic PRIDE definitions |
| `PRIDE Values Matrix.pdf` | Medium | Observable indicators per value | May duplicate the School Values PDF — compare, add anything additional |
| `Ngarri PS conceptual lenses for inquiry (1).pdf` | High | Full definition per lens + Big Questions | Big Questions are required for the inquiry-lens tagging selection rule |
| `Oz Lit Mentor Texts by Year Level and Genre.pdf` (43 pages) | High | Per book: title, author, year level range, genre, writing traits, reading strategies | Primary OzLit calibration source |
| `6+1_Traits_Guide.txt` | Low | Cross-reference with throughlines for additional craft examples | Supplement only |

## OzLit Reading-Strategy Name Mapping

OzLit's own strategy names don't map 1:1 onto Ngarri's 11-strategy list:

- OzLit's "Determining Importance" (DI) maps directly — no remapping needed.
- OzLit's combined "S&S" maps to Ngarri's two separate strategies: Summarising + Synthesising.
- Ngarri's "Self-monitoring" strategy has no OzLit equivalent — treat as Ngarri-only, never sourced from OzLit.
- OzLit year levels indicate "first introduced at" — used as a starting point when assigning Ngarri's year-level ranges, not copied literally.
