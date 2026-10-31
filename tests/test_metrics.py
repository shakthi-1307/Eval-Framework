from evalforge.metrics.exact_match import exact_match 
from evalforge.metrics.accuracy import calculate_accuracy 
from evalforge.models.schemas import ExecutionResult 

def test_exact_match():
    assert exact_match("5","5") is True 
    
def test_exact_match_failure():
    assert exact_match("5","6") is False 
    
def test_accuracy():
    
    results = [
        ExecutionResult(
            test_id = "TC001",
            input="2+3",
            actual_output = "5",
            expected_output = "5",
            passed = True,
            execution_time = 0.1
        ),
        ExecutionResult(
            test_id = "TC002",
            input="4+5",
            actual_output = "10",
            expected_output = "9",
            passed = False,
            execution_time = 0.2
        )
    ]
    
    accuracy = calculate_accuracy(results)
    
    assert accuracy == 0.5
    
def test_empty_results():
    assert calculate_accuracy([]) == 0.0
    
from evalforge.metrics.execution_errors import count_execution_errors


def test_count_execution_errors():
    results = [
        ExecutionResult(
            test_id="TC001",
            input="Question 1",
            actual_output="Answer",
            passed=True,
            execution_time=0.1,
        ),
        ExecutionResult(
            test_id="TC002",
            input="Question 2",
            actual_output=None,
            passed=False,
            error="API timeout",
            execution_time=0.2,
        ),
    ]

    assert count_execution_errors(results) == 1