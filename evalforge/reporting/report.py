from evalforge.models.schemas import EvaluationReport


def generate_report(dataset_name, results):

    total = len(results)

    passed = sum(
        1 for result in results
        if result.passed is True
    )

    failed = sum(
        1 for result in results
        if result.passed is False
    )

    total_time = sum(
        result.execution_time for result in results
    )

    average_time = (
        round(total_time / total, 2) if total > 0 else 0.0
    )

    accuracy = (
        passed / total if total > 0 else 0.0
    )

    return EvaluationReport(
        dataset_name=dataset_name,
        total_tests=total,
        passed_tests=passed,
        failed_tests=failed,
        accuracy=accuracy,
        average_execution_time=average_time,
        total_execution_time=total_time
    )