from evalforge.dataset import load_dataset
from evalforge.evaluator import evaluate
import json


def dummy_app(question):
    answers = {
        "What is 2 + 2?": "4",
        "Capital of France?": "Paris",
        "Say hello politely.": "Hello! How are you?",
    }
    return answers.get(question, "I don't know.")


def dummy_judge(prompt):
    return json.dumps({
        "score": 0.95,
        "passed": True,
        "reason": "The response meets the evaluation criteria.",
    })


cases = load_dataset("data/test_cases.jsonl")

results = evaluate(
    test_cases=cases,
    app=dummy_app,
    grader="llm",
    judge=dummy_judge,
)

for execution, grading in results:
    print(execution.test_id, grading.score, grading.passed)