from evalforge.models.schemas import ExecutionResult
from evalforge.reporting.report import generate_report


def test_generate_report():

    results = [
        ExecutionResult(
            test_id="TC001",
            input="2+3",
            actual_output="5",
            expected_output="5",
            passed=True,
            execution_time=0.2
        ),
        ExecutionResult(
            test_id="TC002",
            input="4+5",
            actual_output="10",
            expected_output="9",
            passed=False,
            execution_time=0.4
        )
    ]

    report = generate_report("Math Tests", results)

    assert report.total_tests == 2
    assert report.passed_tests == 1
    assert report.failed_tests == 1
    assert report.accuracy == 0.5
    assert report.average_execution_time == 0.3


def test_empty_report():

    report = generate_report("Empty Dataset", [])

    assert report.total_tests == 0
    assert report.accuracy == 0.0
    assert report.average_execution_time == 0.0