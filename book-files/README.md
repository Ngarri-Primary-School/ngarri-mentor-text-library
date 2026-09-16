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
        └── Book Title - checked text-only.pdf
```

Use the title and creator in each path so editions remain identifiable. Add a concise note beside a file only when an edition, source or transcription check needs explanation.

## Adding a file

1. Confirm that the school has approved the file for this private repository.
2. Check the file size before adding it. Files below 100 MiB may be committed with ordinary Git.
3. Do not add a file of 100 MiB or more until Git LFS is installed and configured for PDFs. Record that decision in the relevant book's review or source record.
4. Commit the file with its title, edition or source details in the commit message.
5. When a website resource link changes, update its mapping and verify the authenticated viewer.

Keep credentials out of this folder and preserve the school's current access decisions.
