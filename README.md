# Ngarri Mentor Text Library

School project handover updated 8 September 2026. This package contains the working local Fox reviewer, saved teacher review, school curriculum reference records, design references, the approved five-book complete-text pilot and recovered database migrations. The public progress viewer is deployed; the final production teacher library and secure reviewer application are still to be built.

Shared progress viewer: https://ngarri-mentor-library-progress.velveteen.chatgpt.site/

The active structured curriculum, reading, PRIDE, inquiry and calibration files are indexed in [`reference-data/README.md`](reference-data/README.md). The read-only source audit and safe school-owned originals are in [`reference-sources/README.md`](reference-sources/README.md). The private text-only continuity archive is documented in [`restricted-reference/README.md`](restricted-reference/README.md); it is excluded from all publishing workflows. Commercial PDFs, scans and page images are excluded from GitHub.

## Start the existing prototype

With Python 3 installed, run from this repository:

```sh
python -m http.server 8765 --bind 127.0.0.1 --directory fox-working-page
```

Open http://127.0.0.1:8765/. No dependencies or database credentials are required to view it. Serve only that folder. Reviews use browser storage; a new browser starts a new local review. The preserved review export is not automatically imported.

## Current decisions and next development

Read `docs/CURRENT.md`, `docs/CONTENT-AND-DISPLAY-FORMAT.md` and `docs/ENRICHMENT-PIPELINE.md`, then the saved design references. The content-and-display specification records the approved structure for writing, reading, PRIDE, inquiry and teaching ideas, including the collapsible book-page hierarchy. The enrichment pipeline records the reusable script, Codex skill, Google Drive intake pause, and text-type and genre requirements. This README supersedes the earlier proposal to make a separate code-folder copy: the user chose a private school GitHub repository as the shared project destination instead.

Phill's unchanged saved export is `codex-transfer-preparation/fox-review-record.json`: nine locally approved connections and one omitted. Requests to remove PDF page numbers from teacher prose are still outstanding. Preserve precise internal evidence locators and original reviewed text. Rewrite Making Connections around readers connecting the text to their experience, and submit that revised item for review. Do not carry forward approval onto changed content automatically.

Select each book's strongest evidenced examples, without a quota or three-item cap. AI suggestions remain reviewer-only until approved. The five teacher-approved complete-text pilot books are the current quality benchmark. Current local preview controls are not production authentication. The final teacher page should follow the five Fox prototype images in `archive/obsidian-vault-snapshot/Design/assets/fox-prototype/` and the implemented progressive disclosure rules in `docs/CONTENT-AND-DISPLAY-FORMAT.md`.

The recovery snapshot recorded 343 active books, 391 writing annotations and 260 reading annotations. All 651 explanations were empty. The applied access correction and 328-check isolated test record are in `mentor-access-change/`. Production reviewer access, teacher website and enrichment pipeline remain unfinished. No paid generation, bulk enrichment or new database deployment is authorised by this transfer.

## Starting a new ChatGPT or Codex conversation

Give the new conversation this single onboarding document: [`docs/NEW-CONVERSATION-HANDOVER.md`](docs/NEW-CONVERSATION-HANDOVER.md). It explains access, current status, content rules, repository layout and the immediate next action. The repository is private, so the new account must first connect GitHub and receive access.

## Essential project documents

For ordinary project work, read only these four documents:

1. `README.md` — project overview and starting point.
2. `docs/CURRENT.md` — current state, decisions and next development work.
3. `docs/CONTENT-AND-DISPLAY-FORMAT.md` — approved content and website format.
4. `docs/PICTURE-BOOK-PILOT-APPROVAL.md` — approved pilot benchmark.

Component folders contain technical notes for Codex and developers. They are consulted only when working on that component. Material under `archive/` is retained for provenance and recovery; it is not required reading and does not set current project direction.

## Documentation and provenance

`archive/obsidian-vault-snapshot/` is a dated, unchanged capture of the Obsidian project vault, not an automatically synchronised second vault. Historical statements are retained; dated corrections and the current-state note take precedence. Keep that snapshot unchanged. `docs/CURRENT.md` is the editable current handover; make future documentation changes in this repository. A pointer in the original vault will record this transition after publication.

`TRANSFER-MANIFEST.json` records original paths and SHA-256 hashes. Originals remain untouched. This upload staging directory is temporary packaging, not an additional working project. GitHub is the shared destination; a future local checkout must track that repository rather than become another independent copy.

## Dependencies and external material

Viewing the prototype uses only Python's standard library. Rebuilding Fox data additionally requires `pypdf` and the exact external PDF identified by `fox-source-review/manifest.json`; the current builder uses that original local path. Do not rebuild just to view the page. Porting generation to a different computer requires an explicit source-path configuration while retaining the source hash.

The isolated database test uses PGlite 0.5.8, with its original integrity record in `mentor-access-change/runtime-provenance.json`. The vendored runtime is intentionally excluded; restore that version at `mentor-access-change/runtime/package` before running `test-access.mjs`. Historical migrations include recovery data and old access rules: do not apply them to the live database. The later access correction is recorded separately.

Full book PDFs, full commercial inquiry-book extracts, page renders, source ZIPs, credentials, dependency caches and full database export folders are excluded. Their source locations are recorded in existing manifests and handover notes. Original archives and vault backup remain on the current computer; this GitHub package does not replace school storage or the Supabase database backup. Supabase and hosting ownership still need a separate institutional handover.

Steve's organisation invitation is deferred until his GitHub username is available. The school Codex account still needs its own repository authorisation. Repository creation alone does not establish either access.

