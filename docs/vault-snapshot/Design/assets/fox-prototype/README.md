---
title: "Fox Prototype - Screenshot Archive"
type: design-asset-index
tags: [chalkcode, ngarri, design, fox-prototype, screenshots]
created: 2026-08-24
updated: 2026-08-24
status: active
---

# Fox Prototype - Screenshot Archive

Captured 2026-08-24 from the live prototype at [fox-deploy-olive.vercel.app](https://fox-deploy-olive.vercel.app) — the only visual record of it saved anywhere in the vault (it had only ever been referenced as a link before this). If that Vercel deployment ever goes offline, this folder is what's left.

**Known limitation:** cover art and other cross-origin images render blank (grey placeholder box) in these captures — a tool limitation of the capture method (html2canvas can't read cross-origin canvas pixels without CORS headers), not a real bug in the prototype. Everything else — layout, text, colours, chip styling — is accurate.

**Missing:** a saved screenshot of the broken mobile (375px) layout. Three capture attempts were corrupted in transmission; the finding itself (cover image blows up to fill the viewport width, extremely cropped) is documented in [[ChalkCode/Ngarri Mentor Text Library/Research Notes]] and is directly visible if you reopen the live prototype and narrow the browser.

## Screenshots

| File | State | Shows |
|---|---|---|
| `01-hero-and-collapsed-sections.jpg` | Default / closed | The sticky hero plus every section collapsed — the page as a teacher first sees it |
| `02-writing-trait-expanded-year3.jpg` | Open | "Voice / Audience" trait card expanded, "Year 3" row expanded — full KU/KS + "In this book" detail |
| `03-pride-and-inquiry-lens-expanded.jpg` | Open | "Determination" (PRIDE) and "Identity, Creativity & Wellbeing" (Inquiry Lens) cards both expanded |
| `04-teaching-idea-expanded.jpg` | Open | "Spotlight Writing" teaching-idea card expanded, showing description + metadata footer |
| `05-reading-strategy-expanded-year3.jpg` | Open | "Inferring" strategy card expanded, "Year 3" row expanded — confirms the same card pattern as writing traits, in purple |

See [[ChalkCode/Ngarri Mentor Text Library/Design/04 Screen Specs]] for the full page structure these screenshots illustrate, and the element-by-element breakdown below.

## Element Inventory — What Each Piece of the Page Does

Organised top to bottom, matching the screenshots above.

### Hero (sticky — stays pinned while the rest scrolls)

| Element | Job |
|---|---|
| Cover image | Visual identification of the book at a glance |
| Title ("Fox") | Primary identifier, Fraunces serif for visual weight |
| Author / illustrator line | Attribution |
| Publisher, year line | Metadata context (edition, currency) |
| Tag row (Year 3-6 / Picture Book / Narrative / Australian) | Fast filtering-relevant facts — the same categories used in search |
| Blurb (blue left-border panel) | Lets a teacher confirm this is the right book without opening a catalogue elsewhere |
| "Why use this book?" panel (green, right) | The single most important element on the page — answers "why would I use this book?" in 3-5 bullets before the teacher reads anything else. Directly resolves the original Fox-review finding that the page was book-detail-first rather than purpose-first |

### Mentor Text Traits (green section)

| Element | Job |
|---|---|
| Section header + intro line | Orients the teacher: this section is about writing craft, not reading comprehension |
| Trait bar (e.g. "Voice / Audience") | Collapsed by default — one bar per tagged trait, click to expand |
| Year-level row inside a trait (e.g. "Year 3") | Second-level collapse — the specific curriculum year this evidence applies to |
| "Key Understanding:" / "Key Skill:" text | Verbatim curriculum language, attributed to its source throughline — never AI-paraphrased (see [[ChalkCode/Ngarri Mentor Text Library/Working Contract]] rule 8) |
| Attribution line (e.g. "Year 3 Audience/Voice Throughline") | Traceability back to the source curriculum document |
| "In this book:" callout (green tint) | The only AI-authored text in this card — explains how this specific book demonstrates the verbatim skill above it |

### Reading Comprehension Strategies (purple section)

Identical structure and job to Mentor Text Traits, just for reading strategies instead of writing traits, coloured purple instead of green, and sourced from "Ngarri PS English Curriculum" instead of the Writing Throughlines document.

### PRIDE Values (amber section)

| Element | Job |
|---|---|
| Value bar (e.g. "Determination") | Collapsed by default, one bar per tagged value |
| Value definition quote | Verbatim from Ngarri's PRIDE Values document |
| "In this book:" callout | Must cite a specific character decision or story moment — never a vague theme (see the selection rule in [[ChalkCode/Ngarri Mentor Text Library/specs/02 Book Detail Page Field Model]]) |

### Inquiry Lenses (pink section)

Same structure as PRIDE Values. The definition text states the lens's Big Question territory; the "In this book" callout must connect to a specific Big Question, not a general theme.

### Teaching Ideas (3-column card grid)

| Element | Job |
|---|---|
| Coloured dot + title | Quick visual scan of available ideas, colour links back to the trait/strategy it supports |
| Description (collapsed by default, click to expand) | The actual classroom activity |
| Metadata footer (time · grouping · difficulty chip) | Lets a teacher filter ideas by how much time/setup they have before reading the full description |
| "View all teaching ideas" button | Escape hatch if more ideas exist than the 3 shown |

### "Save to My Library" bar

Plain text button, explicitly out of core v1 scope (see [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]], 2026-07-22) — the UI slot is reserved but not a launch requirement.

### Sidebar (scrolls with the main column, not independently — a deliberate lower-priority placement per the original Fox review's "sidebar competes too early" finding)

| Element | Job |
|---|---|
| Resources cards (PDF/DOC badge + title + description + Open button) | Publisher/teacher-made materials, kept visually quieter than the main teaching evidence |
| Related Books, "Same Author" group | Cross-navigation by author |
| Related Books, "Similar Themes" / "Reading strategy (X)" group | Cross-navigation by shared teaching purpose — reinforces the purpose-first model even in a secondary panel |
