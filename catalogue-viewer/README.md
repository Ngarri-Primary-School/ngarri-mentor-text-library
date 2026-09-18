# Catalogue viewer

The shared progress viewer lets authorised school staff search the mentor-text catalogue and inspect approved writing, reading, PRIDE, inquiry and teaching-idea content. It reads approved records from Supabase and refreshes them automatically.

The tracked files in this folder are a project reference and local-development aid. The live site uses its separate Sites deployment source. For all live changes, file links, covers, access settings and deployment steps, read `catalogue-viewer/HOSTING.md` first.

Key behaviour:

- The blurb appears in the book header beside the cover and "Why use this book?" panel.
- Writing and reading open by trait or strategy, then by year level.
- PRIDE and inquiry open directly to their connection.
- Search filters include title/author, writing, reading, PRIDE, inquiry, information availability and year band.
- Approved content comes from Supabase. Draft `ai_suggested` content must remain hidden from staff.
- Covers and PDFs are served through the shared-password site from the private file store. Do not use direct Drive, GitHub or Storage links.
