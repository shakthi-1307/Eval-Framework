from evalforge.models.schemas import TestCase 
from evalforge.core.dataset import EvaluationDataset 
from evalforge.core.runner import EvaluationRunner 

def mock_ai_app(question):
    if question == "2+3":
        return "5"
    
    if question == "4+5":
        return "9"
    
    raise ValueError("Unknown question")

    
def test_runner_execution():
    dataset = EvaluationDataset("Math Tests")
    dataset.add_test_case(TestCase(id="TC002",input="4+5"))
    dataset.add_test_case(TestCase(id="TC001",input="2+3"))
    runner = EvaluationRunner(dataset)
    results = runner.run(mock_ai_app)
    
    assert len(results) == 2
    assert results[0].actual_output == "9"
    assert results[1].actual_output == "5"
    

def test_runner_handles_errors():
    dataset = EvaluationDataset("Error Tests")
    dataset.add_test_case(TestCase(id="TC003",input = "unknown"))
    runner = EvaluationRunner(dataset)
    results = runner.run(mock_ai_app)
    assert results[0].actual_output is None 
    assert results[0].error == "Unknown question"
    
    