---
name: ngarri-mentor-text-enrichment
description: Select, prepare, validate and review Ngarri Mentor Text Library book enrichment using verified full texts, exact school curriculum wording and the approved five-book quality standard.
---

# Ngarri mentor-text enrichment

Use this skill for choosing the next books, analysing complete texts, drafting book records, checking curriculum alignment, or preparing content for teacher review.

Read `docs/ENRICHMENT-PIPELINE.md`, `docs/CONTENT-AND-DISPLAY-FORMAT.md` and `docs/CONTENT-AUTHORING-GUIDE.md`. Use `scripts/mentor_pipeline.py` for intake, extraction, scaffolding and validation. Keep new extractions and working copies under `.mentor-work/`; manage their storage and publishing location according to the school's current direction. Approved text-only transcriptions already preserved under `restricted-reference/` may be used as supplementary evidence.

## Start with the book-intake gate

Review the catalogue, completed books and coverage needs. Propose a small batch of one to three named books with a brief reason for each. Favour books that broaden year levels, text types, genres and curriculum coverage and that the school is likely to hold.

Show the proposed list to the user before beginning so they can check that the complete books are available through the school Google Drive or `book-files/` in this private repository. Record the agreed list with `new-batch`, then stop. Do not analyse from titles, covers or blurbs while the complete texts are unavailable. Complete only one book at a time and wait for teacher approval before publishing it or beginning the next book.

Use the Google Drive connector or `book-files/` to confirm that each selected file is readable in full. Record only sources that Codex can actually open. A visible filename or link is not proof of access. Preserve the school's recorded access decision and do not broaden or change it without approval. Run `register-source --verified` for each verified text. If any source is missing, tell the user exactly which title is still needed and pause that title.

Before extracting anything, search `restricted-reference/jimk-mentor-texts/`, `book-files/` and the Drive `Text Extractions - Restricted/` folders for existing text resources. Prefer a suitable checked transcription or reliable embedded text layer. Use fresh extraction next and OCR only when necessary. Check an existing transcription against the complete school copy at the beginning, middle and ending, verify every cited passage, note edition differences and inspect all illustrations used as evidence.

If a JimK transcription is suitable, it may seed the clean transcript and searchable text-only PDF saved to the book's Drive extraction folder. Also save concise transcription-review notes. Website resource links must point to the approved Drive copies, not the private GitHub transcription.

## Create the draft

Run `make-draft` only after source verification. Establish these bibliographic fields as part of every enrichment:

- **Text type:** the broad communicative form or purpose, such as narrative, informative, persuasive, poetry or hybrid/multimodal.
- **Genre:** the more specific literary or informational tradition, such as cumulative tale, quest narrative, fable, literary nonfiction or procedural text. More than one genre is allowed when the evidence supports it.

Give a brief classification rationale based on the complete work. Do not infer classification only from publisher marketing.

Check the title, author, illustrator, publication details, year band, cover and resource links during every book revision. Confirm that the cover belongs to the correct book or edition and renders correctly. Record whether the original school PDF and searchable text-only PDF are ready to link from the authenticated site.

Read the complete text and inspect available illustrations. Select every strong, distinct connection the book demonstrates especially well, without quotas or padding. For writing and reading, cite one curriculum reference record and copy one matching Key Understanding and Key Skill exactly. A missing Key Skill is permitted only under the documented professional-reading exception. Identify a precise passage, event, language choice or verified illustration and explain its teaching value. PRIDE and inquiry use concepts without year-level subdivisions. Treat counterexamples as counterexamples.

Teaching ideas must grow from the selected book evidence and include the structured fields required by the validator. Before drafting them, inspect and use the narrowest relevant installed education skills, such as `reading-comprehension-strategy-selector`, `pedagogical-content-knowledge-developer` or `think-aloud-script-generator`. Record which skills shaped the draft. If none fits, use the available skill-discovery or installer workflow to look for one. Treat skill output as design support and recheck it against the complete book and exact Ngarri sources. Reject any idea that would still work unchanged after replacing the title with another book.

Keep all new records `ai_suggested`. Run `validate` before presenting a draft. Resolve errors; explain any warnings that reflect a deliberate absence of strong connections.

## Review and publication boundary

Present one complete, teacher-readable book draft, including cover and resource-link status. Teacher approval is required before changing records to `teacher_reviewed` or exposing them in teacher-facing pages and filters. Preserve the AI draft, reviewer identity, review time, edits and source provenance. After approved publication, verify Supabase and the authenticated preview page before beginning the next book. Do not deploy a database migration, publish content or initiate paid/bulk generation without the relevant authorisation.

Google Drive or the private repository's `book-files/` directory may provide access to full books. Supabase stores the resource reference and metadata. The shared-password progress viewer may show approved users an **Open picture book PDF** and **Open text-only PDF** link to the selected school-managed location. Keep website credentials outside GitHub.
