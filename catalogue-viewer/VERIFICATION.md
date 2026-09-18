# Viewer verification record

Updated: 18 September 2026

## Current checks

- The live viewer reads approved Supabase records and refreshes automatically.
- The shared school-group sign-in protects the viewer and all served covers and PDFs.
- The private `mentor-library-files` store contains 238 objects: 16 original/text-only PDFs for the eight linked books and 222 covers.
- The live Fox card shows its correct checked cover, and its picture-book and text-only PDF buttons point to protected `/book-files/fox/...` paths.
- The website deployment no longer contains the PDF or cover collection. Future updates upload only changed objects and deploy a small viewer source change when mapping or interface work is needed.

## Required check after a book update

1. Confirm the approved Supabase record shows the expected content and status.
2. Sign in to the shared site.
3. Search for the book and confirm its title, author, blurb, cover and year-band display.
4. Open both PDF buttons and confirm each leads to the intended protected file.
5. Check that the new or revised content appears only after teacher approval.

Older viewer counts and early interface checks are historical evidence in Git history and `archive/`; they are not current operating instructions.
