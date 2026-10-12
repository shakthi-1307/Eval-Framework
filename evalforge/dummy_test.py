from evalforge.dataset import load_dataset
from evalforge.evaluator import evaluate


def dummy_app(question):
    answers = {
        "What is 2 + 2?": "4",
        "Capital of France?": "Paris",
        "Say hello politely.": "Hello! How are you?",
    }
    return answers.get(question, "I don't know.")


cases = load_dataset("data/test_cases.jsonl")
results = evaluate(cases, dummy_app)

for execution, grading in results:
    print(
        execution.test_id,
        grading.score,
        grading.passed,
        grading.reason,
    )