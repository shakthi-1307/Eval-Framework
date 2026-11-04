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
    
def detect_regression(
    comparison: dict,
    max_latency_increase: float = 0.10,
) -> dict:
    
    accuracy_delta = comparison["accuracy"]["delta"]
    latency_delta = comparison["average_execution_time"]["delta_seconds"]
    
    regressions = []
    
    if accuracy_delta < 0:
        regressions.append("Accuracy decreased")
        
    if accuracy_delta > max_latency_increase:
        regressions.append(
            f"Latency increased by more than {max_latency_increase:.2f}s"
        )
        
    return {
        "regression_detected": bool(regressions),
        "issues": regressions,
    }
    
def compare_test_results(
    baseline_path: str,
    current_path: str,
) -> list[dict]:
    import json
    from pathlib import Path

    with Path(baseline_path).open(encoding="utf-8") as file:
        baseline = json.load(file)

    with Path(current_path).open(encoding="utf-8") as file:
        current = json.load(file)

    baseline_results = {
        result["test_id"]: result
        for result in baseline.get("results", [])
    }

    current_results = {
        result["test_id"]: result
        for result in current.get("results", [])
    }

    comparisons = []

    for test_id in sorted(
        set(baseline_results) | set(current_results)
    ):
        old = baseline_results.get(test_id)
        new = current_results.get(test_id)

        if old is None:
            status = "new_test"
        elif new is None:
            status = "removed_test"
        elif old.get("passed") != new.get("passed"):
            status = "changed"
        else:
            status = "unchanged"

        comparisons.append({
            "test_id": test_id,
            "baseline_passed": old.get("passed") if old else None,
            "current_passed": new.get("passed") if new else None,
            "status": status,
            "baseline_latency" : (
                old.get("execution_time") if old else None
            ),
            "current_latency":(
                new.get("execution_time") if new else None
            ),
            "latency_delta" : (
                round(
                    new["execution_time"] - old["execution_time"],
                    4,
                )
                if old and new
                and old.get("execution_time") is not None
                and new.get("execution_time") is not None
                else None
            ),
        })

    return comparisons

def summarize_test_comparison(comparisons: list[dict]) -> dict:
    valid_latency = [
        item for item in comparisons
        if item.get("current_latency") is not None
    ]
    
    valid_deltas = [
        item for item in comparisons
        if item.get("latency_delta") is not None
    ]
    
    slowest_test = (
        max(valid_latency,key = lambda item: item["current_latency"])
        if valid_latency else None
    )
    
    largest_increase = (
        max(valid_deltas,key = lambda item:item["latency_delta"])
        if valid_deltas else None
    )
    
    return {
        "total_tests_compared": len(comparisons),
        "status_changed":sum(
            item["status"] == "changed" for item in comparisons
        ),
        "became_slower": sum(
            item["latency_delta"] > 0 for item in valid_deltas
        ),
        "became_faster":sum(
            item["latency_delta"] < 0 for item in valid_deltas
        ),
        "unchanged_latency":sum(
            item["latency_delta"] == 0 for item in valid_deltas
        ),
        "slowest_test":(
            {
                "test_id": slowest_test["test_id"],
                "latency_seconds": slowest_test["current_latency"],
            }
            if slowest_test else None
        ),
        "largest_latency_increase":(
            {
                "test_id":largest_increase["test_id"],
                "delta_seconds": largest_increase["latency_delta"],
            }
            if largest_increase
            and largest_increase["latency_delta"] > 0
            else None
        )
    }