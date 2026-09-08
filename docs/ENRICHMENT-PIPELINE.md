# Book enrichment pipeline

Updated: 8 September 2026  
Status: approved workflow design; script implemented; Drive folder and production reviewer integration pending

## Purpose

This pipeline turns a verified complete book into a structured draft for teacher review. It combines deterministic checks with Codex's literary and pedagogical judgement. The five approved picture books remain the quality benchmark.

## The intake pause

At the beginning of each batch, Codex reviews the catalogue and names the next three to five books, with a short selection reason for each. It records the batch using `scripts/mentor_pipeline.py new-batch`, tells the user which books are next, and pauses.

The user places school-held copies in the restricted school Google Drive folder. Codex resumes only after it can list and read each complete file through the school account's Google Drive connection. It records the Drive file identifier, verification time and source fingerprint in an ignored local batch record. Full commercial texts and extracted working copies remain outside GitHub.

The same restricted Drive file can later support an **Open school copy** link in the authenticated teacher library. The public progress viewer must not expose these links. Google Drive permissions remain authoritative.

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
  --batch-id 2026-09-batch-01 `
  --count 5 `
  --out .mentor-work/2026-09-batch-01.json
```

Use Codex's bundled Python runtime if `python` is not configured. PDF extraction uses `pypdf`; DOCX, TXT and MD extraction use the Python standard library. All `.mentor-work/` contents are ignored by Git.

## Codex responsibilities

The script does not decide which literary connections are worthwhile. Codex must read the complete work, inspect available visual evidence and use the approved content standard. It then drafts:

- book type and genre;
- strongest writing connections with exact year-level curriculum wording;
- strongest reading connections with exact year-level curriculum wording;
- relevant PRIDE values and inquiry concepts;
- structured, book-specific teaching ideas; and
- internal source locators and provenance.

`validate` confirms structure and exact matches against `curriculum-reference-records.json`. It cannot prove that an interpretation is insightful or that a teaching idea is useful. Teacher review provides that judgement.

## Review state

All generated records begin as `ai_suggested` and remain reviewer-only. A teacher may approve, edit or reject each record. Only approved records become `teacher_reviewed` and enter teacher-facing pages and filters. Editing an approved record reopens review and preserves its previous version.

## Google Drive handover

The school account needs the Google Drive connector authorised for the school-owned folder. The folder should be restricted to the intended school users. Codex verifies access by listing the folder and reading a selected file; it does not make the folder public.

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

When the folder is created, record its school-owned location and access rules in this document without adding credentials or publicising restricted file links.
