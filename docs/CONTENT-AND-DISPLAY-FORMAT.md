# Canonical content and book-page format

Updated: 8 September 2026  
Status: approved through the complete-text picture-book pilot

This is the current specification for creating, reviewing, storing and displaying mentor-text content. It supersedes conflicting quotas or presentation instructions in the dated Obsidian snapshot. The snapshot remains unchanged as a provenance record.

## Selection standard

- Work from the complete book text and verified illustrations where available. Do not infer a book-specific claim from its title or blurb alone.
- Select all strong, distinct connections supported particularly well by the book. There is no fixed number of connections and no requirement to cover every framework, trait, strategy, value, lens or year level.
- Every explanation identifies a specific passage, language choice, event or verified visual feature and explains why it is a useful mentor example.
- Reject explanations that could be transferred to almost any book by replacing the title.
- Keep source facts, short quotations, interpretation and newly designed activities distinguishable. Do not publish copyrighted full texts.

## Book classification and source access

Every enriched book records its broad **text type**, one or more specific **genres**, and a short classification rationale grounded in the complete work. These fields are part of teacher review rather than catalogue decoration.

Before analysis, Codex names the next small batch and pauses while the user places the complete texts in the restricted school Google Drive. Codex must verify it can read every selected file. The teacher library may later link authorised staff to the school copy, but the public progress viewer must not expose restricted full-text links.

## Writing connections

Organise entries in this order:

1. Writing trait.
2. Applicable year levels, from lowest to highest.
3. Under each year level, the exact Key Understanding from the selected Ngarri source.
4. The matching exact Key Skill for that year level.
5. A brief book-specific explanation of how the selected moment or craft choice supports teaching that understanding and skill.

Use one database annotation row for each trait and year-level combination. Preserve the curriculum source and review provenance on every row.

## Reading connections

Use the same hierarchy as writing: reading strategy, then applicable year levels from lowest to highest, then the exact Key Understanding, matching exact Key Skill and book-specific explanation.

If a trusted professional reading supplies a strong matching Key Understanding but no Key Skill, the connection may be used after teacher review. Leave Key Skill empty, identify the professional-reading source and never invent or relabel curriculum wording. The approved Night Tree Visualising connection is the pilot example.

## PRIDE values

PRIDE connections are concept-based and are not divided into year levels. Tag a value only when a specific character choice, relationship, event or consequence lets a teacher explore the meaning of that value. Explain how the value is shown, complicated, absent or repaired in the text. Store counterexamples distinctly so they are not misrepresented as positive embodiment.

## Inquiry lenses

Inquiry connections are concept-based and are not divided into year levels. Explain which important theme, tension or question the book opens for inquiry and how specific events or choices in the text support that exploration. A mentor text can provide an entry point into inquiry without becoming a compulsory full inquiry unit.

## Teaching ideas

Teaching ideas sit in their own section after the curriculum, PRIDE and inquiry connections. Each idea contains, where applicable:

- title;
- linked focus;
- suggested year levels;
- time, grouping and difficulty;
- where to look in the book;
- learning focus;
- teaching sequence;
- student application; and
- what teachers should notice in student learning.

Teaching ideas must teach through a specific strength of the book and then support transfer into students' reading, discussion or writing.

## Review and visibility

AI-generated records use `ai_suggested` status and remain visible only to authorised reviewers. They do not appear in the public teacher library or influence its filters. After a reviewer approves them, store the reviewer and review time and change their status to `teacher_reviewed`; the shared progress viewer then displays them from Supabase.

## Collapsible book-page display

Book details are progressive and collapsed by default:

- the blurb opens and closes;
- each writing trait opens to reveal its year levels, and each year level opens to reveal curriculum wording and the book-specific explanation;
- each reading strategy uses the same two-level pattern;
- each PRIDE value and inquiry lens opens to reveal its concept-based explanation without a year-level layer; and
- each teaching idea opens independently to reveal its classroom detail.

Use clear directional controls, keyboard-operable native disclosure behaviour and semantic colours for writing, reading, PRIDE and inquiry. Preserve this hierarchy on desktop and small screens.

## Approved reference implementation

The five approved complete-text pilot books are Crickwing, Night Tree, The Alphabet Tree, Little Blue and Little Yellow, and The Gruffalo. Their teacher-reviewed Supabase records and the live shared viewer demonstrate the expected content and display structure:

https://ngarri-mentor-library-progress.velveteen.chatgpt.site/


