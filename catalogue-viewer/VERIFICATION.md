# Verification — 9 September 2026

- The hosted viewer reads approved records directly from Supabase and refreshes every 15 seconds.
- After the approved *Alphabet Tree* revision, its card showed 17 writing, 8 reading, 2 PRIDE and 2 inquiry connections, with explanations for all 29 connections.
- Supabase independently returned 17 writing, 8 reading, 2 PRIDE, 2 inquiry and 8 teaching-idea records for the book with `teacher_reviewed` status.
- The previous six teaching ideas and removed Year 4 Presentation match remain stored but are hidden by their superseded `rejected` status.

## Initial interface checks — 7 September 2026

- Fresh read-only Supabase snapshot: 343 active books, 391 writing links, 260 reading links, zero PRIDE links, inquiry links and teaching ideas.
- Built viewer contains all 343 books, 90 with writing purposes and 54 with reading purposes. All 343 have blurbs; no connection has a book-specific explanation.
- Browser search for Banjo returns one book. Its detail shows the recorded blurb, four writing and four reading connections, sources/statuses and missing explanations.
- Browser Word Choice filter returns 65 books. Combined with Inferring it returns 45, checked independently against the snapshot.
- Determination and Social Responsibility return zero results with a clear empty-state explanation.
- Viewable-cover filter returns 221 books; missing-cover filter returns 122. A filename alone is not counted as a cover.
- Clear filters restores the catalogue. Desktop layout and actual covers visually inspected. Responsive CSS included; phone layout has not been separately tested.
- JavaScript syntax check passed. The live database and existing Fox review storage were not modified.

The local `data.json` remains a dated audit snapshot. The hosted viewer does not use it for curriculum content; it polls Supabase automatically.
