# Catalogue viewer

Simple read-only inspection interface for the current active-book catalogue. Search title/author; combine writing, reading, PRIDE, inquiry and information-availability filters. Open a book to see the blurb, cover and existing connections with their recorded source/status. Empty explanations are explicitly identified. This is a dated snapshot, not an automatically live application or the production teacher library.

Run with Python 3 (no packages required):

```powershell
python catalogue-viewer/server.py --covers "C:/Users/09187270/OneDrive - Department of Education/Documents/Ngarri/Curriculum/Mentor Texts/School Library/Covers"
```

Open http://127.0.0.1:8766/. Existing Fox review remains on port 8765. Cover files are read from their original location without copying or editing them. On another computer supply its covers folder. Missing files are clearly labelled; a cover filename alone is not counted as an available cover.

`data.json` is a curated snapshot checked against Supabase on 7 September 2026. The local raw query result is excluded from Git. To refresh, an authorised assistant can perform the read-only query against the same public tables, save `source-snapshot.json`, then run `build.py`. No database keys are embedded or required to view the snapshot. No writes, approval actions or database policy changes are implemented. This inspection tool is for the project owner; do not publicly deploy the snapshot as the teacher library.

Current scope: 343 active books, 391 writing links, 260 reading links, no PRIDE/inquiry/teaching idea records. Fox's separate local calibration review is not a catalogue record. Definitions of the PRIDE values and lenses are not counted as book connections.
