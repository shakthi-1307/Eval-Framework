import json
from evalforge.reporting.compare import compare_reports

comparison = compare_reports(
    baseline_path="reports/eval_20261031_162034_e2814d8a.json",
    current_path="reports/eval_20261102_232728_7d848920.json",
)

print(json.dumps(comparison, indent=4))