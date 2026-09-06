---
title: "Ngarri Mentor Text Library - Visual Direction"
type: design-doc
tags: [chalkcode, ngarri, design, visual-direction]
created: 2026-08-24
updated: 2026-08-24
status: draft
---

# Ngarri Mentor Text Library - Visual Direction

Migrated from `APP_DESIGN.md`, 2026-08-24. What's actually decided vs. still open — see [[ChalkCode/Ngarri Mentor Text Library/Design/00 Design Index]] for the full picture.

## Decided

**Typography:**
- Book title: Fraunces (serif), large
- Blurb text and throughline KU/KS quotes: Lora (serif), italic
- UI labels, chips, body text: DM Sans

**Hard rule — no emoji anywhere in the UI.** No emoji characters, no emoji-inspired icons. Use coloured dots, text badges, or plain typographic elements instead. This applies to every screen, including chip labels, buttons ("Save to My Library" is plain text, no heart icon), and metadata badges.

**Colour roles** (semantic assignment decided; exact hex palette not yet chosen):
- Blue: Year Level tags
- Orange: Text Type tags
- Green: Genre tags, and the "Why use this book?" panel background tint
- Amber: Australian-text-only tag
- Purple: Reading Strategy chips
- Amber (again): School Values / PRIDE chips
- Pink: Inquiry Lens chips
- Difficulty chips (teaching ideas): Easy = green, Medium = orange, Discussion = blue/purple

**Device target:** desktop-first, responsive for occasional tablet use (per the Fox mockup review, mobile needs a genuinely deliberate layout, not an afterthought — see [[ChalkCode/Ngarri Mentor Text Library/Research Notes]]).

## Not Yet Decided

- Exact colour palette (hex values) — deferred.
- Spacing/sizing scale, shape tokens, formal design tokens file.
- Motion and feedback states.
- Asset register (icons, illustrations if any).

Do not invent these in code — see [[ChalkCode/Ngarri Mentor Text Library/Working Contract]] rule 22.
