import time 
from evalforge.models.schemas import ExecutionResult
from evalforge.core.dataset import EvaluationDataset
from evalforge.metrics.exact_match import exact_match
from evalforge.metrics.contains_answer import contains_answer

class EvaluationRunner:
    def __init__(self,dataset:EvaluationDataset):
        self.dataset = dataset
        
    def run(self,ai_application,evaluator = None):
        results = []
        
        if evaluator is None:
            evaluator = lambda test, output: contains_answer(
                output, test.expected_output
            )
        
        for test in self.dataset.test_cases:
            start_time = time.perf_counter()
            
            try:
                output = ai_application(test.input)
                error = None 
                if test.expected_output is not None:
                    passed = evaluator(test,output)
                else:
                    passed = None
                
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
                passed = passed,
                error = error,
                execution_time = execution_time,
            )
            
            results.append(result)
            
        return results