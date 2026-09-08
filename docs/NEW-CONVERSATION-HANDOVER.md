# Start here — new ChatGPT or Codex conversation

Updated: 8 September 2026  
Status: current onboarding guide  
Repository: https://github.com/Ngarri-Primary-School/ngarri-mentor-text-library

## What this project is

The Ngarri Mentor Text Library is a school-owned teaching library. It helps teachers find books that provide especially strong examples for:

- writing traits and year-level curriculum throughlines;
- reading comprehension strategies and year-level curriculum throughlines;
- Ngarri PRIDE values;
- inquiry concepts and lenses; and
- classroom-ready teaching ideas.

Teachers should be able to search or filter the library, open a book, and see why particular parts of that book are useful for teaching. The aim is to teach through the language, events and verified illustrations of the book rather than attach generic activities to a title.

The public progress viewer is:

https://ngarri-mentor-library-progress.velveteen.chatgpt.site/

The private school GitHub repository is the sole project-documentation source of truth:

https://github.com/Ngarri-Primary-School/ngarri-mentor-text-library

## Access needed in the new school account

The school ChatGPT or Codex account must connect to GitHub and be authorised for the private `Ngarri-Primary-School/ngarri-mentor-text-library` repository. Opening a private GitHub link without that connection may fail even though the repository exists.

The Supabase project identifier is `dahilwcsbtstfbokbxws`. Database credentials and service keys are deliberately absent from GitHub. Obtain access through the school's authorised Supabase account or project invitation; never paste secrets into project documents or chat.

Hosting and Supabase ownership still require institutional handover. Steve's GitHub invitation is pending his GitHub username.

## Read in this order

1. `AGENTS.md` — rules that apply to all coding work.
2. `docs/CURRENT.md` — verified current state, unresolved work and next development action.
3. `docs/CONTENT-AND-DISPLAY-FORMAT.md` — approved content structure and collapsible website presentation.
4. `docs/PICTURE-BOOK-PILOT-APPROVAL.md` — approved pilot benchmark.
5. `docs/ENRICHMENT-PIPELINE.md` — the repeatable script, Drive intake gate, classification and review workflow.
6. Read component README or verification files only when working on that component.

Do not load `archive/` by default. It preserves historical evidence and older working plans. Archived statements do not override current documents.

## Current position

Five complete-text picture books have teacher-approved content in Supabase and are visible in the progress viewer:

- *Crickwing*
- *Night Tree*
- *The Alphabet Tree*
- *Little Blue and Little Yellow*
- *The Gruffalo*

These five books are the quality benchmark. *Fox* is a separate calibration and visual-prototype example; it is not a standalone title in the recovered 343-book catalogue.

The recovered catalogue snapshot recorded 343 active books, 391 writing annotations and 260 reading annotations. Much of the original imported annotation data lacked explanations. The final production teacher library and secure reviewer application remain unfinished.

A public progress viewer exists. Production reviewer authentication, final teacher-site implementation, ongoing enrichment workflow, institutional Supabase ownership and hosting ownership are still work in progress.

## Non-negotiable content rules

- Work from a verified complete book text and verified illustrations where available. A title, cover or blurb is insufficient evidence for book-specific teaching claims.
- Choose only the strongest connections that the book demonstrates particularly well. There is no fixed quota and no need to cover every trait, strategy, value, lens or year.
- Reject generic explanations that could fit almost any book after changing the title.
- Identify the relevant passage, language choice, event or verified visual feature. Explain why it is a particularly useful mentor example.
- Keep source facts, short quotations, interpretation and newly designed teaching activities distinguishable.
- Do not place full copyrighted book texts or commercial PDFs in GitHub.

### Writing

Use this hierarchy: writing trait → applicable year levels from lowest to highest → exact Ngarri Key Understanding → exact matching Key Skill → brief book-specific explanation.

### Reading

Use the same hierarchy: reading strategy → applicable year levels → exact Key Understanding → exact matching Key Skill → book-specific explanation.

A trusted professional source may occasionally contain a suitable Key Understanding without a Key Skill. Leave the skill empty, name the source and never invent wording. The approved *Night Tree* Visualising entry is the reference example.

### PRIDE values and inquiry

These are concept-based and do not use year-level subdivisions. Explain how a specific event, relationship, choice or consequence demonstrates, complicates, lacks or repairs the value or concept. Store counterexamples distinctly from positive demonstrations.

### Teaching ideas

Teaching ideas appear after the curriculum, PRIDE and inquiry connections. Structure them with a title, linked focus, suggested years, time/grouping/difficulty where useful, where to look in the book, learning focus, teaching sequence, student application and what to notice in student learning.

## Review and publishing rules

AI-generated teaching content uses `ai_suggested` status and is visible only to authorised reviewers. It must not appear to teachers or affect teacher-facing filters until a teacher approves it. Approved content becomes `teacher_reviewed` with reviewer and review-time provenance.

Editing approved content reopens review. Preserve the earlier wording and review history. A reviewer note is an instruction for a future edit; it does not mean the edit has already been applied.

Do not run paid or bulk enrichment without explicit user approval. Do not deploy database migrations merely because they exist in the repository. Historical migrations under `archive/database-recovery-2026-09-05/` must not be applied to the live database.

## Website presentation

Book details use progressive disclosure and start collapsed. Writing traits and reading strategies open to reveal applicable year levels; each year opens to reveal exact curriculum wording and the book-specific explanation. PRIDE values, inquiry lenses, blurbs and individual teaching ideas also open independently.

The saved *Fox* prototype images are under `archive/obsidian-vault-snapshot/Design/assets/fox-prototype/`. They remain the visual reference together with `docs/CONTENT-AND-DISPLAY-FORMAT.md`.

## Repository map

- `reference-data/` — structured writing, reading, PRIDE, inquiry, text-availability and Oz Lit calibration references; read its README before using them.
- `reference-sources/` — audited source coverage and safe school-owned originals; commercial publications and full books are excluded.
- `catalogue-viewer/` — progress-viewer code and hosting notes.
- `fox-working-page/` — local Fox review and calibration prototype.
- `curriculum-review-2026-09-06/` — prepared school-curriculum reference records.
- `fox-content-review/` and `fox-source-review/` — Fox evidence and review materials.
- `mentor-access-change/` — applied Supabase access correction and verification evidence.
- `codex-transfer-preparation/` — preserved Fox teacher-review export and transfer evidence.
- `docs/` — current project documentation.
- `archive/` — historical provenance and superseded material; not routine reading.

## How work should be saved

GitHub is the source of truth. Work may be performed in a local Git checkout or Codex worktree, but completed changes must be committed and pushed to this repository. Use a branch and pull request for substantial code, database or schema changes so another person can review them. Small authorised documentation corrections may be committed directly.

Do not update the former Obsidian vault, extracted ZIPs, transfer-staging folders or independent local documentation copies. Local previews are temporary and are not the authoritative project state.

## Immediate next action

First, verify that the new school account can read this private repository and open the public progress viewer. Then confirm whether it has authorised access to the Supabase project without exposing credentials.

After access is established, authorise the school account's Google Drive connector and verify access to the restricted school book folder. Use `.codex/skills/ngarri-mentor-text-enrichment/SKILL.md`: name the next three to five books, pause while the user supplies their complete texts, and verify each file before analysis. Prepare text type, genre, strongest writing, reading, PRIDE, inquiry and teaching-idea connections for teacher review; do not restart a broad 20-book trial.

## Message to paste into a new conversation

> Continue the Ngarri Mentor Text Library from the school GitHub repository at https://github.com/Ngarri-Primary-School/ngarri-mentor-text-library. Read `docs/NEW-CONVERSATION-HANDOVER.md`, then follow its reading order. Treat GitHub `main` as the documentation source of truth and `archive/` as historical evidence only. Explain your initial understanding and access status in plain language, then continue from the Immediate next action. Do not publish unreviewed AI content, run paid or bulk enrichment, deploy migrations, or use a book without a verified complete text.
