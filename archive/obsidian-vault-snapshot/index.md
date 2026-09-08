---
title: Ngarri Mentor Text Library - AI Project Index
type: ai-project-index
tags: [chalkcode, ngarri, supabase, nextjs, vercel, education, curriculum, ai-project]
created: 2026-08-24
updated: 2026-08-24
status: active
---

## Current reconciliation — 6 September 2026

Start with the linked current handover. The old pickup instructions below are superseded: the prior scripts and sample outputs remain unrecovered, and the next action is a preserved Codex transfer, not bulk enrichment.

Read [[ChalkCode/Ngarri Mentor Text Library/Current State and Codex Handover]] first. This dated block supersedes conflicting historical statements below; earlier wording is retained for provenance.


# Ngarri Mentor Text Library - AI Project Index

This folder contains **all** planning, instruction, rules, and contract documents for the Ngarri Mentor Text Library app, following the ChalkCode project rules template.

## If You're Picking This Up Right Now

**The 20-book spot-check is done (2026-08-25) — done with no API key at all.** Claude researched the sample itself via web search and wrote real, validator-passed output. Next action:

1. **Phill reviews `School Library/Migration/ai_trait_spot_check.csv`** for evidence quality — same human gate the spec always required. See [[ChalkCode/Ngarri Mentor Text Library/specs/01 AI Enrichment Pass 1]] for the full method and results (39 writing-trait tags, 10 reading-strategy tags, 20 books, zero validation warnings).
2. Once approved, the remaining ~233 books need either:
   - **The same manual approach repeated** (no API key, but slow — many research turns), or
   - **A real API key for `--mode bulk`** (fast, ~$10-20). Two open questions affect this: (a) Anthropic vs. the school's OpenAI/ChatGPT Pro access — see Project Map Hard Questions — and (b) if Anthropic, a disposable personal key is fine for this one-time step (`export ANTHROPIC_API_KEY="..."`, the `anthropic` Python package is already installed).
   ```
   cd "/Users/phillcantone/Library/Mobile Documents/com~apple~CloudDocs/Family/Phill/AI Coding/Mentor Texts/School Library/Migration" && python3 enrich_traits.py --mode bulk
   ```
3. Then `python3 enrich_traits.py --mode sqlgen`, apply the resulting SQL via the Supabase MCP `apply_migration` tool, and verify row counts.
4. After that, Pass 1 is done and Project Map Section 10 (Pilot App) is next.

Full detail on every other decision, rule, and open question lives in the files below — this section only exists so nobody has to reconstruct "what do I actually do next" from the rest of the vault.

## Relationship to the Project Folder

**As of 2026-08-24, this Obsidian folder holds every instruction document** — the project folder (`/Users/phillcantone/Library/Mobile Documents/com~apple~CloudDocs/Family/Phill/AI Coding/Mentor Texts/`) holds only data and code (Supabase migration scripts, CSVs, covers, `schema.sql`, `reference-data/*.json`). The governance docs written there on 2026-08-03 (`AI_CONTRACT.md`, `ARCHITECTURE.md`, `DECISIONS.md`, `PROJECT_MAP.md`, `specs/`) and the pre-existing product/roadmap docs (`README.md`, `APP_DESIGN.md`, `BOOK_DETAIL_FIELDS.md`, `PROJECT_OVERVIEW.md`, `AI_PROJECT_HANDOFF_NEXT_STEPS.md`, `APP_READINESS_CHECKLIST.md`) have been retired from that folder — their content is fully migrated here, not summarised or dropped. See [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]], 2026-08-24 entry.

The project folder keeps a minimal `CLAUDE.md` stub that points back to this folder, so a Claude Code session starting there still auto-loads a pointer to the real rules.

The existing narrative dashboard note, [[ChalkCode/Ngarri Mentor Text Library/Ngarri Mentor Text Library|Ngarri Mentor Text Library]], stays as the quick-status summary linked from the ChalkCode `README.md`.

## Current Phase

Phase 1 (one-time data setup) complete as of 2026-07-30: 343 canonical books, verified blurbs, real covers, teacher-spreadsheet and OzLit annotations matched, imported, and live in Supabase. Phase 2 (the live app) has not started. The immediate next step — AI Enrichment Pass 1 for the 253 books with no writing-trait/reading-strategy data — is built and offline-tested but paused at a human spot-check gate (see [[ChalkCode/Ngarri Mentor Text Library/Project Map]] Section 9).

## Core Files

| File | Purpose |
|---|---|
| [[ChalkCode/Ngarri Mentor Text Library/Working Contract]] | Non-negotiable rules for AI and human work on the project |
| [[ChalkCode/Ngarri Mentor Text Library/Project Map]] | Product purpose, domains, boundaries, and the full 14-step build plan with real status |
| [[ChalkCode/Ngarri Mentor Text Library/Architecture]] | System design, live Supabase layout, source hierarchies, script pipeline |
| [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]] | Persistent record of product and architecture decisions |
| [[ChalkCode/Ngarri Mentor Text Library/Research Notes]] | Source-backed research behind the curriculum framework and enrichment rules |
| [[ChalkCode/Ngarri Mentor Text Library/Design/00 Design Index]] | Visual direction and screen specs — partially decided, see the index for what's real vs. open |

## Feature Specs

| Spec | Purpose |
|---|---|
| [[ChalkCode/Ngarri Mentor Text Library/specs/01 AI Enrichment Pass 1]] | One-time writing-trait/reading-strategy AI enrichment for the 253 gap books |
| [[ChalkCode/Ngarri Mentor Text Library/specs/02 Book Detail Page Field Model]] | Field-by-field data and tagging-selection rules for the book detail page |
| [[ChalkCode/Ngarri Mentor Text Library/specs/03 Teacher Search and Results]] | Purpose-first search, filters, and result cards |
| [[ChalkCode/Ngarri Mentor Text Library/specs/04 Leader Admin Area]] | Add-book form, passcode gate, AI-suggestion review queue |
| [[ChalkCode/Ngarri Mentor Text Library/specs/05 Ongoing Book Enrichment Pipeline]] | The future in-app per-book enrichment pipeline (distinct from the one-time Pass 1 migration) |

## Working Principle

Before coding or making substantial design decisions, AI should read:

1. [[ChalkCode/Ngarri Mentor Text Library/Working Contract]]
2. [[ChalkCode/Ngarri Mentor Text Library/Project Map]]
3. [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]]
4. [[ChalkCode/Ngarri Mentor Text Library/Architecture]]
5. The relevant feature spec under `specs/`
6. For visual implementation, [[ChalkCode/Ngarri Mentor Text Library/Design/00 Design Index]] and the relevant design document

This follows the Codex anti-rot workflow: persistent rules first, short project map, feature specs before code, small implementation slices, tests and documentation gates.
