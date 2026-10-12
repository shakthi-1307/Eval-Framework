from dataclasses import dataclass, field 

@dataclass
class TestCase:
    test_id: str 
    input: str
    expected_output: str
    tags: list[str] = field(default_factory = list)
    grading_criteria: str|None = None 
    
@dataclass
class EvaluationResult:
    test_id: str
    input: str
    expected_output: str 
    actual_output: str|None
    score: float|None
    passed: bool|None 
    latency_seconds:float|None 
    error: str|None 
    
    