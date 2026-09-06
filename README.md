# Ngarri Mentor Text Library

School project handover prepared 7 September 2026. This package contains the working local Fox reviewer, saved teacher review, school curriculum reference records, design references and recovered database migrations. It is not a finished or deployed teacher website.

## Start the existing prototype

With Python 3 installed, run from this repository:

```sh
python -m http.server 8765 --bind 127.0.0.1 --directory fox-working-page
```

Open http://127.0.0.1:8765/. No dependencies or database credentials are required to view it. Serve only that folder. Reviews use browser storage; a new browser starts a new local review. The preserved review export is not automatically imported.

## Current decisions and next development

Read `docs/CURRENT.md`, then the saved design references. This README supersedes that note's proposal to make a separate code-folder copy: the user chose a private school GitHub repository as the shared project destination instead.

Phill's unchanged saved export is `codex-transfer-preparation/fox-review-record.json`: nine locally approved connections and one omitted. Requests to remove PDF page numbers from teacher prose are still outstanding. Preserve precise internal evidence locators and original reviewed text. Rewrite Making Connections around readers connecting the text to their experience, and submit that revised item for review. Do not carry forward approval onto changed content automatically.

Select each book's strongest evidenced examples, without a quota or three-item cap. AI suggestions remain reviewer-only until approved. Current local preview controls are not production authentication. The final teacher page should follow the five Fox prototype images in `docs/vault-snapshot/Design/assets/fox-prototype/`.

The recovery snapshot recorded 343 active books, 391 writing annotations and 260 reading annotations. All 651 explanations were empty. The applied access correction and 328-check isolated test record are in `mentor-access-change/`. Production reviewer access, teacher website and enrichment pipeline remain unfinished. No paid generation, bulk enrichment or new database deployment is authorised by this transfer.

## Documentation and provenance

`docs/vault-snapshot/` is a dated, unchanged capture of the Obsidian project vault, not an automatically synchronised second vault. Historical statements are retained; dated corrections and the current-state note take precedence. Keep that snapshot unchanged. `docs/CURRENT.md` is the editable current handover; make future documentation changes in this repository. A pointer in the original vault will record this transition after publication.

`TRANSFER-MANIFEST.json` records original paths and SHA-256 hashes. Originals remain untouched. This upload staging directory is temporary packaging, not an additional working project. GitHub is the shared destination; a future local checkout must track that repository rather than become another independent copy.

## Dependencies and external material

Viewing the prototype uses only Python's standard library. Rebuilding Fox data additionally requires `pypdf` and the exact external PDF identified by `fox-source-review/manifest.json`; the current builder uses that original local path. Do not rebuild just to view the page. Porting generation to a different computer requires an explicit source-path configuration while retaining the source hash.

The isolated database test uses PGlite 0.5.8, with its original integrity record in `mentor-access-change/runtime-provenance.json`. The vendored runtime is intentionally excluded; restore that version at `mentor-access-change/runtime/package` before running `test-access.mjs`. Historical migrations include recovery data and old access rules: do not apply them to the live database. The later access correction is recorded separately.

Full book PDFs, full commercial inquiry-book extracts, page renders, source ZIPs, credentials, dependency caches and full database export folders are excluded. Their source locations are recorded in existing manifests and handover notes. Original archives and vault backup remain on the current computer; this GitHub package does not replace school storage or the Supabase database backup. Supabase and hosting ownership still need a separate institutional handover.

Steve's organisation invitation is deferred until his GitHub username is available. The school Codex account still needs its own repository authorisation. Repository creation alone does not establish either access.
