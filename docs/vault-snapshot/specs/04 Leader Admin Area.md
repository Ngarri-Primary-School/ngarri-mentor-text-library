---
title: "Feature Spec - Leader Admin Area"
type: feature-spec
tags: [chalkcode, ngarri, feature-spec, admin]
created: 2026-08-24
updated: 2026-08-24
status: draft
---

## Current reconciliation — 6 September 2026

The production admin workflow remains unbuilt. Local browser review has nine approvals and one omitted item, with outstanding revision requests. Notes do not automatically edit content. Preview approval is not live publication or authentication; preserve exact reviewed revisions and provide visible action feedback.

Read [[ChalkCode/Ngarri Mentor Text Library/Current State and Codex Handover]] first. This dated block supersedes conflicting historical statements below; earlier wording is retained for provenance.


# Feature Spec - Leader Admin Area

Migrated from `APP_DESIGN.md` (Leader App section) and `AI_PROJECT_HANDOFF_NEXT_STEPS.md` Step 11, 2026-08-24. The passcode-gated area where leading teachers add books and review AI suggestions.

## Problem

New books need to enter the library, and AI-suggested content needs human approval before teachers see it, without requiring a login system or ongoing developer involvement — a leading teacher must be able to do this unaided.

## Non-Goals

- Visual layout of admin screens — see [[ChalkCode/Ngarri Mentor Text Library/Design/04 Screen Specs]].
- The mechanics of how AI enrichment actually runs — see [[ChalkCode/Ngarri Mentor Text Library/specs/05 Ongoing Book Enrichment Pipeline]].
- Per-user accounts or roles — explicitly rejected (single shared passcode instead, see [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]], 2026-07-27).

## Behaviour Rules

**Access:** single shared passcode gate on `/admin` routes, checked server-side (never exposed client-side). Not per-user accounts, not OAuth.

**Add Book form:** required fields are Title and Author only. Optional: Illustrator, Year Level, Text Type, Blurb. Curriculum Links section lets the leader tick any writing trait/reading strategy/PRIDE value/inquiry lens that applies, or leave blank for AI (if a key is configured) or later manual entry. Buttons: Cancel, Next Book (save + clear for another entry), Finished (save + return home).

**After saving:** the book is saved immediately with leader-entered fields and is **immediately searchable by teachers**. The enrichment pipeline (if an AI key is configured — see [[ChalkCode/Ngarri Mentor Text Library/Working Contract]] rule 16) runs in the background. Only fields the leader explicitly entered are published immediately; every enriched/AI-suggested field goes to "Needs Review" and is never auto-published.

**Needs Review queue:** leader sees books awaiting review; for each, AI-suggested fields appear as editable tags. Leader can accept, remove, or edit any tag. "Approve & Publish" makes it live; "Save as Draft" keeps it in the queue.

**Bulk add:** repeated "Next Book" clicks queue multiple books; each enters the enrichment queue independently, no progress screen needed.

## Edge Cases

- A book saved with zero curriculum tags and no AI key configured — must still be fully searchable by teachers on its metadata (title, author, blurb) alone; missing tags are not a blocking error.
- Two leaders editing overlapping data around the same time — no per-user accounts means no natural conflict-owner; last-write-wins is acceptable at this scale but should be a deliberate choice, not an accident.
- An AI-suggested tag on a book that already has some teacher-entered tags — the review queue must make clear which is which; approving an AI suggestion must never silently overwrite an existing teacher-entered value.
- The passcode being guessed or shared beyond the intended leading-teacher group — no built-in mitigation beyond RLS write restrictions; treat as a known, accepted risk at this trust level (a small school, a small trusted group).

## Acceptance Checks

- The Add Book form is fully usable and produces a searchable book with zero AI key configured anywhere in the environment.
- No AI-suggested field ever reaches a teacher-facing view before an explicit "Approve & Publish" action.
- The passcode gate genuinely blocks writes without it — tested against direct API calls, not just the UI (per the launch-readiness checklist, Project Map Section 14).
- A leader can add a book start-to-finish in roughly 10-15 minutes for the common case (title, author, a few known trait ticks).
