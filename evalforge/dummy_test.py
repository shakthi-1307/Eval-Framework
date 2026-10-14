
import json

from evalforge.dataset import load_dataset
from evalforge.graders.llm_grader import llm_grade


def dummy_judge(prompt: str) -> str:
    # Simulates a judge returning structured JSON.
    return json.dumps({
        "score": 0.95,
        "passed": True,
        "reason": "The response satisfies the grading criteria."
    })


cases = load_dataset("data/test_cases.jsonl")

test_case = cases[2]
actual_output = "Hello! How are you?"

result = llm_grade(
    test_case=test_case,
    actual_output=actual_output,
    judge=dummy_judge,
)

print(result)

