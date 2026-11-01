from evalforge.models.schemas import EvaluationReport
from evalforge.metrics.execution_errors import count_execution_errors
from datetime import datetime 
from uuid import uuid4 
from pydantic import BaseModel, Field 

class EvaluationReport(BaseModel):
    dataset_name:str 
    total_tests:int 
    passed_tests:int
    failed_tests:int
    accuracy:float 
    average_execution_time:float 
    total_execution_time:float 
    error_count: int
    run_id: str = Field(default_factory = lambda: str(uuid4()))
    generated_at: datetime = Field(default_factory = datetime.now)
    
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
    
    error_count = count_execution_errors(results)

    return EvaluationReport(
        dataset_name=dataset_name,
        total_tests=total,
        passed_tests=passed,
        failed_tests=failed,
        accuracy=accuracy,
        average_execution_time=average_time,
        total_execution_time=total_time,
        error_count=error_count,
    )