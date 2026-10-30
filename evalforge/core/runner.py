import time 
from evalforge.models.schemas import ExecutionResult
from evalforge.core.dataset import EvaluationDataset

class EvaluationRunner:
    def __init__(self,dataset:EvaluationDataset):
        self.dataset = dataset
        
    def run(self,ai_application):
        results = []
        
        for test in self.dataset.test_cases:
            start_time = time.perf_counter()
            
            try:
                output = ai_application(test.input)
                error = None 
                
            except Exception as e:
                output = None 
                error = str(e)
                
            execution_time = time.perf_counter() - start_time 
            
            result = ExecutionResult(
                test_id = test.id,
                input = test.input,
                actual_output = output,
                error = error,
                execution_time = execution_time,
            )
            
            results.append(result)
            
        return results