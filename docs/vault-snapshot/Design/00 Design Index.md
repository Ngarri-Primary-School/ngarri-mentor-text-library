---
title: "Ngarri Mentor Text Library - Design Index"
type: design-index
tags: [chalkcode, ngarri, design]
created: 2026-08-24
updated: 2026-08-24
status: draft
---

## Current reconciliation — 6 September 2026

The user reaffirmed the saved Fox screenshots as the teacher-site design reference. The current local review form is a temporary workspace, not the replacement design. Retain documented purpose-first and responsive improvements.

Read [[ChalkCode/Ngarri Mentor Text Library/Current State and Codex Handover]] first. This dated block supersedes conflicting historical statements below; earlier wording is retained for provenance.


# Ngarri Mentor Text Library - Design Index

This folder is the source of truth for the app's visual design, interaction design, and component styling.

## Core Documents

- [[ChalkCode/Ngarri Mentor Text Library/Design/01 Visual Direction]] — typography, colour roles, the no-emoji rule (decided); exact palette and tokens (not yet decided)
- [[ChalkCode/Ngarri Mentor Text Library/Design/04 Screen Specs]] — Teacher App and Leader App screen composition, informed by the Fox mockup review
- `Design/assets/fox-prototype/` — screenshots of the live Fox prototype (closed and open accordion states) plus a full element-by-element inventory of what every piece of the page does. The only saved visual record of the prototype in the vault.

## What's Genuinely Decided vs. Not

Some real design decisions exist — this is not a blank stub. Typography (Fraunces/Lora/DM Sans), the no-emoji rule, semantic colour-role assignments, and full screen composition for both the Teacher App and Leader App are documented above, migrated faithfully from the project's earlier design work (`APP_DESIGN.md`, the Fox mockup review) on 2026-08-24.

What's genuinely **not** decided yet, and should not be invented in code:

- `02 Design Tokens` — exact colour hex values, spacing scale, shape tokens
- `03 Core Components` — formal reusable component specs beyond the screen-level descriptions above
- `06 Motion And Feedback States` — animation and interaction states
- `07 Asset Register` — icons/illustrations, if any

(`05 Gameplay And Rewards UI` from the ChalkCode template doesn't apply — this isn't a gamified app.)

## Handoff Rule

Any AI or human coding visual elements must read this index and the relevant documents above before implementation. If a needed design element isn't documented (an exact colour, a spacing value, an interaction state), pause and ask rather than inventing it — see [[ChalkCode/Ngarri Mentor Text Library/Working Contract]] rule 22.

## What Belongs Here

- visual direction, colours, typography, spacing and shape tokens (once decided)
- reusable component appearance
- screen layouts and states
- animation and feedback states
- asset register

## What Does Not Belong Here

- domain rules (source hierarchy, provenance model — see [[ChalkCode/Ngarri Mentor Text Library/Working Contract]])
- database schema or annotation logic (see [[ChalkCode/Ngarri Mentor Text Library/Architecture]])
- API secrets or credentials
