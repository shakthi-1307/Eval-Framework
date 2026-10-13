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