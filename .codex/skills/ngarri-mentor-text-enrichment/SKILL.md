---
name: ngarri-mentor-text-enrichment
description: Select, prepare, validate and review Ngarri Mentor Text Library book enrichment using verified full texts, exact school curriculum wording and the approved five-book quality standard.
---

# Ngarri mentor-text enrichment

Use this skill for choosing the next books, analysing complete texts, drafting book records, checking curriculum alignment, or preparing content for teacher review.

Read `docs/ENRICHMENT-PIPELINE.md`, `docs/CONTENT-AND-DISPLAY-FORMAT.md` and `docs/CONTENT-AUTHORING-GUIDE.md`. Use `scripts/mentor_pipeline.py` for intake, extraction, scaffolding and validation. Keep all full texts and working extracts under `.mentor-work/`; never commit them.

## Start with the book-intake gate

Review the catalogue, completed books and coverage needs. Propose a manageable batch of three to five named books with a brief reason for each. Favour books that broaden year levels, text types, genres and curriculum coverage and that the school is likely to hold.

Record the chosen list with `new-batch`, show it to the user, and stop. Do not analyse from titles, covers or blurbs while the complete texts are unavailable. Resume only after the user says the files are in the school Google Drive and provides or identifies the folder.

Use the Google Drive connector to list the folder and confirm that each selected file is readable in full. Record only sources that Codex can actually open. A visible filename or link is not proof of access. Keep commercial books restricted to the appropriate school accounts; do not change sharing to public or “anyone with the link.” Run `register-source --verified` for each verified text. If any source is missing, tell the user exactly which title is still needed and pause that title.

## Create the draft

Run `make-draft` only after source verification. Establish these bibliographic fields as part of every enrichment:

- **Text type:** the broad communicative form or purpose, such as narrative, informative, persuasive, poetry or hybrid/multimodal.
- **Genre:** the more specific literary or informational tradition, such as cumulative tale, quest narrative, fable, literary nonfiction or procedural text. More than one genre is allowed when the evidence supports it.

Give a brief classification rationale based on the complete work. Do not infer classification only from publisher marketing.

Read the complete text and inspect available illustrations. Select every strong, distinct connection the book demonstrates especially well, without quotas or padding. For writing and reading, cite one curriculum reference record and copy one matching Key Understanding and Key Skill exactly. A missing Key Skill is permitted only under the documented professional-reading exception. Identify a precise passage, event, language choice or verified illustration and explain its teaching value. PRIDE and inquiry use concepts without year-level subdivisions. Treat counterexamples as counterexamples.

Teaching ideas must grow from the selected book evidence and include the structured fields required by the validator. Before drafting them, inspect and use the narrowest relevant installed education skills, such as `reading-comprehension-strategy-selector`, `pedagogical-content-knowledge-developer` or `think-aloud-script-generator`. Record which skills shaped the draft. If none fits, use the available skill-discovery or installer workflow to look for one. Treat skill output as design support and recheck it against the complete book and exact Ngarri sources. Reject any idea that would still work unchanged after replacing the title with another book.

Keep all new records `ai_suggested`. Run `validate` before presenting a draft. Resolve errors; explain any warnings that reflect a deliberate absence of strong connections.

## Review and publication boundary

Present a teacher-readable review draft. Teacher approval is required before changing records to `teacher_reviewed` or exposing them in teacher-facing pages and filters. Preserve the AI draft, reviewer identity, review time, edits and source provenance. Do not deploy a database migration, publish content or initiate paid/bulk generation without the relevant authorisation.

Google Drive remains the access-control point for full books. Supabase stores the book's restricted Drive reference and resource metadata; the public progress viewer must never expose full-text links. The eventual authenticated teacher library may show an **Open school copy** action to authorised users.
