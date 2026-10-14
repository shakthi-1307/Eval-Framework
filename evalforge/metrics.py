
from dataclasses import dataclass

from evalforge.runner import ExecutionResult
from evalforge.graders.code_grader import GradingResult
from evalforge.statistics import wilson_interval


@dataclass
class EvaluationMetrics:
    total_tests: int
    passed_tests: int
    failed_tests: int
    pass_rate: float
    ci_lower: float | None
    ci_upper: float | None
    average_latency_seconds: float


def calculate_metrics(results) -> EvaluationMetrics:
    # Execution errors are not valid grading outcomes.
    attempted = len(results)
    
    valid_results = [
        (execution, grading)
        for execution, grading in results
        if execution.error is None and grading is not None
    ]

    total = len(valid_results)
    passed = sum(
        1 for _, grading in valid_results
        if grading.passed
    )
    failed = total - passed

    pass_rate = passed / total if total else 0.0

    if total:
        ci_lower, ci_upper = wilson_interval(passed, total)
    else:
        ci_lower = ci_upper = None

    latencies = [
        execution.latency_seconds
        for execution, _ in results
        if execution.error is None
    ]

    average_latency = (
        sum(latencies) / len(latencies)
        if latencies else 0.0
    )

    return EvaluationMetrics(
        total_tests=attempted,
        passed_tests=passed,
        failed_tests=failed,
        pass_rate=pass_rate,
        ci_lower=ci_lower,
        ci_upper=ci_upper,
        average_latency_seconds=average_latency,
    )

