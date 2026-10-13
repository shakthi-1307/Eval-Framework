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

from evalforge.metrics import calculate_metrics

metrics = calculate_metrics(results)

print("\nEvaluation Summary")
print("------------------")
print("Total:", metrics.total_tests)
print("Passed:", metrics.passed_tests)
print("Failed:", metrics.failed_tests)
print(f"Pass rate: {metrics.pass_rate:.2%}")
print(f"Average latency: {metrics.average_latency_seconds:.6f}s")
print(f"Pass rate: {metrics.pass_rate:.2%}")
print(
    f"95% CI: {metrics.ci_lower:.2%} - "
    f"{metrics.ci_upper:.2%}"
)

from evalforge.storage import save_results

file_path = save_results(results, metrics)

print(f"\nResults saved to: {file_path}")

from evalforge.statistics import wilson_interval

lower, upper = wilson_interval(passed=2, total=3)

print(f"Pass rate: {2/3:.2%}")
print(f"95% CI: {lower:.2%} - {upper:.2%}")