import importlib.util
import json
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("mentor_pipeline", ROOT / "scripts" / "mentor_pipeline.py")
PIPELINE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(PIPELINE)


class MentorPipelineTests(unittest.TestCase):
    def test_batch_pauses_and_requires_selection_reasons(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            candidates = base / "candidates.json"
            batch = base / "batch.json"
            candidates.write_text(json.dumps([
                {"id": "2", "title": "Second", "author": "B", "priority": 1, "selection_reason": "Broadens genre coverage."},
                {"id": "1", "title": "First", "author": "A", "priority": 2, "selection_reason": "Fills an upper-primary gap."},
            ]), encoding="utf-8")
            args = Namespace(books=candidates, out=batch, batch_id="test", count=1, exclude=[])
            self.assertEqual(PIPELINE.cmd_new_batch(args), 0)
            saved = json.loads(batch.read_text(encoding="utf-8"))
            self.assertEqual(saved["stage"], "awaiting_full_text")
            self.assertEqual(saved["books"][0]["title"], "First")
            self.assertFalse(saved["books"][0]["access_verified"])

    def test_draft_cannot_be_created_before_access_verification(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            batch = base / "batch.json"
            batch.write_text(json.dumps({"books": [{"catalogue_id": "1", "title": "Book", "access_verified": False}]}), encoding="utf-8")
            with self.assertRaises(ValueError):
                PIPELINE.cmd_make_draft(Namespace(batch=batch, book="1", out=base / "draft.json"))

    def test_validator_accepts_exact_curriculum_wording_and_classification(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            curriculum = base / "curriculum.json"
            draft = base / "draft.json"
            curriculum.write_text(json.dumps([{
                "reference_id": "source:1",
                "section": "Ideas",
                "year_label": "Year Three",
                "key_understandings": ["Ideas can be developed."],
                "key_skills": ["I can elaborate an idea."],
            }]), encoding="utf-8")
            draft.write_text(json.dumps({
                "book": {
                    "title": "Book", "author": "Author", "text_type": "Narrative",
                    "genres": ["Fable"], "classification_rationale": "The story uses animal characters to explore a moral choice.",
                    "full_text": {"drive_url": "https://drive.google.com/file/d/example", "access_verified_at": "2026-09-08T00:00:00+00:00"},
                },
                "writing": [{
                    "focus": "Ideas", "year_level": "Year Three", "key_understanding": "Ideas can be developed.",
                    "key_skill": "I can elaborate an idea.", "curriculum_reference_id": "source:1",
                    "where_to_look": "The turning point where the character returns the object.",
                    "explanation": "The repeated attempts make the final choice a clear example of elaborating one central idea.",
                    "status": "ai_suggested",
                }],
                "reading": [], "pride": [], "inquiry": [], "teaching_ideas": [],
                "review": {"status": "ai_suggested"},
            }), encoding="utf-8")
            result = PIPELINE.cmd_validate(Namespace(draft=draft, curriculum=curriculum))
            self.assertEqual(result, 0)

    def test_validator_rejects_missing_genre(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            curriculum = base / "curriculum.json"
            draft = base / "draft.json"
            curriculum.write_text("[]", encoding="utf-8")
            draft.write_text(json.dumps({
                "book": {
                    "title": "Book", "author": "Author", "text_type": "Narrative",
                    "genres": [], "classification_rationale": "A narrative classification based on the complete story.",
                    "full_text": {"drive_url": "https://drive.google.com/file/d/example", "access_verified_at": "2026-09-08T00:00:00+00:00"},
                },
                "writing": [], "reading": [], "pride": [], "inquiry": [], "teaching_ideas": [],
                "review": {"status": "ai_suggested"},
            }), encoding="utf-8")
            result = PIPELINE.cmd_validate(Namespace(draft=draft, curriculum=curriculum))
            self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
