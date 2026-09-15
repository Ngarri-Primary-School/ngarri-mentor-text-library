# Complete-text picture-book pilot approval

Approval date: 8 September 2026  
Approved by: Phill  
Live viewer: https://ngarri-mentor-library-progress.velveteen.chatgpt.site/

## Approved books

| Book | Writing | Reading | PRIDE | Inquiry | Teaching ideas |
|---|---:|---:|---:|---:|---:|
| Crickwing | 16 | 9 | 3 | 3 | 6 |
| Night Tree | 11 | 5 | 2 | 2 | 6 |
| The Alphabet Tree | 17 | 8 | 2 | 2 | 8 |
| Little Blue and Little Yellow | 11 | 7 | 2 | 2 | 6 |
| The Gruffalo | 12 | 7 | 1 | 1 | 6 |

All records above are stored in Supabase with `teacher_reviewed` status. The shared-password progress viewer reads approved data from Supabase and refreshes every 15 seconds.

The canonical authoring, database and page-display rules established by this approval are recorded in `docs/CONTENT-AND-DISPLAY-FORMAT.md`.

## Review rules confirmed by this pilot

- Use only the strongest connections supported by the complete book.
- Writing and reading entries are organised by focus, then year level from lowest to highest.
- Each year-level entry contains one exact Key Understanding, one matching Key Skill and a book-specific explanation.
- PRIDE values and inquiry lenses are whole-book concepts and do not require year levels.
- Teaching ideas identify where to look, the learning focus, a teaching sequence, student application and observable learning.
- AI suggestions remain private until a reviewer approves them.
- Preserve complete-text sources and source references; do not place copyrighted full texts in the public repository or website.
- Display book details progressively. The blurb sits in the header; writing and reading first open by trait or strategy and then by year level; PRIDE and inquiry open directly to their connection; teaching ideas open independently.

## Night Tree Visualising decision

The current Ngarri reading source has no dedicated Visualising Key Understanding or Key Skill. Its database reference groups Visualising with wording for neighbouring strategies, which must not be relabelled as Visualising curriculum.

For Night Tree, the approved Visualising entry instead uses the matching understanding from *Strategies That Work*, Chapter 9: proficient readers create sensory images to improve comprehension. The entry intentionally has no Key Skill and identifies the professional-reading source in Supabase and on the shared progress page.

## Canonical supporting files

The source project retains:

- `reviews/20-book-trial-first-pass/REMAINING-PICTURE-BOOK-REVIEW.md`
- `reviews/20-book-trial-first-pass/remaining-picture-book-records.ai-draft.json`
- `reviews/20-book-trial-first-pass/build_remaining_picture_book_records.py`
- `reviews/20-book-trial-first-pass/PICTURE-BOOK-PILOT-DRAFT.md`

The `.ai-draft.json` name records provenance: the content began as AI-generated suggestions. Supabase review fields record the later human approval.

