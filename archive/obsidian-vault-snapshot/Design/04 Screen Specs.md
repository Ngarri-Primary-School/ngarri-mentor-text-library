---
title: "Ngarri Mentor Text Library - Screen Specs"
type: design-doc
tags: [chalkcode, ngarri, design, screen-specs]
created: 2026-08-24
updated: 2026-08-24
status: draft
---

## Current reconciliation — 6 September 2026

The teacher-page composition remains the target. The local approval form does not implement that final composition or production authentication. Page numbers should be internal evidence details rather than teacher-facing prose; the user request is recorded and implementation is pending.

Read [[ChalkCode/Ngarri Mentor Text Library/Current State and Codex Handover]] first. This dated block supersedes conflicting historical statements below; earlier wording is retained for provenance.


# Ngarri Mentor Text Library - Screen Specs

Migrated from `APP_DESIGN.md`, 2026-08-24, incorporating the Fox mockup review findings (see [[ChalkCode/Ngarri Mentor Text Library/Research Notes]]). These are decided layouts/composition, informal in the sense that no pixel-level design tokens exist yet (see [[ChalkCode/Ngarri Mentor Text Library/Design/01 Visual Direction]]) — but the structure itself is real design direction, not a placeholder.

## Teacher App

### Home / Search Screen

Purpose-first filter/search bar across the top; books displayed as a scrollable list below. See [[ChalkCode/Ngarri Mentor Text Library/specs/03 Teacher Search and Results]] for filter behaviour rules. Each result card: cover thumbnail (left), title, author, blurb snippet, matched purpose tags as coloured chips, year suitability as a secondary chip, short "why use this book?" summary when available. No source/provenance labels ever shown.

### Book Detail Page

Reference mockup: the Fox prototype's `book-detail-v5.html`, revised per the mockup review. See `Design/assets/fox-prototype/` for screenshots of every section in both closed and open states, plus a full element-by-element inventory of what each piece of the page does.

**Hero (full width, sticky — doesn't scroll):**
1. Book cover (left) — natural aspect ratio, no fixed height, no cropping.
2. Book information (centre, flex: 1) — title (Fraunces, large), author, illustrator/publisher/year, tag row (Year Level/Text Type/Genre/Australian), blurb below the tags.
3. "Why use this book?" panel (right, ~260px) — green-tinted, full hero height, 3-5 AI-generated bullets (coloured dots, no checkmarks or emoji).

**Main column (scrollable):**

*Teaching Purposes — first section below the hero.* Directly resolves the Fox review's "book-detail-first, not purpose-first" critique: shows the strongest matched uses across Writing Traits, Reading Strategies, PRIDE Values, and Inquiry Lenses immediately, each with a short "In this book" evidence statement and year suitability. This answers "why would I use this book?" before anything else.

*Curriculum Detail — expandable section below Teaching Purposes,* not the first thing teachers navigate. Writing trait cards: green header bar with trait name + year range badge (clickable to collapse/expand, no icon/emoji), body has a Throughline section (verbatim KU/KS, labelled and attributed) plus an "In this book" callout (green left-border panel, AI-written). Cards open by default. Reading strategies, PRIDE values (amber chips), and Inquiry Lenses (pink chips) follow the same "In this book" pattern.

*Teaching Ideas — 3-column card grid below Curriculum Detail.* Each card: coloured dot + title, description, metadata footer (time estimate, grouping, difficulty chip). "View more teaching ideas" button below the grid.

*"Save to My Library" bar (bottom of main column)* — plain text button, no heart emoji. Confirmed out of core v1 scope (see [[ChalkCode/Ngarri Mentor Text Library/Decisions Log]], 2026-07-22) but the UI slot is reserved.

**Sidebar (right, 360px, scrollable with main content) — deliberately lower visual priority than the main teaching evidence,** per the Fox review's "sidebar competes too early" finding:

*Teaching Resources (top)* — file-type text badge + title + description, Download button. No emoji icons, no author attribution shown to teachers.

*Related Books (below resources)* — vertical list, cover thumbnail (50px, 2:3 ratio) + title + author, grouped "More by [Author]" / "Similar — [tags]", "View more like this" link.

**Accessibility (from the Fox review):** accordion controls must be real buttons with accessible expanded/collapsed states, headings must be real heading elements, not generic styled divs.

**Mobile:** the Fox prototype's mobile layout broke at 390px (cover became extremely wide and cropped, narrow awkward columns) — the real build needs a deliberate mobile/tablet layout, even though desktop is the primary target.

## Leader App

### Home Screen

Three action tiles: **+ Add New Book** (primary, prominent), **Browse & Edit Books** (same search view as teachers, with edit capability), **Needs Review** (badge count — books awaiting leader approval). Library stats overview: total books / fully annotated / blurb only / needs review count.

### Add Book Form, Needs Review Flow, Bulk Add

See [[ChalkCode/Ngarri Mentor Text Library/specs/04 Leader Admin Area]] for full behaviour rules. Visually: Add Book form has required fields (Title, Author) at top, optional fields below, a Curriculum Links tick-section, and Cancel/Next Book/Finished buttons. Needs Review shows AI-suggested fields as editable tags per book (same visual pattern as the Curriculum Detail trait cards on the teacher-facing page), with Approve & Publish / Save as Draft actions.
