# Shared progress viewer

Site address: https://ngarri-mentor-library-progress.velveteen.chatgpt.site/

This is the staff-facing, read-only library. It uses a school-group sign-in. Keep the username, password and all service credentials in secure runtime settings, never in GitHub, prompts, source code or project notes.

## Where things live

| Item | Authoritative location | What the website uses |
|---|---|---|
| Project documentation, complete school PDFs, transcripts, text-only PDFs and OCR notes | This private GitHub repository | The repository is the source to update first. |
| Approved book content and metadata | Supabase project `dahilwcsbtstfbokbxws` | The viewer reads approved content directly and refreshes automatically. |
| Staff-served original PDFs, text-only PDFs and covers | Private Supabase Storage bucket `mentor-library-files` | The site worker proxies these objects after the school sign-in. Direct bucket links are not for staff use. |
| Viewer interface, login worker and resource mapping | The separate Sites deployment source | It is a deployment copy, not a second curriculum-content source. |

Google Drive is retired for this project. Do not add Drive links or use Drive as a fallback source.

## What needs a website deployment

An approved change to Supabase teaching content appears automatically in the viewer. A website deployment is needed only when changing the interface, shared access behaviour, a resource-link mapping, cover availability, or the file-serving code.

The deployment must remain small. Do not package the complete PDF or cover collection with the website. The existing protected file store contains 16 original/text-only PDFs for *Crickwing*, *Night Tree*, *The Alphabet Tree*, *Little Blue and Little Yellow*, *Owl Moon*, *The Gruffalo*, *The Boy Who Loved Words* and *Fox*, plus 222 catalogue covers.

## Add or revise a staff-served book file

1. Commit the verified original PDF, clean text-only PDF, transcript and OCR notes to the matching `book-files/` package in this private repository. This is the canonical record.
2. Check or create the correct cover. It must be an authorised image of the right book or edition, not an inferred substitute.
3. Upload only the changed website objects to the private file store through the authenticated `mentor-library-files` function. Preserve these object paths: `book-files/<slug>/picture-book.pdf`, `book-files/<slug>/text-only.pdf` and `covers/<cover filename>`.
4. Update the viewer resource mapping and checked-cover status only when they changed. Keep browser links relative to the protected site; do not use a direct GitHub, Storage or Drive URL.
5. Deploy the small viewer source. If the hosting archive upload is unavailable, use the hosting service's source-only remote-build fallback instead of rebuilding a large archive.
6. Sign in to the live site and verify the correct cover, **Open picture book PDF** and **Open text-only PDF** links for that book.

The storage bucket is private. The function name, bucket name and object paths can be recorded in project notes; upload, proxy and login values cannot. If the authorised school account cannot access the Sites project, Supabase project or their secure runtime settings, stop and ask a project owner to grant that access rather than weakening the protection.

## Routine deployment sequence

1. Read this file and `docs/CURRENT.md` in GitHub `main`.
2. Make and test the small source change in the Sites deployment source.
3. Push that source with the current Sites write credential.
4. Save and deploy the resulting version through the existing Sites project, keeping the current public audience because the worker itself supplies the school sign-in.
5. Confirm the deployment succeeds, then verify the signed-in live page.

Do not create a second website or replace the shared sign-in with a public site. No automatic GitHub-to-Sites deployment is configured. Institutional ownership handover for Supabase and Sites remains deferred work.
