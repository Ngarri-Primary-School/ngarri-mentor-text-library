# Book enrichment pipeline

Updated: 18 September 2026
Status: approved post-trial workflow; script implemented; five-book trial complete

## Purpose

This pipeline turns a verified complete book into a structured draft for teacher review. It combines deterministic checks with Codex's literary and pedagogical judgement. The five completed trial books remain the quality benchmark: *Crickwing*, *The Alphabet Tree*, *Night Tree*, *Little Blue and Little Yellow* and *The Gruffalo*.

## The intake pause

At the beginning of each batch, Codex reviews the catalogue and names one to three proposed books, with a short selection reason for each. It tells the user before beginning so the user can confirm that the complete books are available in `book-files/` in this private repository. It records the agreed batch using `scripts/mentor_pipeline.py new-batch` and pauses until access is confirmed.

A batch is only a short forward plan. Codex completes one book, presents the entire `ai_suggested` draft and waits for teacher approval before publishing it or beginning the next book. The teacher may reorder, replace or stop the remaining books at every approval point.

The user makes school-held copies available in `book-files/` in this private repository. Codex resumes a book only after it can locate the complete file and verify that the book can be read. It records the repository path, verification time and source fingerprint in an ignored local batch record. An approved text-only transcription may also be consulted from the private continuity archive under `restricted-reference/`, but it does not replace checking the complete school copy and available illustrations.

The repository package is the source for an **Open picture book PDF** link and a matching **Open text-only PDF** link in the shared-password progress viewer. The protected-site deployment must serve or proxy those files; a direct private GitHub URL would require each staff member to have GitHub access.

## Find text before extracting it

For each selected book, use this order:

1. Search `restricted-reference/jimk-mentor-text-index.json` with `lookup-jimk-reference` and open any matching document in `restricted-reference/jimk-mentor-texts/`.
2. Search the matching `book-files/text-only/` package for an existing checked transcript, searchable text-only PDF and review notes.
3. Check whether the complete repository PDF already has a reliable searchable text layer.
4. Extract text from that PDF only when no suitable checked text exists.
5. Use OCR on scanned pages only as the last option.

An existing JimK document saves extraction work, but its edition, completeness and accuracy are not assumed. Compare it with the complete school copy, check the beginning, middle and ending, and verify every passage used in the proposed content. Record omissions or wording differences. Visually inspect every illustration used as evidence.

When a JimK transcription is suitable, use the verified text as the starting point for the book's linkable resources. Prepare a clean transcript, searchable text-only PDF and concise transcription-review notes in the matching `book-files/text-only/` package. The text-only PDF contains only the title, author, illustrator when known, and book text; keep all source, page, OCR and review detail in the separate review notes. The authenticated website may link to the original school PDF and text-only PDF only through its protected deployment; do not send staff to a direct private GitHub URL.

### JimK discovery index

`restricted-reference/jimk-mentor-text-index.json` is a compact, versioned index of the copied JimK transcripts. It records title, author, source path, completeness, review date, genre, teaching-trait tags and both the copied-transcript and metadata source revisions. It is a discovery aid only: JimK tags suggest possible lines of inquiry but do not establish a Ngarri curriculum connection.

Before beginning a book, run:

```sh
python scripts/mentor_pipeline.py lookup-jimk-reference --title "Fireflies" --author "Julie Brinckloe"
```

Use an exact matching transcript only after comparing it with the complete school copy. When the copied JimK folder is refreshed from the JimK project, rebuild its index and record the upstream commit:

```sh
python scripts/mentor_pipeline.py index-jimk-reference --source-revision <copied-text-commit>
```

When the current JimK project is available locally, its `content/Mentor Texts` folder may also enrich the index's genre and trait fields. Record that metadata revision separately. Do not replace a copied transcript merely because its current metadata has changed.

## Per-book preflight

Before writing content, confirm and record:

- complete school book access and its repository path;
- existing JimK or repository text resources, or the extraction method required;
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
- `register-source`: records a repository source only after Codex has checked access;
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

All generated records begin as `ai_suggested` and remain reviewer-only. Present the complete book package for review: metadata, blurb, why-use-this-book summary, strongest writing and reading connections, PRIDE and inquiry connections, teaching ideas, cover status and resource-link status. A teacher may approve, edit or reject it. Only approved records become `teacher_reviewed` and enter teacher-facing pages and filters. Editing an approved record reopens review and preserves its previous version. The school Codex account commits approved source materials to GitHub and reports them ready for publication. The current personal-account owner publishes to Supabase and the authenticated viewer, then verifies the live result before reporting the book complete.

## Book-file access

The private repository's `book-files/` directory is the sole project source for complete books and checked extraction packages. Codex verifies access by listing the relevant location and reading a selected file.

For book files in this repository, use the layout and file-size rules in `book-files/README.md`. Ordinary Git supports files below 100 MiB. Add Git LFS before committing a PDF of 100 MiB or more.

The protected viewer uses its shared school-group sign-in to protect teacher access. Keep the repository private and keep website credentials outside GitHub. The viewer proxies staff requests to the private `mentor-library-files` store, so a new book requires only its changed files to be uploaded. Follow `catalogue-viewer/HOSTING.md`; never rebuild a deployment archive containing the complete PDF or cover collection.
