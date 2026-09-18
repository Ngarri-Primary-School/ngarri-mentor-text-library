---
title: Ngarri Mentor Text Library - Current State
type: project-status
updated: 2026-09-18
status: active
---

# Current State

This is the single live record of project status. Update it whenever an approval, publication, access arrangement or immediate next action changes. GitHub `main` is the documentation source of truth; `archive/` is historical evidence only.

## Current work

The five-book complete-text trial is approved and published in Supabase and the shared progress viewer: *Crickwing*, *Night Tree*, *The Alphabet Tree*, *Little Blue and Little Yellow* and *The Gruffalo*. *The Boy Who Loved Words* was approved and published on 18 September 2026 as the first post-trial revision. These books are the quality benchmark. *Crickwing* remains the primary model for the strength and specificity of book connections. *Fox* is a calibration and visual-prototype example, not a catalogue title.

The agreed next batch is *Owl Moon*, *Fireflies!* and *Smoky Night*. Their complete books are available in `book-files/`.

*Owl Moon* was approved and published on 10 September 2026. It has 7 writing, 6 reading, 1 PRIDE, 2 inquiry and 8 teaching-idea records. Its metadata, cover and the former website resource links were checked on the live website.

**Immediate next action:** do not begin another book unless Phill asks to continue. The next proposed book is *Big Red Kangaroo* by Claire Saxby; prepare it as `ai_suggested`, show the complete draft for review, and wait for approval before publishing another book.

## Working systems

- **School GitHub repository:** https://github.com/Ngarri-Primary-School/ngarri-mentor-text-library
- **Shared progress viewer:** https://ngarri-mentor-library-progress.velveteen.chatgpt.site/
- **Viewer access:** shared school-group password for Phill, the principal and literacy leaders. The credential is deliberately outside GitHub, source code and project documents.
- **Supabase project:** `dahilwcsbtstfbokbxws`. Publication is performed only by the current personal-account owner; never paste credentials into chat or files.
- **Repository book files:** `book-files/picture-books/` contains 31 complete picture-book PDFs copied from the school local Mentor Texts collection on 16 September 2026. The files total 408 MiB; *Dingo* is managed with Git LFS. `book-files/text-only/` contains 26 complete checked extraction packages, each with a searchable PDF, Markdown transcript and OCR review notes. Follow `book-files/README.md` for later additions.
- **Text resources:** check `restricted-reference/jimk-mentor-text-index.json`, its matching transcript when present, and `book-files/text-only/` before extracting text or running OCR.

The repository is the sole source for project files; Google Drive is retired for this project. The protected website serves its book PDFs and covers from the private `mentor-library-files` storage bucket, through the same shared-password site. The bucket currently holds the 16 original/text-only PDFs for the eight linked books and 222 catalogue covers. It is not public; staff always use the normal website links.

**Account boundary:** the school Codex account may do book research, content drafting, PDF preparation and GitHub updates. It must stop after committing a teacher-approved package and report it ready for publication. The current personal-account owner alone can update Supabase, the private file store, secure settings and the current Sites deployment. This remains the arrangement until the school adopts a replacement hosting service it owns and can administer.

## Current rules that must not drift

- Work from a verified complete school copy and verified illustrations where available.
- Select only strong, distinct, book-specific connections. Every explanation must identify a passage, event, language choice or verified visual feature.
- Use exact Ngarri curriculum wording for writing and reading connections.
- Keep AI-created work `ai_suggested` until reviewed. Preserve the earlier wording and review history when content changes.
- Check text type, genre, year band, metadata, cover correctness, original-PDF link and text-only-PDF link for every revised book.
- Use relevant installed education skills when designing teaching ideas, then check their output against the book and Ngarri references.
- Do not publish unreviewed AI content, run paid or bulk enrichment or deploy database migrations.
- A school Codex account must not attempt Supabase, storage or live-website publication, even after teacher approval; hand the approved GitHub package to the current personal-account owner.

## Task routing

| When working on | Read |
|---|---|
| New book content | `docs/CONTENT-AUTHORING-GUIDE.md`, `docs/ENRICHMENT-PIPELINE.md`, `.codex/skills/ngarri-mentor-text-enrichment/SKILL.md` |
| Book-page structure or interaction | `docs/CONTENT-AND-DISPLAY-FORMAT.md` |
| Approved quality examples | `docs/PICTURE-BOOK-PILOT-APPROVAL.md` and the relevant approved review file |
| Website deployment or resource links | `catalogue-viewer/HOSTING.md` |
| Moving work to another school Codex/ChatGPT account | `docs/SCHOOL-CODEX-CONTINUATION-PROMPT.md` |
| Curriculum or source material | the relevant reference-folder README before using its contents |

## Deferred work

- Individual reviewer authentication and school-owned access management.
- Institutional ownership handover for Supabase and hosting.
- Steve's GitHub organisation invitation, once his GitHub username is available.
- Remaining catalogue enrichment, one reviewed book at a time.

Older recovery counts, Fox review history, local Windows paths, migration records and former handover details are retained in component folders and `archive/` for provenance. They are not active instructions.

