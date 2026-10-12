from evalforge.models import TestCase 
from evalforge.runner import run_test, ExecutionResult
from evalforge.graders.code_grader import exact_match,GradingResult

def evaluate(test_cases:list[TestCase],app) -> list[tuple[ExecutionResult,GradingResult]]:
    results = []
    
    for test_case in test_cases:
        execution = run_test(test_case,app)
        
        grading = exact_match(
            test_id = test_case.test_id,
            expected = test_case.expected_output,
            actual = execution.actual_output
        )
        
        results.append((execution,grading))
        
    return results