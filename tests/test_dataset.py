import pytest 
from evalforge.models.schemas import TestCase 
from evalforge.core.dataset import EvaluationDataset 

def test_add_test_case():
    dataset = EvaluationDataset("Math Tests")
    
    test = TestCase(
        id = "TC001",
        input = "2+3",
        expected_output = "5",
    )
    
    dataset.add_test_case(test)
    
    assert dataset.size() == 1 
    
def test_duplicate_test_case():
    dataset = EvaluationDataset("Math Tests")
    dummy = TestCase(
        id = "TC001",
        input = "2+1",
    )
    dataset.add_test_case(dummy)
    
    test = TestCase(
        id = "TC001",
        input = "2+1",
    )
    
    with pytest.raises(ValueError):
        dataset.add_test_case(test)
        
def test_get_test_case():
    dataset = EvaluationDataset("Math Tests")
    
    test = TestCase(
        id = "TC001",
        input = "2 + 3",
    )
    
    dataset.add_test_case(test)
    
    result = dataset.get_test_case("TC001")
    
    assert result.id == "TC001"
    
def test_nonexistent_test_case():
    dataset = EvaluationDataset("Math Tests")
    result = dataset.get_test_case("TC999")
    assert result is None 
    
def test_empty_dataset():
    dataset = EvaluationDataset("Math Tests")
    assert dataset.size() == 0