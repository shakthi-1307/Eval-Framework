from evalforge.models.schemas import ExecutionResult 

def count_execution_errors(results: list[ExecutionResult]) -> int:
    return sum(1 for result in results if result.error is not None)