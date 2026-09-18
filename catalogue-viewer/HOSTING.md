# Shared progress viewer handover

Site address: https://ngarri-mentor-library-progress.velveteen.chatgpt.site

The user approved a shared-password sign-in for the school principal, literacy leaders and Phill. The site retains the original search, combined filters, book detail view and missing-information indicators. The password is intentionally absent from GitHub, source code and project documents. Change it only through the hosting environment's secure settings.

As verified on 18 September 2026, Supabase contains Owl Moon as an approved revision with 7 writing, 6 reading, 1 PRIDE, 2 inquiry and 8 teaching ideas. Draft AI annotations are excluded from teacher-facing responses. Complete book and text-only resource packages live in the private repository's `book-files/`.

## Protected file store

The shared site now proxies `/book-files/...` and `/covers/...` to the private Supabase Storage bucket `mentor-library-files`. This keeps the original school PDFs, clean text-only PDFs and all catalogue covers behind the same shared-password sign-in, while keeping website releases small. Direct bucket access is not allowed.

The one-time migration stored 16 PDFs for *Crickwing*, *Night Tree*, *The Alphabet Tree*, *Little Blue and Little Yellow*, *Owl Moon*, *The Gruffalo*, *The Boy Who Loved Words* and *Fox*, plus 222 covers. Fox's cover was added from the checked first page of its school PDF.

For a later book update:

1. Keep the canonical original PDF, text-only PDF and transcript package in `book-files/` in this private repository.
2. Upload only that book's changed served files to the private bucket using the authenticated file-store deployment procedure. Preserve the object paths already used by the viewer: `/book-files/<slug>/picture-book.pdf`, `/book-files/<slug>/text-only.pdf` and `/covers/<cover filename>`.
3. Update the resource mapping or cover status only when it changes, then deploy the small viewer source update. Do not put the full PDF or cover collection back into the website deployment archive.
4. Sign in to the shared site and check the cover plus both PDF buttons for the changed book.

The file-store proxy and its credentials are in the separate Sites deployment source and runtime settings. The bucket name, function name (`mentor-library-files`) and object paths are safe to record; passwords, proxy values and upload values must remain in secure runtime settings only.

`.openai/hosting.json` records the existing Sites project; reuse it for updates rather than creating another site. The separate Sites deployment copy contains the shared sign-in worker and current link mapping. Sites keeps the published interface independent of this computer. Use the standard Sites packaging helper and credentials provided at runtime for future interface or link updates. The served PDFs and covers must stay in the private file store, not in the deployment archive.

The school GitHub repository remains the canonical project documentation/code destination. The Sites source repository is a deployment copy, not a competing editable project. The initial Site is owned by Phill's current account; school ownership/access handover for hosting remains a separate task. No automatic GitHub-to-Sites deployment has been configured.

Database content refreshes without republishing the website. Republish this Site when its interface, static cover collection or hard-coded school-resource link mapping changes. Supabase Row Level Security keeps unreviewed suggestions out of teacher-facing responses.
