from evalforge.models import TestCase 
from evalforge.runner import run_test, ExecutionResult
from evalforge.graders.code_grader import exact_match,GradingResult
from typing import Callable 
from evalforge.graders.llm_grader import llm_grade 


def evaluate(
    test_cases:list[TestCase],
    app:Callable[[str],str],
    grader:str="code",
    judge:Callable[[str],str] | None = None,
    threshold:float = 0.7,
):
    if grader not in {"code","llm"}:
        raise ValueError("grader must be 'code' or 'llm'.")
    
    if grader == "llm" and judge is None:
        raise ValueError("A judge function is required for LLM grading.")
    
    results = []
    
    for test_case in test_cases:
        execution = run_test(test_case,app)
        
        if execution.error is not None:
            grading = None 
            
        elif grader == "code":
            grading = exact_match(
                test_id = test_case.test_id,
                expected = test_case.expected_output,
                actual = execution.actual_output,
            )
            
        else:
            grading = llm_grade(
                test_case = test_case,
                actual_output = execution.actual_output,
                judge = judge,
                threshold = threshold,
            )
            
        results.append((execution,grading))
        
    return results