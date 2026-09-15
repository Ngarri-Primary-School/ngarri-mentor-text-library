# Book enrichment pipeline

Updated: 10 September 2026
Status: approved post-trial workflow; script implemented; five-book trial complete

## Purpose

This pipeline turns a verified complete book into a structured draft for teacher review. It combines deterministic checks with Codex's literary and pedagogical judgement. The five completed trial books remain the quality benchmark: *Crickwing*, *The Alphabet Tree*, *Night Tree*, *Little Blue and Little Yellow* and *The Gruffalo*.

## The intake pause

At the beginning of each batch, Codex reviews the catalogue and names one to three proposed books, with a short selection reason for each. It tells the user before beginning so the user can confirm that the complete books are in the school Google Drive. It records the agreed batch using `scripts/mentor_pipeline.py new-batch` and pauses until access is confirmed.

A batch is only a short forward plan. Codex completes one book, presents the entire `ai_suggested` draft and waits for teacher approval before publishing it or beginning the next book. The teacher may reorder, replace or stop the remaining books at every approval point.

The user places school-held copies in the school Google Drive folder. Codex resumes a book only after it can locate the complete file and verify that the book can be read. It records the Drive file identifier, verification time and source fingerprint in an ignored local batch record. Full PDFs, page images and newly extracted working copies remain outside GitHub. An approved text-only transcription may also be consulted from the private continuity archive under `restricted-reference/`, but it does not replace checking the complete school copy and available illustrations.

The same restricted Drive file can support an **Open picture book PDF** link in the shared-password progress viewer. A matching Drive-hosted **Open text-only PDF** link may also be shown after its transcript has been checked. Google Drive permissions remain authoritative; do not embed a book file in the website, GitHub or Supabase.

## Find text before extracting it

For each selected book, use this order:

1. Search `restricted-reference/jimk-mentor-texts/` for an existing title transcription.
2. Search the book's Drive folder and `Text Extractions - Restricted/` for an existing checked transcript, searchable text-only PDF and review notes.
3. Check whether the complete Drive PDF already has a reliable searchable text layer.
4. Extract text from that PDF only when no suitable checked text exists.
5. Use OCR on scanned pages only as the last option.

An existing JimK document saves extraction work, but its edition, completeness and accuracy are not assumed. Compare it with the complete school copy, check the beginning, middle and ending, and verify every passage used in the proposed content. Record omissions or wording differences. Visually inspect every illustration used as evidence.

When a JimK transcription is suitable, use the verified text as the starting point for the book's linkable resources. Prepare a clean transcript, searchable text-only PDF and concise transcription-review notes in the appropriate Drive extraction folder. Do not expose the private GitHub source file itself as a website download. The authenticated website may link to the original school PDF and the Drive-hosted text-only PDF using approved Drive metadata.

## Per-book preflight

Before writing content, confirm and record:

- complete school book access and its Drive link;
- existing JimK or Drive text resources, or the extraction method required;
- transcription checks and any edition differences;
- title, author, illustrator, publication details, text type, genre and year band;
- whether the displayed cover exists, belongs to the correct edition and renders properly; and
- availability of both the original-book link and text-only PDF link for the authenticated site.

Replace or correct a cover only from an authorised source. Do not infer visual evidence from a cover alone.

## Required book classification

Every new or revisited book record must establish:

- `text_type`: one broad form or communicative purpose;
- `genres`: one or more specific genres; and
- `classification_rationale`: a short evidence-based explanation.

Text type and genre are separate. For example, a book might have `text_type: narrative` and `genres: [cumulative tale, quest narrative]`. Classification is part of teacher review.

The existing `books` table already contains nullable `text_type` and `genre` fields. Before production use, agree how multiple genres will be represented and prepare a reviewable migration if a separate genre relationship is preferred. Do not overwrite existing values in bulk.

## Script responsibilities

`scripts/mentor_pipeline.py` provides these commands:

- `new-batch`: records the selected books and prints the required pause;
- `register-source`: records a Drive source only after Codex has checked access;
- `extract-text`: creates a line-addressable TXT working copy and source hash;
- `make-draft`: creates the standard draft structure after source verification; and
- `validate`: checks required fields, exact curriculum wording, provenance and `ai_suggested` status.

Example:

```powershell
python scripts/mentor_pipeline.py new-batch `
  --books .mentor-work/candidates.json `
  --batch-id 2026-09-batch-02 `
  --count 3 `
  --out .mentor-work/2026-09-batch-02.json
```

Use Codex's bundled Python runtime if `python` is not configured. PDF extraction uses `pypdf`; EPUB, DOCX, TXT and MD extraction use the Python standard library. EPUB chapters are read in the publication's spine order. All `.mentor-work/` contents are ignored by Git.

If a PDF's embedded font produces missing or corrupted characters, do not use that extraction as evidence. Render and inspect every relevant page visually, and record page-based locators instead. *Dingo* in batch `2026-09-batch-01` required this fallback.

## Codex responsibilities

The script does not decide which literary connections are worthwhile. Codex must read the complete work, inspect available visual evidence and use the approved content standard. It then drafts:

- book type and genre;
- strongest writing connections with exact year-level curriculum wording;
- strongest reading connections with exact year-level curriculum wording;
- relevant PRIDE values and inquiry concepts;
- structured, book-specific teaching ideas; and
- internal source locators and provenance.

Select only the strongest connections. Every explanation must point to an identifiable passage, event, language choice or verified illustration and explain why it is useful for teaching. Check the cover, metadata and school resource links as part of the same book revision rather than treating them as later cleanup.

`validate` confirms structure and exact matches against `curriculum-reference-records.json`. It cannot prove that an interpretation is insightful or that a teaching idea is useful. Teacher review provides that judgement.

## Review state

All generated records begin as `ai_suggested` and remain reviewer-only. Present the complete book package for review: metadata, blurb, why-use-this-book summary, strongest writing and reading connections, PRIDE and inquiry connections, teaching ideas, cover status and resource-link status. A teacher may approve, edit or reject it. Only approved records become `teacher_reviewed` and enter teacher-facing pages and filters. Editing an approved record reopens review and preserves its previous version. After publication, verify the live Supabase records and authenticated preview page before reporting the book complete.

## Google Drive handover

The school account needs the Google Drive connector authorised for the school-owned folder. Codex verifies access by listing the folder and reading a selected file. It preserves the sharing decision recorded by the folder owner.

Recommended layout:

```text
Ngarri Mentor Text Library
├── Book files - restricted
│   ├── Incoming
│   └── Verified
└── Teaching resources
    ├── Teacher notes
    └── Student materials
```

Current school folder: `Mentor Texts`, Google Drive folder ID `15H0vElzelAVyq_okj427vUlD7IQeAbap`.

On 8 September 2026, Phill explicitly accepted the folder's existing **anyone-with-the-link** access because book links are intended to be presented to teachers through the shared-password website. Preserve this as a recorded owner decision and do not broaden or change access without a new decision. Do not copy full books into Supabase or website data. The private text-only continuity archive is the documented GitHub exception. The website should link to the Drive copies and let Google Drive enforce the configured access.
