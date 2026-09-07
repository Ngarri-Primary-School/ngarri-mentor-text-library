# Verification — 7 September 2026

- Fresh read-only Supabase snapshot: 343 active books, 391 writing links, 260 reading links, zero PRIDE links, inquiry links and teaching ideas.
- Built viewer contains all 343 books, 90 with writing purposes and 54 with reading purposes. All 343 have blurbs; no connection has a book-specific explanation.
- Browser search for Banjo returns one book. Its detail shows the recorded blurb, four writing and four reading connections, sources/statuses and missing explanations.
- Browser Word Choice filter returns 65 books. Combined with Inferring it returns 45, checked independently against the snapshot.
- Determination and Social Responsibility return zero results with a clear empty-state explanation.
- Viewable-cover filter returns 221 books; missing-cover filter returns 122. A filename alone is not counted as a cover.
- Clear filters restores the catalogue. Desktop layout and actual covers visually inspected. Responsive CSS included; phone layout has not been separately tested.
- JavaScript syntax check passed. The live database and existing Fox review storage were not modified.

This is a dated local inspection tool. Refreshing requires a fresh authorised snapshot; it does not poll Supabase automatically.
