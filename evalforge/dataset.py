
import json
from pathlib import Path

from evalforge.models import TestCase


def load_dataset(file_path: str | Path) -> list[TestCase]:
    path = Path(file_path)
    test_cases = []
    seen_ids = set()

    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue

            try:
                data = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"Invalid JSON on line {line_number}: {exc.msg}"
                ) from exc

            if not isinstance(data, dict):
                raise ValueError(
                    f"Line {line_number}: each test case must be a JSON object."
                )

            required = {"test_id", "input", "expected_output"}
            missing = required - data.keys()

            if missing:
                raise ValueError(
                    f"Line {line_number}: missing fields {sorted(missing)}"
                )

            allowed = required | {"tags", "grading_criteria"}
            unknown = data.keys() - allowed

            if unknown:
                raise ValueError(
                    f"Line {line_number}: unknown fields {sorted(unknown)}"
                )

            test_id = data["test_id"]
            user_input = data["input"]
            expected = data["expected_output"]
            tags = data.get("tags", [])
            criteria = data.get("grading_criteria")

            if not isinstance(test_id, str) or not test_id.strip():
                raise ValueError(
                    f"Line {line_number}: test_id must be a non-empty string."
                )

            if test_id in seen_ids:
                raise ValueError(
                    f"Line {line_number}: duplicate test_id '{test_id}'."
                )

            if not isinstance(user_input, str) or not user_input.strip():
                raise ValueError(
                    f"Line {line_number}: input must be a non-empty string."
                )

            if not isinstance(expected, str):
                raise ValueError(
                    f"Line {line_number}: expected_output must be a string."
                )

            if (
                not isinstance(tags, list)
                or not all(isinstance(tag, str) for tag in tags)
            ):
                raise ValueError(
                    f"Line {line_number}: tags must be a list of strings."
                )

            if criteria is not None and not isinstance(criteria, str):
                raise ValueError(
                    f"Line {line_number}: grading_criteria must be a string or null."
                )

            test_cases.append(
                TestCase(
                    test_id=test_id,
                    input=user_input,
                    expected_output=expected,
                    tags=tags,
                    grading_criteria=criteria,
                )
            )
            seen_ids.add(test_id)

    if not test_cases:
        raise ValueError("The dataset contains no test cases.")

    return test_cases
