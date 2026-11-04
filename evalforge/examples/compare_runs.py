import json
from evalforge.reporting.compare import compare_reports,detect_regression

comparison = compare_reports(
    baseline_path="reports/eval_20261031_162034_e2814d8a.json",
    current_path="reports/eval_20261102_232728_7d848920.json",
)

regression = detect_regression(
    comparison,
    max_latency_increase = 0.10,
)

print("Comparison:")
print(json.dumps(comparison, indent = 4))
print("\nRegression Check:")
print(json.dumps(regression,indent = 4))

from evalforge.reporting.compare import compare_test_results

test_comparison = compare_test_results(
    baseline_path="reports/eval_20261103_131353_b86a1213.json",
    current_path="reports/eval_20261103_131401_9ded46c9.json",
)

print(json.dumps(test_comparison, indent=4))

from evalforge.reporting.compare import summarize_test_comparison

summary = summarize_test_comparison(test_comparison)
print("\nTest Comparison Summary : ")
print(json.dumps(summary, indent = 4))
