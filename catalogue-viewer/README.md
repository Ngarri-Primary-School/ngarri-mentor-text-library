# Catalogue viewer

Simple read-only inspection interface for the current active-book catalogue. Search title/author; combine writing, reading, PRIDE, inquiry and information-availability filters. Open a book to see the blurb, cover and approved connections with their recorded source/status. The hosted viewer reads Supabase directly and checks for approved changes every 15 seconds.

Run with Python 3 (no packages required):

```powershell
python catalogue-viewer/server.py --covers "C:/Users/09187270/OneDrive - Department of Education/Documents/Ngarri/Curriculum/Mentor Texts/School Library/Covers"
```

Open http://127.0.0.1:8766/. Existing Fox review remains on port 8765. Cover files are read from their original location without copying or editing them. On another computer supply its covers folder. Missing files are clearly labelled; a cover filename alone is not counted as an available cover.

`data.json` remains a local audit snapshot and is not shipped to the hosted viewer. The browser uses a Supabase publishable key; Row Level Security restricts it to active books and approved or trusted imported content. The key cannot bypass those policies. No writes or approval actions are available through this interface.

Static cover files still require a site rebuild when they change. Database content does not: once an approved record is written to Supabase, the hosted viewer discovers it automatically. Fox's separate local calibration review is not yet a catalogue record.

For the protected deployment, run `build_public.py` with both `--covers` and `--book-files`. The build currently packages The Gruffalo's picture-book and searchable text-only PDFs at protected internal URLs. Add later books to the explicit resource mapping only after checking the files and their displayed links.
