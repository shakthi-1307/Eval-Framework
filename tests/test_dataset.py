
import json
import tempfile
import unittest
from pathlib import Path

from evalforge.dataset import load_dataset


class TestDataset(unittest.TestCase):

    def load_temp_dataset(self, content):
        temp_file = tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            suffix=".jsonl",
            delete=False,
        )
        with temp_file:
            temp_file.write(content)

        self.addCleanup(Path(temp_file.name).unlink, missing_ok=True)
        return load_dataset(temp_file.name)

    def test_valid_dataset(self):
        content = json.dumps({
            "test_id": "TC001",
            "input": "What is 2 + 2?",
            "expected_output": "4",
            "tags": ["math"],
        }) + "\n"

        cases = self.load_temp_dataset(content)

        self.assertEqual(len(cases), 1)
        self.assertEqual(cases[0].tags, ["math"])

    def test_missing_required_field(self):
        content = json.dumps({
            "test_id": "TC001",
            "input": "What is 2 + 2?",
        }) + "\n"

        with self.assertRaisesRegex(ValueError, "missing fields"):
            self.load_temp_dataset(content)

    def test_invalid_json(self):
        with self.assertRaisesRegex(ValueError, "Invalid JSON"):
            self.load_temp_dataset('{"test_id": invalid}\n')

    def test_tags_must_be_a_list(self):
        content = json.dumps({
            "test_id": "TC001",
            "input": "What is 2 + 2?",
            "expected_output": "4",
            "tags": "math",
        }) + "\n"

        with self.assertRaisesRegex(ValueError, "tags must be a list"):
            self.load_temp_dataset(content)


if __name__ == "__main__":
    unittest.main()
