# Teacher-pilot access change — applied

**Current status:** Applied after explicit user approval on 6 September 2026. Read [the deployment report](deployed/README.md) for live verification. The preparation record below is retained as historical context and its approval-pending statements are superseded.

Prepared 6 September 2026. **Not deployed.** Automatic approval review rejected the live migration because the prior authorisation was interpreted as review/validation only. No alternate execution was attempted.

## Exact change awaiting approval

Apply candidate.sql to project dahilwcsbtstfbokbxws as `restrict_teacher_pilot_access`:

- Replace the 14 unrestricted public read policies with explicit trusted-read policies on 13 tables. Teaching resources remain inaccessible to client roles until their review workflow exists.
- Remove all client-role table privileges, including MAINTAIN, then grant SELECT only where needed. Both anon and authenticated remain read-only. Administrative service-role grants remain unchanged.
- Expose active books and existing reference data. Writing/reading annotations are visible only when imported_teacher, imported_ozlit, teacher_reviewed or teacher_added; other annotation/teaching content requires teacher_reviewed or teacher_added. Related rows must have an active parent book.
- Stop automatic client-role table grants for future tables created by postgres in public.
- Make no changes to book or annotation content, original archives, credentials, or Storage.

This preserves public access to all current 343 active books and 651 imported annotations. Six blurbs remain marked needs_review and are still readable; the future interface must visibly label that status. This change does not implement a blurb approval interface or certify the content for public publication. The existing no-login read model is retained.

## Validation

328 checks passed in isolated PGlite PostgreSQL. All 22 recovered historical migrations replayed successfully, with only pgcrypto extension registration omitted because gen_random_uuid is built in. This recovered the documented 343/391/260 book/writing/reading counts. Tests checked both client roles, every annotation status, archived parent filtering, actual denied INSERT/UPDATE/DELETE attempts, unavailable teaching-resource reads, absence of write/maintenance grants, future-table defaults for postgres, unchanged row counts and rollback restoration of table grants/policies. The first rollback comparison failed because ACL entry ordering changed; the test now compares sorted ACL entries, preserving semantic equality.

This is not a hosted Supabase API integration test. No live migration or post-deployment validation has occurred. `test-results.json` records the engine and checks; `test-access.mjs` is reproducible with the integrity-checked PGlite 0.5.8 runtime described in runtime-provenance.json. The runtime is excluded from the distributable package.

## Scope and rollback

`rollback.sql` restores the observed pre-change public read policies and broad client table/default grants; it deliberately restores their earlier exposure. Use it only to reverse this exact change after checking for subsequent changes. Both scripts use transactions; the candidate has a five-second lock timeout.

The live raw ACL records also revealed MAINTAIN privileges omitted from the earlier information_schema-based summary. `table-acls.json` preserves that correction. Platform-owned supabase_admin default grants also exist in public; they remain unchanged. Future tables created by that role require explicit grant/RLS review. Sequence/function default grants are also outside this table-only change. No new security-definer function or reviewer write policy is introduced.

After explicit approval: recheck policies/grants for drift, register and apply the tested SQL as a migration, verify both client roles against the live data, and save the resulting migration record and evidence. The database-update tool generates the migration history entry; this SQL candidate is not a manually timestamped migration file.

## Provenance and documentation

The earlier database-verified handover ZIP remains unchanged. This is a separate implementation addendum. The audit/recovery package remains authoritative for original source provenance, missing enrichment code/tests/benchmark, credential findings and cover recovery.

The official [RLS guide](https://supabase.com/docs/guides/database/postgres/row-level-security) and [API security guide](https://supabase.com/docs/guides/api/securing-your-api) were checked, along with the Supabase changelog. Grants and row policies are separate controls; this change addresses both. No relevant breaking change prevented this table-policy implementation.
