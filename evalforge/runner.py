
from dataclasses import dataclass
from time import perf_counter
from typing import Callable

from evalforge.models import TestCase


@dataclass
class ExecutionResult:
    test_id: str
    input: str
    expected_output: str
    actual_output: str | None
    latency_seconds: float
    error: str | None


def run_test(
    test_case: TestCase,
    app: Callable[[str], str],
) -> ExecutionResult:

    start_time = perf_counter()

    try:
        output = app(test_case.input)

        if not isinstance(output, str):
            raise TypeError("AI application must return a string.")

        error = None

    except Exception as exc:
        output = None
        error = f"{type(exc).__name__}: {exc}"

    latency = perf_counter() - start_time

    return ExecutionResult(
        test_id=test_case.test_id,
        input=test_case.input,
        expected_output=test_case.expected_output,
        actual_output=output,
        latency_seconds=latency,
        error=error,
    )
