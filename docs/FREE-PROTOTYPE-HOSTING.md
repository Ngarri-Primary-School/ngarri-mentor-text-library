# School-Owned Prototype Hosting

Status: planning only. The current personal-account website remains live and unchanged while this prototype is prepared and tested.

## Purpose

Create a school-owned prototype that lets an authorised user of the school Codex account maintain the mentor-text website, its approved content and its staff-served files. The preferred route is the school's existing cPanel hosting with WordPress on a subdomain. It must use existing school hosting or free services only and must stop if a new service requires payment or billing details.

## Proposed services

| Service | School-owned role | Free-plan check |
|---|---|---|
| Private GitHub repository | Canonical source: documents, website source, complete books and checked extraction packages | Existing project repository. |
| School cPanel/WordPress | Website, database, shared-password access, Media Library and protected PDF routes | Confirm the existing school hosting includes a subdomain, HTTPS, PHP 8.2+, MySQL/MariaDB, storage, backups and Git/SFTP deployment. |
| Private GitHub repository | Canonical source and backup for plugin source, documents, complete books and checked extraction packages | Existing project repository. |

The proposed address is a school subdomain such as `mentor-library.ngarrips.vic.edu.au`. The current personal-account site remains the fallback until the subdomain is verified.

## Capacity decision

The complete-book collection is documented as approximately 408 MiB, including one Git-LFS book. Repository metadata on 9 October 2026 measured 274 MiB for 30 normal-Git original PDFs and 0.2 MiB for 26 text-only PDFs; the difference is the LFS-managed book. A Supabase Free project has 1 GB storage and 5 GB monthly egress.

This is enough for a small prototype, but not a reason to mirror the whole private GitHub collection immediately. The initial transfer contains only the resources currently linked in the staff viewer: original and text-only PDFs for *Crickwing*, *Fox*, *Little Blue and Little Yellow*, *Night Tree*, *Owl Moon*, *The Alphabet Tree*, *The Boy Who Loved Words* and *The Gruffalo*, plus their required covers. Measure the actual transferred total before accepting the prototype. Keep at least 25% of the 1 GB limit unused.

## Ownership and access

1. The school IT provider creates or confirms the cPanel subdomain and WordPress installation.
2. The school records at least two responsible staff owners outside this repository, so access does not depend on one person.
3. The school GitHub account receives repository write access.
4. The school cPanel account deploys the tracked WordPress plugin from the private repository using an IT-approved Git or SFTP process.
5. The school WordPress administrator owns the database, Media Library, access settings and backups.

Do not put credentials, API keys, shared passwords or recovery codes in GitHub, this document, Codex chats or website source files.

## Prototype phases

### Phase 0: hosting check

The IT provider confirms the cPanel capabilities listed above. Stop if the school would need a new paid account or billing details. Do not create a second cloud storage service while cPanel capacity is unverified.

Record only these outcomes in `docs/CURRENT.md`: account created or blocked, account owner role confirmed, and whether the free plan is active. Do not record account credentials.

### Phase 1: school-owned WordPress test deployment

1. Install `wordpress-plugin/ngarri-mentor-library/` on a temporary school subdomain.
2. Create a WordPress page containing `[ngarri_mentor_library]`.
3. Create the shared school WordPress user and keep its credentials outside GitHub.
4. Import the approved catalogue JSON through **Mentor Library > Import catalogue**.
5. Upload a test cover and PDFs into the plugin's private media area.
6. Confirm that an unauthenticated visitor cannot load the catalogue, a cover or a PDF route.
7. Confirm that an authenticated user can sign out and loses resource access.

Do not point staff to the prototype yet and do not replace the present viewer.

### Phase 2: WordPress data and media migration

The current personal-account owner exports the approved database schema and approved data as JSON. Import it into the WordPress plugin tables. Transfer all PDFs and covers to the WordPress Media Library using the plugin's private upload route.

Keep the WordPress site and its direct media URLs behind the shared login. Do not expose direct file-system paths or private GitHub links.

### Phase 3: complete resource transfer

1. Copy all complete original PDFs, text-only PDFs and matching covers to the WordPress Media Library.
2. Preserve the existing resource paths: `book-files/<slug>/picture-book.pdf`, `book-files/<slug>/text-only.pdf` and `covers/<filename>`.
3. Measure storage after upload and record only the aggregate total in `docs/CURRENT.md`.
4. Confirm the resource route requires the website sign-in and does not disclose a direct storage URL.

Confirm the cPanel storage and bandwidth allowance before beginning the complete transfer.

### Phase 4: parity check

Test the school prototype against the current viewer:

- catalogue search and all filters, including year level;
- correctly displayed book covers;
- approved teaching content only;
- original and text-only PDFs for all eight linked books;
- sign-in, sign-out and rejection of unauthenticated requests;
- a GitHub change deployed by the school account; and
- a changed PDF uploaded without redeploying the complete resource collection.

The current personal-account site remains the staff site until Phill approves the parity check.

### Phase 5: cutover decision

Only after approval, change the staff link to the school-owned prototype address. Retain the old site unchanged until the replacement has been used successfully in a literacy meeting. Update `docs/CURRENT.md`, `catalogue-viewer/HOSTING.md` and the school continuation prompt only after that decision.

## Free-tier limitations

- WordPress Media Library files must use the plugin's protected `/ngarri-file/<attachment-id>` routes, not ordinary public upload URLs.
- cPanel storage, bandwidth and backup limits must be confirmed with the IT provider.
- The plugin's current admin screen is an import/listing screen; the full WordPress-native book editor remains Phase 2 implementation work.

## Next action

Phill creates or asks school IT to create the two school-owned Free accounts. Before entering any payment or billing details, stop and report the screen/request. Once both free accounts exist, the next technical task is Phase 1: create the school-owned Cloudflare test deployment.
