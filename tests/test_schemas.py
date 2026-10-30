import pytest 
from pydantic import ValidationError 
from evalforge.models.schemas import TestCase 

def test_valid_test_case():
    test = TestCase(
        id="TC001",
        input = "What is 2 + 3?",
        expected_output = "5"
    )
    
    assert test.id == "TC001", "ID must be of string type"
    
def test_empty_id():
    with pytest.raises(ValidationError):
        TestCase(id="",input = "Hello")
        
def test_empty_input():
    with pytest.raises(ValidationError):
        TestCase(id='TC002',input = "")
        
def test_default_metadata():
    test = TestCase(id = "TC003",input = "Hello")
    assert test.metadata == {}
    
def test_default_metadata_is_independent():
    test1 = TestCase(id = "TC004",input = "Hello")
    test2 = TestCase(id = "TC005",input = "Hi")
    test1.metadata["category"] = "greeting"
    assert test2.metadata == {}
    
def test_expected_output_is_optional():
    test = TestCase(id="TC006",input = "Hello")
    assert test.expected_output is None 