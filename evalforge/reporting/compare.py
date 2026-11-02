import json
from pathlib import Path


def compare_reports(
    baseline_path: str,
    current_path: str,
) -> dict:
    with Path(baseline_path).open(encoding="utf-8") as file:
        baseline = json.load(file)

    with Path(current_path).open(encoding="utf-8") as file:
        current = json.load(file)

    accuracy_delta = current["accuracy"] - baseline["accuracy"]
    latency_delta = (
        current["average_execution_time"]
        - baseline["average_execution_time"]
    )

    return {
        "baseline_run": baseline.get("run_id"),
        "current_run": current.get("run_id"),
        "accuracy": {
            "baseline": baseline["accuracy"],
            "current": current["accuracy"],
            "delta": round(accuracy_delta, 4),
        },
        "average_execution_time": {
            "baseline": baseline["average_execution_time"],
            "current": current["average_execution_time"],
            "delta_seconds": round(latency_delta, 4),
        },
    }