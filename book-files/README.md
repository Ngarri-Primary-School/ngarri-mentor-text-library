# School book files

This directory is the in-repository location for school-managed picture-book files and their checked text-only PDFs. It is part of the private Ngarri Mentor Text Library repository.

## Layout

```text
book-files/
├── picture-books/
│   └── author-or-illustrator/
│       └── Book Title - complete school copy.pdf
└── text-only/
    └── author-or-illustrator/
        ├── Book Title - checked text-only.pdf
        ├── Book Title - checked transcript.md
        └── Book Title - OCR review notes.md
```

Use the title and creator in each path so editions remain identifiable. Add a concise note beside a file only when an edition, source or transcription check needs explanation.

The checked text-only PDF is a clean reading copy: it contains only the book title, author, illustrator (when known) and book text. Do not include Markdown syntax, source paths, preparation dates, page maps, visual-evidence notes, OCR confidence statements or workflow instructions. Keep those details in the separate OCR review notes file.

## Adding a file

1. Confirm that the school has approved the file for this private repository.
2. Check the file size before adding it. Files below 100 MiB may be committed with ordinary Git.
3. Do not add a file of 100 MiB or more until Git LFS is installed and configured for PDFs. Record that decision in the relevant book's review or source record.
4. Commit the file with its title, edition or source details in the commit message.
5. When a book is ready for staff links, upload only its changed original PDF, text-only PDF and, if needed, cover to the protected website file store. Keep the repository copy as the canonical source. Follow `catalogue-viewer/HOSTING.md` for object paths, mapping and verification.

Google Drive is not used for this project. Keep credentials out of this folder and preserve the school's current access decisions.
