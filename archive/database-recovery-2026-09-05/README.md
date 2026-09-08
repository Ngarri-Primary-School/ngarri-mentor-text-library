# Ngarri Mentor Text Library — restored database handover

Verified 5 September 2026 against Supabase project `dahilwcsbtstfbokbxws`. This addendum supersedes the inactive-database status and restore instruction in the earlier reconciled handover. Earlier packages are retained unchanged for provenance.

## Current state

The restored database is readable and contains 343 active books, 391 writing annotations and 260 reading annotations. Both kinds of annotation exist for 54 books; 36 have writing only; none have reading only; 253 have neither. These counts confirm the later handover. Missing annotations are an enrichment queue, not evidence that every book should receive every kind of tag.

The 651 existing annotations comprise 318 OzLit imports and 333 teacher spreadsheet imports. There are no AI suggestions in these two tables. There are no orphan book/reference links or duplicate book/trait-or-strategy/year keys in these tables. All books have blurbs; six are marked for review. PRIDE annotations, inquiry annotations, teaching ideas, why-use bullets and teaching resources are empty.

The database retains 22 migration records with their original SQL statements. The `migrations/` folder preserves each record as JSON and a readable SQL companion. These are recovered historical migrations, not newly applied changes. Current public-table rows are preserved in `data/`; catalog evidence is in `catalog/`. `verification-evidence.json` records the audit queries' results. The generated manifest records file hashes and row counts.

This is a logical recovery snapshot taken through separate read-only queries, not an atomic PostgreSQL backup. It excludes Auth, Storage objects, private schemas, roles, secrets and infrastructure settings. The migration SQL has not been replayed in a clean database. Do not treat it as a tested disaster-recovery backup.

## Access discrepancy to resolve before the pilot

All 14 public tables have row-level security enabled, but their public SELECT policies use `true`. Thus existing read access does not filter by review status, and future unreviewed suggestions could be returned. Both `anon` and `authenticated` hold SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES and TRIGGER privileges on these tables. Absence of row-write policies currently restricts ordinary row writes through RLS; broad grants alone do not demonstrate an exploitable anonymous web write. TRUNCATE is not governed by RLS, so unnecessary role privileges still merit removal. No destructive access tests were performed.

The security advisor reported no findings, which does not establish that these policies match the project's intended review workflow. See ACCESS-PROPOSAL.md for the concrete intended correction. No permissions were changed.

## Remaining gaps

- Cover fields contain filenames, not hosted image URLs. The asset comparison identifies which filenames match the inspected OneDrive images; filename matching does not verify book identity or hosting.
- The original enrichment implementation, regression suite, saved 20-book benchmark outputs and historical Git repository remain unrecovered. Database recovery cannot recreate them. Historical claims of 24 passing tests are not fresh test results.
- PRIDE and inquiry annotation tables lack the explicit source fields present on writing/reading annotations. Teaching ideas and why-use records also lack complete provenance/reviewer fields described in the planned governance. These are implementation gaps, not reasons to fabricate evidence.
- The earlier audit's Google API credential findings and script-quality defects remain outstanding. Credential-bearing source files were excluded from the handover packages; no credential rotation occurred.

## Canonical structure and next action

Keep one future repository with README.md and docs/PROJECT.md, ARCHITECTURE.md, GOVERNANCE.md and HANDOVER.md as the maintained entry points. Keep recovered SQL under supabase/migrations/, reference datasets under reference-data/, dated snapshots and provenance manifests under data/snapshots/, implementation under scripts/ and app/, and the permanent reviewed benchmark under tests/fixtures/. Retain original archives separately and do not overwrite historical evidence with regenerated output.

The final bundle includes the earlier reconciled documentation unchanged plus this current addendum. This is a recovery/handover package, not a runnable application. No source files or database records were altered.

**Next single action:** review ACCESS-PROPOSAL.md and authorise the described access correction before teacher-pilot development resumes. The Mac can remain deferred while this is addressed.
