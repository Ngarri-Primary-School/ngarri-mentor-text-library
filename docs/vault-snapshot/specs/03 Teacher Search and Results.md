---
title: "Feature Spec - Teacher Search and Results"
type: feature-spec
tags: [chalkcode, ngarri, feature-spec, search]
created: 2026-08-24
updated: 2026-08-24
status: draft
---

## Current reconciliation — 6 September 2026

The unreviewed-content edge case below is now decided: AI suggestions stay out of teacher-facing content and purpose matching until approved. Imported trusted annotations remain under the deployed access rules. Do not expose draft suggestions with a lower visual weight.

Read [[ChalkCode/Ngarri Mentor Text Library/Current State and Codex Handover]] first. This dated block supersedes conflicting historical statements below; earlier wording is retained for provenance.


# Feature Spec - Teacher Search and Results

Migrated from `AI_PROJECT_HANDOFF_NEXT_STEPS.md` §5, 2026-08-24. The core teacher-facing search behaviour — the app's primary purpose.

## Problem

Teachers need to find useful mentor texts starting from a teaching purpose ("I want to teach Word Choice"), not from a year-level catalogue browse. The search and result display must make that possible quickly, without exposing internal data-quality mechanics.

## Non-Goals

- The book detail page itself — see [[ChalkCode/Ngarri Mentor Text Library/specs/02 Book Detail Page Field Model]].
- Admin/leader search-with-edit-capability — see [[ChalkCode/Ngarri Mentor Text Library/specs/04 Leader Admin Area]].
- Visual styling of the search screen — see [[ChalkCode/Ngarri Mentor Text Library/Design/04 Screen Specs]].

## Behaviour Rules

**Primary filters** (purpose-first): Writing Trait (7), Reading Strategy (11), PRIDE Value (5), Inquiry Lens (4), text type/genre, Australian/First Nations/special categories where available.

**Secondary filters:** year level range, format, author, resource availability, cover available/missing.

**Filter logic:** within one filter, OR (Year 3 + Year 4 shows books for either); across filters, AND (Year 3/4 + Inferring shows books satisfying both).

**Result cards** must show: title, author, cover or an intentional no-cover fallback, short blurb preview, matched purpose tags, year suitability, a short "why use this book?" summary.

**Provenance rule:** never show annotation source/provenance labels (`ozlit`, `ai_suggested`, `teacher_spreadsheet`) to ordinary teachers — internal only, would add confusing cognitive load with no benefit to the search task.

## Edge Cases

- A search with zero matching results for a valid, sensible combination of filters — should suggest broadening (e.g. drop the secondary year-level filter) rather than a bare empty state.
- A book matching the purpose filter but still `ai_suggested` and unreviewed — decide whether it appears in results at all, or appears with lower visual weight, before Pass 1/2 data goes live to teachers (this is currently undecided — see Project Map Hard Questions).
- A book with no cover — must not look broken or lower-quality; the no-cover fallback should be a deliberate, polished state (per Project Map Section 13).
- Multiple traits/strategies matched on one book — result card must show matched tags without becoming visually cluttered.

## Acceptance Checks

- A teacher can filter by any single primary-category value and get sensible results without touching a secondary filter.
- A teacher can combine a primary purpose filter with a year-level filter and get the AND-combined result set.
- No result card or detail view ever renders a raw `source_type`/`status` value as visible teacher-facing text.
- Success criterion (from the original roadmap, Section 10): a teacher can find a useful collection of books for a stated teaching purpose in under a minute.
