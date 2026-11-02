import json 
from evalforge.reporting.compare import compare_reports 

comparison = compare_reports(
    baseline_path = "reports/baseline.json",
    current_path = "reports/current.json",
)

print(json.dumps(comparison, indent = 4))