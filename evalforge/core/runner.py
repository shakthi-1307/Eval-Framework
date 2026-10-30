import time 
from evalforge.models.schemas import ExecutionResult
from evalforge.core.dataset import EvaluationDataset
from evalforge.metrics.exact_match import exact_match

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
                passed = None
                if test.expected_output is not None:
                    passed = exact_match(output,test.expected_output)
                
            except Exception as e:
                output = None 
                error = str(e)
                passed = False
                
            execution_time = time.perf_counter() - start_time 
            
            result = ExecutionResult(
                test_id = test.id,
                input = test.input,
                actual_output = output,
                expected_output = test.expected_output,
                passedd = passed,
                error = error,
                execution_time = execution_time,
            )
            
            results.append(result)
            
        return results