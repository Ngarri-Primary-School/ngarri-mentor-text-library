#!/usr/bin/env python3
"""Deterministic support tools for the Ngarri mentor-text enrichment workflow.

The script records the intake pause, extracts text into an ignored working area,
creates draft scaffolds, and checks curriculum wording and review invariants. It
does not generate literary analysis or publish to Supabase.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from xml.etree import ElementTree


AI_STATUS = "ai_suggested"
REQUIRED_IDEA_FIELDS = (
    "title",
    "linked_focus",
    "suggested_year_levels",
    "where_to_look",
    "learning_focus",
    "teaching_sequence",
    "student_application",
    "notice_learning",
)


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def normalise_books(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict):
        payload = payload.get("books", payload.get("candidates", []))
    if not isinstance(payload, list):
        raise ValueError("Book input must be a JSON list or an object containing 'books'.")
    books = []
    for index, raw in enumerate(payload, 1):
        if not isinstance(raw, dict) or not str(raw.get("title", "")).strip():
            raise ValueError(f"Candidate {index} needs a title.")
        item = dict(raw)
        item["catalogue_id"] = str(raw.get("catalogue_id", raw.get("id", raw.get("row", ""))))
        item["title"] = str(raw["title"]).strip()
        item["author"] = str(raw.get("author", "")).strip()
        item["priority"] = int(raw.get("priority", 0))
        item["selection_reason"] = str(raw.get("selection_reason", "")).strip()
        books.append(item)
    return books


def cmd_new_batch(args: argparse.Namespace) -> int:
    candidates = normalise_books(read_json(args.books))
    excluded = {str(x).casefold() for x in args.exclude}
    eligible = [
        b for b in candidates
        if b["title"].casefold() not in excluded
        and str(b.get("workflow_status", "")).casefold() not in {"complete", "approved", "in_progress"}
    ]
    eligible.sort(key=lambda b: (-b["priority"], b["title"].casefold(), b["author"].casefold()))
    chosen = eligible[: args.count]
    if not chosen:
        raise ValueError("No eligible books remain in the candidate file.")
    if any(not b["selection_reason"] for b in chosen):
        raise ValueError("Every selected candidate needs a selection_reason written by Codex.")

    batch = {
        "schema_version": "1.0",
        "batch_id": args.batch_id,
        "created_at": now_iso(),
        "stage": "awaiting_full_text",
        "instructions": "Pause until the user places these books in the approved Google Drive folder and Codex verifies access to each complete text.",
        "books": [
            {
                "catalogue_id": b["catalogue_id"],
                "title": b["title"],
                "author": b["author"],
                "selection_reason": b["selection_reason"],
                "drive_url": None,
                "drive_file_id": None,
                "file_name": None,
                "access_verified": False,
                "access_verified_at": None,
                "source_sha256": None,
                "source_locator_scheme": None,
                "status": "awaiting_full_text",
            }
            for b in chosen
        ],
    }
    write_json(args.out, batch)
    print("Next enrichment batch")
    for number, book in enumerate(batch["books"], 1):
        author = f" — {book['author']}" if book["author"] else ""
        print(f"{number}. {book['title']}{author}")
        print(f"   Reason: {book['selection_reason']}")
    print("\nPAUSE: wait for the user to place complete texts in the school Google Drive folder.")
    return 0


def find_book(batch: dict[str, Any], identifier: str) -> dict[str, Any]:
    wanted = identifier.casefold()
    matches = [
        b for b in batch.get("books", [])
        if str(b.get("catalogue_id", "")).casefold() == wanted or str(b.get("title", "")).casefold() == wanted
    ]
    if len(matches) != 1:
        raise ValueError(f"Expected one batch book matching {identifier!r}; found {len(matches)}.")
    return matches[0]


def cmd_register_source(args: argparse.Namespace) -> int:
    batch = read_json(args.batch)
    book = find_book(batch, args.book)
    book.update(
        {
            "drive_url": args.drive_url,
            "drive_file_id": args.drive_file_id,
            "file_name": args.file_name,
            "access_verified": bool(args.verified),
            "access_verified_at": now_iso() if args.verified else None,
            "source_sha256": args.sha256,
            "source_locator_scheme": args.locator_scheme,
            "status": "ready_for_analysis" if args.verified else "awaiting_access_verification",
        }
    )
    batch["stage"] = (
        "ready_for_analysis"
        if batch.get("books") and all(b.get("access_verified") for b in batch["books"])
        else "awaiting_full_text"
    )
    batch["updated_at"] = now_iso()
    write_json(args.batch, batch)
    print(f"Recorded source for {book['title']}: {book['status']}")
    print(f"Batch stage: {batch['stage']}")
    return 0


def extract_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        root = ElementTree.fromstring(archive.read("word/document.xml"))
    paragraphs = []
    for paragraph in root.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"):
        text = "".join(node.text or "" for node in paragraph.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"))
        if text.strip():
            paragraphs.append(text.strip())
    return "\n".join(paragraphs)


def extract_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError("PDF extraction needs pypdf. Use Codex's bundled Python runtime or provide a TXT/MD export.") from exc
    pages = []
    for number, page in enumerate(PdfReader(str(path)).pages, 1):
        pages.append(f"[PAGE {number}]\n{page.extract_text() or ''}")
    return "\n\n".join(pages)


def cmd_extract_text(args: argparse.Namespace) -> int:
    raw = args.input.read_bytes()
    suffix = args.input.suffix.casefold()
    if suffix in {".txt", ".md"}:
        text = raw.decode("utf-8-sig")
    elif suffix == ".docx":
        text = extract_docx(args.input)
    elif suffix == ".pdf":
        text = extract_pdf(args.input)
    else:
        raise ValueError("Supported source formats are PDF, DOCX, TXT and MD.")
    clean_lines = [re.sub(r"\s+", " ", line).strip() for line in text.splitlines() if line.strip()]
    located = "\n".join(f"[L{number:04d}] {line}" for number, line in enumerate(clean_lines, 1)) + "\n"
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(located, encoding="utf-8")
    digest = hashlib.sha256(raw).hexdigest()
    print(json.dumps({"output": str(args.out), "source_sha256": digest, "lines": len(clean_lines)}, indent=2))
    return 0


def cmd_make_draft(args: argparse.Namespace) -> int:
    batch = read_json(args.batch)
    book = find_book(batch, args.book)
    if not book.get("access_verified"):
        raise ValueError("The full text must be accessible and verified before a draft is created.")
    draft = {
        "schema_version": "1.0",
        "book": {
            "catalogue_id": book.get("catalogue_id"),
            "title": book.get("title"),
            "author": book.get("author"),
            "text_type": "",
            "genres": [],
            "classification_rationale": "",
            "full_text": {
                "drive_url": book.get("drive_url"),
                "drive_file_id": book.get("drive_file_id"),
                "file_name": book.get("file_name"),
                "access_verified_at": book.get("access_verified_at"),
                "source_sha256": book.get("source_sha256"),
                "locator_scheme": book.get("source_locator_scheme"),
            },
        },
        "writing": [],
        "reading": [],
        "pride": [],
        "inquiry": [],
        "teaching_ideas": [],
        "review": {"status": AI_STATUS, "reviewed_by": None, "reviewed_at": None},
    }
    write_json(args.out, draft)
    print(f"Created AI-draft scaffold for {book['title']} at {args.out}")
    return 0


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_curriculum_entry(entry: dict[str, Any], records: dict[str, dict[str, Any]], label: str, errors: list[str]) -> None:
    ref = str(entry.get("curriculum_reference_id", ""))
    record = records.get(ref)
    if not record:
        errors.append(f"{label}: unknown curriculum_reference_id {ref!r}")
        return
    if entry.get("year_level") != record.get("year_label"):
        errors.append(f"{label}: year_level does not exactly match {ref}")
    if entry.get("focus") != record.get("section"):
        errors.append(f"{label}: focus does not exactly match {ref}")
    if entry.get("key_understanding") not in record.get("key_understandings", []):
        errors.append(f"{label}: Key Understanding is not verbatim in {ref}")
    skill = entry.get("key_skill")
    if skill not in (None, "") and skill not in record.get("key_skills", []):
        errors.append(f"{label}: Key Skill is not verbatim in {ref}")
    for field in ("where_to_look", "explanation"):
        if not nonempty(entry.get(field)):
            errors.append(f"{label}: missing {field}")
    if entry.get("status") != AI_STATUS:
        errors.append(f"{label}: new content must have status {AI_STATUS!r}")


def cmd_validate(args: argparse.Namespace) -> int:
    draft = read_json(args.draft)
    curriculum_list = read_json(args.curriculum)
    records = {r["reference_id"]: r for r in curriculum_list}
    errors: list[str] = []
    warnings: list[str] = []
    book = draft.get("book", {})
    for field in ("title", "author", "text_type", "classification_rationale"):
        if not nonempty(book.get(field)):
            errors.append(f"book: missing {field}")
    if (
        not isinstance(book.get("genres"), list)
        or not book.get("genres")
        or not all(nonempty(x) for x in book.get("genres", []))
    ):
        errors.append("book: genres must contain at least one non-empty genre")
    source = book.get("full_text", {})
    if not nonempty(source.get("drive_url")) or not nonempty(source.get("access_verified_at")):
        errors.append("book: verified Google Drive source is required")

    for category in ("writing", "reading"):
        seen: set[tuple[str, str]] = set()
        for index, entry in enumerate(draft.get(category, []), 1):
            label = f"{category}[{index}]"
            validate_curriculum_entry(entry, records, label, errors)
            key = (str(entry.get("focus", "")), str(entry.get("year_level", "")))
            if key in seen:
                errors.append(f"{label}: duplicate focus/year combination {key}")
            seen.add(key)

    for category in ("pride", "inquiry"):
        for index, entry in enumerate(draft.get(category, []), 1):
            label = f"{category}[{index}]"
            for field in ("concept", "where_to_look", "explanation"):
                if not nonempty(entry.get(field)):
                    errors.append(f"{label}: missing {field}")
            if entry.get("status") != AI_STATUS:
                errors.append(f"{label}: new content must have status {AI_STATUS!r}")

    for index, idea in enumerate(draft.get("teaching_ideas", []), 1):
        label = f"teaching_ideas[{index}]"
        for field in REQUIRED_IDEA_FIELDS:
            value = idea.get(field)
            if field == "suggested_year_levels":
                if not isinstance(value, list) or not value:
                    errors.append(f"{label}: missing {field}")
            elif not nonempty(value):
                errors.append(f"{label}: missing {field}")
        if idea.get("status") != AI_STATUS:
            errors.append(f"{label}: new content must have status {AI_STATUS!r}")

    if not draft.get("writing"):
        warnings.append("No writing connections selected; this is allowed only when the book has no strong match.")
    if not draft.get("reading"):
        warnings.append("No reading connections selected; this is allowed only when the book has no strong match.")
    if draft.get("review", {}).get("status") != AI_STATUS:
        errors.append("review.status must remain ai_suggested until teacher approval")

    result = {"valid": not errors, "errors": errors, "warnings": warnings}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    commands = root.add_subparsers(dest="command", required=True)

    new = commands.add_parser("new-batch", help="Record the next books and enforce the full-text pause.")
    new.add_argument("--books", type=Path, required=True, help="JSON candidate list prepared from the catalogue.")
    new.add_argument("--out", type=Path, required=True)
    new.add_argument("--batch-id", required=True)
    new.add_argument("--count", type=int, default=5)
    new.add_argument("--exclude", action="append", default=[])
    new.set_defaults(func=cmd_new_batch)

    register = commands.add_parser("register-source", help="Record a Drive text after Codex checks access.")
    register.add_argument("--batch", type=Path, required=True)
    register.add_argument("--book", required=True, help="Catalogue ID or exact title.")
    register.add_argument("--drive-url", required=True)
    register.add_argument("--drive-file-id")
    register.add_argument("--file-name", required=True)
    register.add_argument("--sha256")
    register.add_argument("--locator-scheme", default="page and/or extracted line")
    register.add_argument("--verified", action="store_true")
    register.set_defaults(func=cmd_register_source)

    extract = commands.add_parser("extract-text", help="Create a line-addressable working copy outside Git.")
    extract.add_argument("--input", type=Path, required=True)
    extract.add_argument("--out", type=Path, required=True)
    extract.set_defaults(func=cmd_extract_text)

    draft = commands.add_parser("make-draft", help="Create a blank draft only after full-text verification.")
    draft.add_argument("--batch", type=Path, required=True)
    draft.add_argument("--book", required=True)
    draft.add_argument("--out", type=Path, required=True)
    draft.set_defaults(func=cmd_make_draft)

    validate = commands.add_parser("validate", help="Check a completed AI draft before teacher review.")
    validate.add_argument("--draft", type=Path, required=True)
    validate.add_argument("--curriculum", type=Path, default=Path("curriculum-review-2026-09-06/curriculum-reference-records.json"))
    validate.set_defaults(func=cmd_validate)
    return root


def main() -> int:
    try:
        args = parser().parse_args()
        return args.func(args)
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
