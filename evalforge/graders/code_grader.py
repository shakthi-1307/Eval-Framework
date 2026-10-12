from dataclasses import dataclass 

@dataclass 
class GradingResult:
    test_id: str 
    score: float 
    passed: bool 
    reason: str 
    
def exact_match(test_id:str,expected:str,actual:str|None) -> GradingResult:
    if actual is None:
        return GradingResult(
            test_id = test_id,
            score = 0.0,
            passed = False,
            reason = "No output avaiable to grade.",
        )
        
    passed = actual.strip() == expected.strip()
    
    return GradingResult(
        test_id = test_id,
        score = 1.0 if passed else 0.0,
        passed = passed,
        reason = "Exact match." if passed else "Output does not match expected output."
    )
    