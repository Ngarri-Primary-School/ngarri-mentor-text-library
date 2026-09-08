# Approved content updates

This folder contains reviewable SQL used to publish teacher-approved book content to Supabase. The files are data-change records, not instructions to rerun every update blindly.

- `2026-09-09-alphabet-tree.sql` publishes Phill's approved complete revision of *The Alphabet Tree*. It hides the superseded pilot records, reuses schema-constrained record identities, adds the new connections and verifies the expected live counts inside the transaction.

Before applying a file, confirm the target project, inspect the current book records and check that the approval named in the header is recorded. After applying it, query the resulting counts and inspect the public read path.
