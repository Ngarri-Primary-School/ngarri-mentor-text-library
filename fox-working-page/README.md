# Fox working review page

**Latest: text-checked v3.** The user supplied a four-page text-only Fox PDF. All four pages were read and visually inspected. `build_data.py` now runs `full_text_examples.py`, producing ten individually supported connections: three writing, three reading, Determination, Integrity as counterexample discussion, and two inquiry lenses. All book excerpts are checked during generation. See ../fox-source-review/READING-AND-CONNECTIONS.md. There is no three-item cap. Prior fixtures and browser keys remain preserved; all revised content requires review. Historical revision notes below are superseded by this paragraph.

**Current revision: three specific mentor-text candidates.** The user corrected the generic approach: select only each book's strongest examples, with no requirement to cover every skill, year or domain. `build_data.py` now runs `specific_examples.py`. See MENTOR-TEXT-CORRECTION.md for the selection rule and sources. Two additional possibilities are held in reserve-examples.json; the original eight-item fixture and builder are preserved in history/generic-v1. Revised content uses a new browser-storage key, retaining the old key untouched. The eight-item descriptions and initial verification below describe the earlier prototype and are superseded by this revision.

Local functional calibration prototype, 6 September 2026. Not the production teacher library or a secured reviewer application. No Supabase connection, API keys, paid generation or catalogue writes.

Run `build_data.py` with Python to rebuild the eight draft items from preserved references, then serve this directory only on loopback using `python -m http.server 8765 --bind 127.0.0.1`. Open http://127.0.0.1:8765/. No installation is needed. Fonts use the documented families when installed, with local fallbacks; no external font requests are made.

## Acceptance checks

- All suggestions begin pending. A teacher preview displays only locally approved items.
- Approval requires reviewer name, nonempty content, evidence notes and confirmation that the whole item was checked.
- Editing teaching text or evidence invalidates the affected approval. Omission removes the item from the preview.
- Curriculum quotations are separate from editable AI teaching suggestions.
- Reload preserves review state when browser storage is available. Storage errors are reported.
- Export preserves each original suggestion, source identifiers, current edits, review decisions and approval history.
- Layout supports a narrow phone viewport and keyboard controls. Content is rendered with text nodes, not injected HTML.

These rules cover reading, writing, oral language, values and inquiry items. A generic activity with no checked book evidence must remain pending. The reusable decision rules belong to the local review controller (`app.js`), while the book and suggestions are a separate fixture (`data.json`). No title-specific review exception exists.

## Sources and deliberate limits

Content is derived from `../fox-content-review/FOX-REVIEW.md` and its curriculum addendum. Five new curriculum quotations are checked during fixture generation against exact source records. The original source documents remain untouched. The older writing/value/lens excerpts retain their recovered-source identity and review limitations.

Base colour values come from the preserved `book-detail-v5.html` prototype. That file's title is Bowerbird Blues despite its association with the Fox design history; only its styling conventions are reused. The vault's Visual Direction and Screen Specs guide semantic colours, typography, purpose-first content and accessible controls. This layout is a provisional local implementation, not a finalised design system. The tall sticky hero is not reproduced on this review page, to keep review controls and content accessible on smaller screens.

No verified cover or blurb is supplied; a clearly labelled cover placeholder is shown. No related books or unverified resources are invented. Organisation/pacing stays in the original pending review document. Teaching ideas and their curriculum links are reviewed together as complete items in this first prototype; a production workflow will need separate entities and dependency checks where links and ideas are approved independently.

Browser storage and a preview toggle are not access controls. Do not deploy this prototype as a teacher site: all draft data is delivered to this local browser. Production needs authenticated reviewer access and server-enforced publication rules. Local approval neither changes the live database nor implies approval of a bulk run. Downloaded JSON is a review record, not an automatic import file.
