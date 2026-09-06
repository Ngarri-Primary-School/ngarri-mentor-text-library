---
title: Ngarri Mentor Text Library
type: project
tags: [chalkcode, project, supabase, nextjs, vercel, education, curriculum, ngarri, library]
status: planning
created: 2026-06-15
updated: 2026-07-30
---

## Current reconciliation — 6 September 2026

The database is built and restored. Complete cover readiness is not established. A local review prototype exists, while the production teacher/admin application is still to be built. The older phase checklist below is historical.

Read [[ChalkCode/Ngarri Mentor Text Library/Current State and Codex Handover]] first. This dated block supersedes conflicting historical statements below; earlier wording is retained for provenance.


# 📚 Ngarri Mentor Text Library

> A web app for Ngarri Primary School teachers to search the school's 343-book mentor text library by teaching purpose — writing trait, reading strategy, PRIDE value, or inquiry lens — rather than by year level alone. Built in two phases: a one-time data setup for the existing collection, then an ongoing app where leading teachers add 1–2 new books at a time.

---

## 🗂️ AI Working-Control Docs

Full ChalkCode project rules (Working Contract, Project Map, Decisions Log, Research Notes, specs/, Design/) live alongside this note — see [[ChalkCode/Ngarri Mentor Text Library/index|index]]. Read those before substantial AI-assisted work; this note stays the quick-status dashboard.

## 🔗 Links & Services

| Service | Name / URL | Notes |
|---------|-----------|-------|
| **Project folder** | `/Users/phillcantone/Library/Mobile Documents/com~apple~CloudDocs/Family/Phill/AI Coding/Mentor Texts/` | Moved from OneDrive to iCloud Drive on 2026-07-22 to fix sync/cloud-only file timeouts |
| **Prototype** | [fox-deploy-olive.vercel.app](https://fox-deploy-olive.vercel.app) | Fox book detail page mockup — reviewed and used to drive the revised page layout |
| **Hosting (planned)** | Vercel | Not yet provisioned |
| **Database (planned)** | Supabase (PostgreSQL) | Not yet created — schema designed only |
| **AI tagging** | Claude API (Anthropic) | Not yet built — curriculum tag suggestions during enrichment, gaps only, never overrides teacher/OzLit data |

---

## 🗄️ Database Schema (Designed — Not Yet Built)

Normalized annotation tables, not boolean columns on `books` — chosen so source hierarchy, confidence, year-level nuance, and teacher review all have somewhere to live.

| Table | Purpose |
|-------|---------|
| `books` | Stable metadata: title, author, illustrator, publisher, year, text type, genre, year level range, blurb, cover, duplicate group |
| `writing_trait_annotations` | Book × writing trait × year level, with verbatim KU/KS + "in this book" note |
| `reading_strategy_annotations` | Book × reading strategy × year level |
| `pride_value_annotations` | Book × PRIDE value, with text evidence |
| `inquiry_lens_annotations` | Book × inquiry lens, with Big Question addressed |
| `teaching_ideas` | Practical lesson ideas linked to a book |
| `why_use_bullets` | Short teacher-facing reasons to use the book |
| Reference tables | `writing_traits`, `reading_strategies`, `pride_values`, `inquiry_lenses`, `ozlit_books` — populated once from Ngarri's own curriculum PDFs |

**Explicitly deferred:** `book_copies`/`library_holdings` table, per-user accounts (`users` table dropped — admin area uses a single shared passcode instead, decided 2026-07-27), and Supabase Edge Functions for enrichment (local scripts / a Next.js API route cover the actual volume — 343 books once, then 1–2 at a time).

---

## 🧭 Curriculum Frameworks (Ngarri-Specific)

| Framework | Values |
|---|---|
| **Writing traits (7)** | Ideas, Organisation, Voice/Audience, Word Choice, Sentence Fluency, Conventions, Presentation |
| **Reading strategies (11)** | Summarising, Determining Importance, Predicting, Making Connections, Synthesising, Inferring, Visualising, Analysing, Critiquing, Questioning, Self-monitoring |
| **PRIDE values (5)** | Pride, Respect, Integrity, Determination, Excellence |
| **Inquiry lenses (4)** | Social Responsibility, Environmental Sustainability, The Physical World, Identity/Creativity/Wellbeing |

Source hierarchy for annotations: **teacher-entered spreadsheet → OzLit → AI-suggested → manual override.** Source/provenance is stored internally for leader review — never shown as teacher-facing chips.

---

## 📁 Key Documents (in project folder)

| File | Role |
|------|------|
| `PROJECT_OVERVIEW.md` | Full scope: vision, two-phase plan, tech stack, success criteria |
| `APP_READINESS_CHECKLIST.md` | Plain-English readiness checklist — for Phill and external review (e.g. an app designer) |
| `AI_PROJECT_HANDOFF_NEXT_STEPS.md` | Current roadmap, ordered work plan, completed-step log |
| `BOOK_DETAIL_FIELDS.md` | Authoritative field/annotation/provenance model |
| `APP_DESIGN.md` | Product and UX design, book detail page spec |
| `School Library/Migration/` | Duplicate resolution, matching scripts, canonical import preview |

---

## 📋 Phases

### Phase 1 — One-Time Data Setup
Getting all existing books clean, verified, and annotated. Happens once; not repeated at this scale. **Complete as of 2026-07-30**, except AI enrichment (deliberately deferred to Phase 2).

- [x] Master book list — grew from 342 to 352 (10 books the school owns were found missing from the original list during teacher-spreadsheet matching)
- [x] Duplicate detection and resolution — 9 confirmed duplicates removed, 343 canonical books remain
- [x] ~16 long-standing title/author typos found and fixed during blurb/cover lookups
- [x] Blurbs — 352/352 books verified (6 flagged for a quick manual double-check)
- [x] Covers — 343/343 canonical books have a real cover image
- [x] Teacher writing-traits spreadsheet matched and imported (89 books)
- [x] OzLit matched and imported (54 books — writing traits + reading strategies)
- [x] Canonical import preview built — ready to load into Supabase once it exists
- [ ] AI enrichment for the 253 books with no writing-trait/reading-strategy data, and PRIDE values/inquiry lenses/teaching ideas for all books — **deferred to Phase 2**, needs the real app review workflow rather than a one-off script

### Phase 2 — The Live App
**Not started.** Ongoing app once built. New books added 1–2 at a time by a leading teacher via an in-app form (~10–15 min per book), no login for teachers, single shared passcode for the leader/admin area.

- [x] Fox prototype built and reviewed — drove the revised book-detail-page layout (purpose-first, not year-level-first)
- [ ] Supabase project + schema
- [ ] Thin pilot app: search/filter + book detail, ~30-50 books
- [ ] Pilot test with real teacher search queries
- [ ] Leader/admin area: add book form, passcode gate, "Needs Review" queue
- [ ] AI enrichment pipeline (fills remaining trait/strategy/PRIDE/lens/teaching-idea gaps)
- [ ] School-wide launch

---

## 🛠️ Architecture Notes

- **Single Next.js app**, not a monorepo — `/app` (public teacher routes + passcode-gated admin routes) and `/lib` (database, enrichment, AI tagger). A two-app split was considered and rejected as premature for a solo-maintained school app.
- **No login for teachers** (decided 2026-07-27) — fully public app. Admin area uses a single shared passcode, not per-user accounts or OAuth.
- **No embeddings** for the curriculum reference PDFs — they're stored as structured JSON lookups (`reference-data/*.json`) instead, which is simpler and sufficient at this scale.
- Full planning-document review completed 2026-07-22 — confirmed the architecture, reconciled contradicting curriculum-framework lists across docs, and trimmed several premature abstractions (see `AI_PROJECT_HANDOFF_NEXT_STEPS.md` §11 for the full list).

---

## Notes

- Google Books API key is stored outside versioned docs (environment variable), never committed.
- Not to be confused with **Personal Collection** (129 books, Phill's own collection) — same project folder, explicitly lower priority than the School Library.
- Full readiness checklist (for external review, e.g. handing to an app designer): `APP_READINESS_CHECKLIST.md` in the project folder.
