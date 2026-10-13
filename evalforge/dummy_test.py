from evalforge.dataset import load_dataset


cases = load_dataset("data/test_cases.jsonl")

from evalforge.experiments import compare_version

def version_a(question):
    return "I don't know."

def version_b(question):
    answers = {
        "What is 2 + 2?": "4",
        "Capital of France?": "Paris",
        "Say hello politely.": "A polite greeting",
    }
    return answers.get(question, "I don't know.")

comparison = compare_version(cases, version_a, version_b)

a = comparison["version_a"]["metrics"]
b = comparison["version_b"]["metrics"]

print("\nVersion Comparison")
print("------------------")
print(f"Version A: {a.pass_rate:.2%}")
print(f"Version B: {b.pass_rate:.2%}")
print(
    "Improvement: "
    f"{comparison['pass_rate_difference']:+.2%}"
)
