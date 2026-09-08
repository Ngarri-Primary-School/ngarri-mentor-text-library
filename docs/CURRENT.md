---
title: Ngarri Mentor Text Library - Current State and Codex Handover
type: project-handover
updated: 2026-09-08
status: active
---

# Current State and Codex Handover

This reconciliation records the work and user decisions made through 8 September 2026. Read it before the older project notes. Where a dated reconciliation block identifies a conflict, this note supersedes the historical statement; unaffected design and domain rules remain in effect. Repository documentation is the current source. The preserved Obsidian snapshot records provenance; it is not an independent editable copy.

## Current approved implementation — 8 September 2026

The complete-text picture-book pilot is approved for Crickwing, Night Tree, The Alphabet Tree, Little Blue and Little Yellow, and The Gruffalo. Their writing, reading, PRIDE, inquiry and teaching-idea records are stored in Supabase as `teacher_reviewed` and are visible in the public, read-only progress viewer at https://ngarri-mentor-library-progress.velveteen.chatgpt.site/.

The approved content hierarchy and book-page interaction are now specified in `docs/CONTENT-AND-DISPLAY-FORMAT.md`. In particular, writing and reading are organised by trait or strategy and then year level, with exact curriculum wording and a book-specific explanation. PRIDE and inquiry are concept-based without year-level subdivisions. Teaching ideas use structured classroom fields. All book-detail disclosures start closed and open progressively, including the blurb, trait or strategy, year-level record, value, lens and individual teaching idea.

This current specification supersedes older fixed 1–3 connection targets, generic teaching-idea allowances and any presentation note that conflicts with the approved pilot. Historical files under `archive/obsidian-vault-snapshot/` remain unchanged for provenance.

## What exists now

- Supabase project `dahilwcsbtstfbokbxws` was restored and inspected. Recorded recovery counts: 343 active books, 391 writing annotations, 260 reading annotations; 54 books with both, 36 writing-only, 253 with neither. These are the verified recovery snapshot, not a fresh live query on this documentation-update turn.
- All 651 existing writing/reading explanations were empty in the recovered snapshot. PRIDE, inquiry, teaching ideas, why-use bullets and teaching resources were empty. Preserve imported teacher/OzLit annotations; missing explanations are a separate task from new tagging.
- Six blurbs still needed review. The cover audit matched 221 catalogue filenames to recovered local covers; 122 lacked an exact local match. Older claims of complete cover readiness must not be relied upon.
- Original enrichment scripts, the claimed regression suite and the old 20-book outputs were not recovered. Earlier descriptions of a successful run are historical reports, not available evidence of an approved benchmark. Do not infer bulk permission or assume the remaining sample is 233 books. Recover the original or build a clearly labelled replacement benchmark and obtain its review before bulk work.
- A local functional Fox review workspace exists in `fox-working-page/`. It is not a production Next.js app, secure reviewer application or finished teacher-page design. It has no Supabase connection and publishes nothing.
- Fox is a separate calibration example, not a standalone book in the recovered 343-title catalogue. No new catalogue record was created.

## Teacher visibility and access

The user approved: AI-generated teaching content is visible only to reviewers until approved, then appears in the teacher library. Unreviewed suggestions must not influence teacher-facing purpose filters or appear as lesser-weight results.

The school Google Drive folder `Mentor Texts` (folder ID `15H0vElzelAVyq_okj427vUlD7IQeAbap`) now holds the selected full books. On 8 September 2026, Phill explicitly accepted its existing anyone-with-the-link sharing state because the book links are intended for teachers using the eventual website. Full book files remain outside GitHub and Supabase. Store only link metadata and provenance in the application. Do not change the sharing state without a new owner decision.

The applied access correction is migration `20260905205749`, `restrict_teacher_pilot_access`. The deployment report records SELECT-only client access where permitted, active-book parent checks and approved/imported status filtering. Teaching resources remain blocked to clients pending their policy. Unnecessary client grants were removed across fourteen tables; thirteen permit the intended SELECT access. The local isolated access tests passed 328 checks. See the actual deployment report and recovered schema; do not treat older blanket public-read descriptions or schema.sql references as current authority.

Production review access remains to be implemented. A local browser preview toggle and reviewer name field are not authentication. The historical shared-passcode design is not evidence of a completed secure implementation. Preserve the school-owned-key/spending-cap requirement; a coding assistant account does not settle the enrichment provider or authorise a paid run.

## Mentor-text content standard

Select all strong, distinct, evidenced connections a book supports. There is no requirement to cover every framework or year, and no three-connection maximum. Avoid padding and title-swappable generic routines.

Each recommendation should identify a particular passage, language choice, event or verified visual feature; explain why it demonstrates the selected skill or value particularly well; link exact school curriculum wording; and teach through that example before transferring learning to students' work. Keep source facts, quotations, interpretation and new activities distinguishable.

The supplied Fox PDF is four pages of retyped story text. All four pages were read and visually inspected. It contains no original illustrations; neither its layout nor its styling establishes the published book's typography. Book excerpts in the current fixture were checked against this copy. No full illustrated edition has been inspected.

The ten Fox candidates assess the original three writing connections, three reading connections, two PRIDE discussions and two inquiry lenses. Integrity is explicitly a counterexample discussion, not an assertion that a character embodies the value. Any future database representation must retain that distinction; do not automatically import it as a positive value tag.

## School curriculum and inquiry

The earlier ten-file structured reference set is now preserved in `reference-data/`. It contains the Ngarri writing throughlines, reading strategies, inquiry lenses and PRIDE values; a dated available-text inventory; and Oz Lit calibration plus its staged extraction records. `reference-data/README.md` defines the authority and limits of each file. These records are a verified working subset, not evidence that every useful curriculum or professional-reading source has been collected.

A read-only audit of the three user-nominated legacy project locations found 832 file copies, 485 unique hashes and 265 duplicate groups spanning locations. `reference-sources/README.md` records the result. Ten safe school-owned curriculum, values and inquiry originals are retained under `reference-sources/school-originals/`. Full books and commercial professional publications remain outside GitHub. The source folders were not changed.

The three newly supplied English documents provide 77 Foundation–Year 6 reference cells across eleven throughlines. Their four comprehension groups overlap with, but do not replace, the eleven recovered reading strategies. Keep exact wording, source versions and year columns. The newer source places the selected traits/motives/perspectives inference skill in Year 4, whereas the recovered Fox prototype used different Year 3 wording. Neither source is silently relabelled. These condensed school documents are not certified as verbatim official VCAA standards.

The five-page inquiry summary was read. The Power of Inquiry was extracted in full and relevant passages in chapters 3–5 closely reviewed, not read end to end. Use the school phase names flexibly and allow student questions to shape an inquiry. Books can provide an entry point rather than a compulsory full unit. Draft conceptual questions can be reviewed without waiting for an official Big Question list; never attribute AI-written questions to Ngarri as quotations.

## Saved teacher review and outstanding corrections

Phill's downloaded `fox-review-record.json` was verified: ten items, nine locally approved and Making Connections omitted. The original export has been copied without alteration to `codex-transfer-preparation/fox-review-record.json`.

All nine approvals include requests to remove PDF page-number references. Those comments are saved instructions for revision, not already-applied edits. Remove page numbers from teacher-facing prose while retaining precise locators in internal evidence records. Keep the original reviewed text and review history; do not silently rewrite a signed-off record.

Phill rejected the Making Connections example: the comprehension strategy concerns readers connecting the text with their own experience to deepen meaning, not characters making connections with each other. Rewrite its focus and example accordingly, and return it for review. It remains omitted and must not be reinstated under the other nine approvals.

The local UI now gives confirmation beside each approval button and distinguishes notes from direct text edits. Approved items display a disabled Approved button; editing reopens review. Saving a note does not automatically implement the request it contains. Exported records do not themselves update Supabase. Do not describe the nine approvals as live publication or as completion of the requested revisions.

## Visual direction

The saved `Design/assets/fox-prototype/` screenshots remain the teacher-site reference: book header, Why use this book panel, semantic colour roles, expandable curriculum connections and teaching-idea cards. Retain the documented purpose-first and responsive-layout improvements. No emoji in the app UI. The temporary text-heavy review form does not replace that design. Screenshot text is prototype content, not automatically verified book evidence; original errors included Kookaburra references, unsupported speech counts and other claims corrected during direct text review.

## Local locations

Current working files are in the ChatGPT project mirror:
`C:/Users/09187270/.codex/.chatgpt-projects/g-p-6a9b9af533e48191844e765db0f00f13`

Useful folders: `fox-working-page`, `fox-source-review`, `fox-content-review`, `curriculum-review-2026-09-06`, `mentor-access-change/deployed`, `archive/database-recovery-2026-09-05`, `mentor-handover-reconciled-2026-09-05`, and `codex-transfer-preparation`. Preserve source snapshots. Files under `sources/` are read-only synced material. These paths record the original source computer. Use repository-relative files after checking out the school repository; no dedicated Codex project has been registered yet.

This documentation vault is locally accessible at:
`C:/Users/09187270/iCloudDrive/iCloud~md~obsidian/ChalkCode/Ngarri Mentor Text Library`

Additional school documents:
`C:/Users/09187270/iCloudDrive/iCloud~md~obsidian/Education/Curriculum/Ngarri Documents`

Book PDFs:
`C:/Users/09187270/OneDrive - Department of Education/Documents/Ngarri/Curriculum/Literacy/Mentor Texts`

Fox text copy: `Margaret Wild/Fox/Fox Margaret Wild.pdf` under that book-PDF folder. Earlier project/data files also occur under the separate `Curriculum/Mentor Texts` path without Literacy; do not conflate the locations.

## Next development action

The user selected the private school repository https://github.com/Ngarri-Primary-School/ngarri-mentor-text-library as the shared project destination. The transfer preserves the old Obsidian notes under archive/obsidian-vault-snapshot; those are historical snapshots. This file is the current editable handover, and repository documentation is the source for future project changes. Do not maintain competing editable copies in the old vault. The local transfer staging area is packaging only.

The repeatable enrichment support is now defined in `docs/ENRICHMENT-PIPELINE.md`, implemented by `scripts/mentor_pipeline.py`, and guided by the repository skill at `.codex/skills/ngarri-mentor-text-enrichment/SKILL.md`. New batches begin with Codex naming three to five books and pausing until the user supplies complete texts in the restricted school Google Drive and Codex verifies access. Every new draft includes text type, genre and a classification rationale.

The first new batch has been selected: *Dingo*, *Owl Moon*, *The Boy Who Loved Words*, *The Important Book* and *Whoever You Are*. Their files are now in the school Drive and matching school-held local copies have been opened for complete-text analysis. *Dingo* requires visual page inspection because its embedded PDF font corrupts programmatic extraction. These books broaden the benchmark across narrative nonfiction, lyrical voice and imagery, explicit word choice, patterned description, and PRIDE/inquiry themes.

The five previously approved pilot books predate the classification requirement. Their existing content approval remains valid, but their text type and genre still require evidence-based classification and teacher review before those fields are treated as approved.

On 8 September 2026, Phill approved the proposed text type and genre classifications for the five pilot books and the five selected next-batch books. The review record is `reviews/text-type-and-genre.ai-draft.json`; it retains its original draft filename for provenance, but its internal status and all ten records are `teacher_reviewed`. The approved values are stored in the ten matching Supabase book rows and were verified after update.

On 9 September 2026, Phill approved the content-authoring guide with two additions: it must name the exact Ngarri reference files, and teaching ideas must use relevant installed education skills or the available skill-discovery workflow. The canonical guide is `docs/CONTENT-AUTHORING-GUIDE.md`; the detailed rules are also reflected in `docs/CONTENT-AND-DISPLAY-FORMAT.md` and `.codex/skills/ngarri-mentor-text-enrichment/SKILL.md`.

The remaining pilot books are being revised one at a time, with teacher approval between books. *The Alphabet Tree* revision in `reviews/the-alphabet-tree.revision.ai-draft.md` was approved and published on 9 September 2026. Its live Supabase record now contains 17 writing, 8 reading, 2 PRIDE, 2 inquiry and 8 teaching-idea records. The public viewer was verified against the live connection and showed all 29 approved connections. The earlier six teaching ideas and removed Year 4 Presentation match remain hidden as superseded records.

The remaining order is *Night Tree*, *Little Blue and Little Yellow*, then *The Gruffalo*. *Crickwing* remains the quality model. Prepare *Night Tree* as a separate `ai_suggested` draft and obtain Phill's approval before publishing it.

Keep all other new material `ai_suggested` until Phill reviews it; do not expose it in teacher-facing pages or filters before approval. No paid generation or bulk enrichment is authorised by the transfer. Steve's invitation and school-account Codex connection remain pending. Supabase and hosting ownership require their own handover.

