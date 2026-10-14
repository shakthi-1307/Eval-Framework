from evalforge.evaluator import evaluate 
from evalforge.metrics import calculate_metrics 

def compare_version(test_cases,app_a,app_b):
    results_a = evaluate(test_cases,app_a)
    results_b = evaluate(test_cases,app_b)
    
    metrics_a = calculate_metrics(results_a)
    metrics_b = calculate_metrics(results_b)
    
    return {
        "version_a": {
            "results": results_a,
            "metrics": metrics_a,
        },
        "version_b": {
            "results": results_b,
            "metrics": metrics_b,
        },
        "pass_rate_difference": (
            metrics_b.pass_rate - metrics_a.pass_rate
        ),
    }
    

def compare_test_results(results_a, results_b):
    if len(results_a) != len(results_b):
        raise ValueError("Both versions must have the same test count.")

    comparison = []

    for (execution_a, grading_a), (execution_b, grading_b) in zip(
        results_a, results_b
    ):
        if execution_a.test_id != execution_b.test_id:
            raise ValueError("Test IDs must match and be in the same order.")

        if grading_a.passed == grading_b.passed:
            status = "unchanged"
        elif grading_b.passed:
            status = "improved"
        else:
            status = "regressed"

        comparison.append({
            "test_id": execution_a.test_id,
            "version_a_passed": grading_a.passed,
            "version_b_passed": grading_b.passed,
            "status": status,
        })

    return comparison
