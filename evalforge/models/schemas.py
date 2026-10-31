from pydantic import BaseModel, Field
from datetime import datetime 
class TestCase(BaseModel):
    __test__ = False
    id: str = Field(min_length=1)
    input: str = Field(min_length=1)
    expected_output: str | None = None
    expected_behavior: list[str] = Field(default_factory = list)
    metadata: dict = Field(default_factory = dict)
    
class ExecutionResult(BaseModel):
    test_id: str
    input: str
    actual_output: str | None = None 
    expected_output:str | None = None
    passed: bool | None = None
    error: str | None = None
    execution_time: float 
    timestamp: datetime = Field(
        default_factory = datetime.now
    )
    
class EvaluationReport(BaseModel):
    dataset_name:str 
    total_tests:int 
    passed_tests:int
    failed_tests:int
    accuracy:float 
    average_execution_time:float 
    total_execution_time:float 
    error_count: int
    