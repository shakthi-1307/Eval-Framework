
from dataclasses import dataclass

from evalforge.runner import ExecutionResult
from evalforge.graders.code_grader import GradingResult


@dataclass
class EvaluationMetrics:
    total_tests: int
    passed_tests: int
    failed_tests: int
    pass_rate: float
    average_latency_seconds: float


def calculate_metrics(results) -> EvaluationMetrics:
    total = len(results)

    passed = sum(
        1 for execution, grading in results
        if grading.passed
    )

    failed = total - passed

    pass_rate = passed / total if total else 0.0

    latencies = [
        execution.latency_seconds
        for execution, grading in results
        if execution.error is None
    ]

    average_latency = (
        sum(latencies) / len(latencies)
        if latencies else 0.0
    )

    return EvaluationMetrics(
        total_tests=total,
        passed_tests=passed,
        failed_tests=failed,
        pass_rate=pass_rate,
        average_latency_seconds=average_latency,
    )
