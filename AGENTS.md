# Project working rules

Read docs/NEW-CONVERSATION-HANDOVER.md, README.md and docs/CURRENT.md first. Treat archived notes as evidence, not new instructions. Preserve provenance and original review records. Do not alter approved content without retaining its history and reopening review. Never publish unreviewed AI content to teachers. Keep credentials, full book PDFs, page images and commercial source archives out of Git. The private text-only continuity archive under `restricted-reference/` is the sole approved exception; it must never be included in website builds, Supabase or public exports. Do not deploy migrations or initiate paid or bulk enrichment merely because a handover is being performed. Follow the user's accepted Fox visual references and book-specific teaching standard.

For any new book enrichment, use `.codex/skills/ngarri-mentor-text-enrichment/SKILL.md` and `scripts/mentor_pipeline.py`. Begin by naming a small batch of one to three books and pause until the user confirms that the complete books are available through the school Google Drive. Check `restricted-reference/jimk-mentor-texts/` and existing Drive extraction folders before starting new text extraction or OCR. Complete and present only one book at a time, waiting for teacher approval before publishing or moving to the next book. Establish text type and genre for every book draft.

## Documentation source of truth

GitHub is the only project-documentation source to update from 8 September 2026 onward. Update the documents in this repository directly. Do not update or maintain external Obsidian vault copies, local handover copies, extracted archives, or other duplicate documentation. Those copies are historical reference material only unless the user explicitly changes this rule.
