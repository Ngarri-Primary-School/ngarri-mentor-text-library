# School Codex continuation prompt

Copy the following prompt into the school Codex or ChatGPT account after it has access to the private Ngarri GitHub repository and the authorised school Supabase and Sites connections.

```text
Continue the Ngarri Mentor Text Library project from the private GitHub repository:
https://github.com/Ngarri-Primary-School/ngarri-mentor-text-library

Treat GitHub main as the sole documentation and project-file source of truth. Treat archive/ as historical evidence only. Google Drive is retired for this project: do not use, create or request Drive links.

Before changing anything, read in this order:
1. README.md
2. AGENTS.md
3. docs/CURRENT.md
4. the guide named there for the requested task
5. catalogue-viewer/HOSTING.md for any website, cover or PDF-link work
6. .codex/skills/ngarri-mentor-text-enrichment/SKILL.md for any book-content work.

Then reply in plain teacher-friendly language with:
- the current completed books and the immediate next book/action;
- where canonical books, text-only PDFs, review notes, approved content, website files and credentials live;
- which authorised services you can access; and
- any access gap that prevents publication or website work.

Do not start a new book or make changes until I ask you to continue.

Core rules:
- Complete school PDFs, checked transcripts, clean text-only PDFs and OCR notes live in book-files/ in the private repository. Check existing JimK and book-files text resources before extracting from a PDF.
- Work in small announced batches, but complete and show one book at a time. Every AI-created record stays ai_suggested until I approve the complete draft.
- Use exact Ngarri curriculum wording. Select only strong, distinct, book-specific connections supported by a passage, event, language choice or verified illustration. Use relevant installed education skills for teaching ideas.
- Do not publish unreviewed AI content, run paid or bulk enrichment, or deploy database migrations.
- Check each revised book's metadata, text type, genre, year band, correct cover, original-PDF link and clean text-only-PDF link.
- The staff website is https://ngarri-mentor-library-progress.velveteen.chatgpt.site/. It has a shared school-group sign-in. Keep all credentials out of chat, GitHub, source code and documents.
- Supabase holds approved teaching content. The private mentor-library-files store holds served PDFs and covers. The website proxies those files after sign-in; do not expose direct GitHub, Storage or Drive links.
- For file or viewer changes, follow catalogue-viewer/HOSTING.md. Upload only changed PDFs/covers to the private store and keep website deployments small. If you lack authorised access to Sites, Supabase or secure runtime settings, say so and ask for access; do not weaken protection or create another site.
```

The school account needs access to the private GitHub repository, the existing Supabase project and the existing Sites project to make an end-to-end change. The prompt cannot grant those permissions.
