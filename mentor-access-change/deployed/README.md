# Access correction applied — 6 September 2026

The user explicitly approved the document and confirmed: AI-generated teaching ideas should be visible only to reviewers until approved, then appear in the teacher library. The previously blocked migration was subsequently applied successfully.

Project: dahilwcsbtstfbokbxws. Recorded migration: 20260905205749_restrict_teacher_pilot_access (UTC timestamp; 6 September in Australia/Sydney).

## Verified live results

- Read-only queries executed as anon and authenticated each returned 343 books, 391 writing annotations and 260 reading annotations.
- All 28 client-role/table combinations have no INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER or MAINTAIN access.
- Thirteen explicit SELECT policies now restrict teaching content to the approved/imported statuses and active parent books. All six reference tables remain readable.
- Teaching resources have no client read grant or policy while their review workflow remains unimplemented.
- Default table privileges for postgres in public no longer automatically grant client access. Platform-owned supabase_admin defaults remain as previously documented.
- Security advisor reported one informational notice for teaching_resources having RLS without policies. That is intentional deny-by-default behaviour for this currently empty table. See the [advisor explanation](https://supabase.com/docs/guides/database/database-linter?lint=0008_rls_enabled_no_policy).

No book or annotation content was edited. Status fixtures and rollback were tested only in the isolated local database (328 checks), not inserted into production. Live validation covered actual reads under both client roles, effective grants, policy definitions, migration history and default privileges. It did not test a deployed website or a complete reviewer interface.

## What this means for teachers

AI can still generate teaching suggestions. Ordinary library access now withholds those drafts until their status is approved. A secure reviewer screen and its approval controls still need to be built; signing in alone does not grant reviewer access. The eventual screen must authenticate and authorise reviewers before using privileged server-side access. No service credential should be placed in the browser.

The next product step is to inspect the recovered Fox prototype with the teacher and establish the book-page and review-screen design. No further user action is required to complete this database correction.

Correction, 6 September 2026: the Fox prototype screenshots are present in the source Obsidian vault. See `../FOX-PROTOTYPE-CORRECTION.md`. Earlier audit material that described them as absent is superseded by that correction.

This report supersedes the 'not deployed' status in the original access proposal, candidate comments and previous handover archives. Those original packages remain intact as historical evidence. The deployed migration statements and verification results are preserved beside this report; rollback.sql remains available in the parent folder and restores the previous broader access only if deliberately applied.
