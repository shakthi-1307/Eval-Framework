from evalforge.models.schemas import TestCase 

class EvaluationDataset:
    def __init__(self,name:str):
        self.name = name 
        self.test_cases: list[TestCase] = []
        
    def add_test_case(self,test_case:TestCase):
        for exisiting in self.test_cases:
            if exisiting.id == test_case.id:
                raise ValueError(f"Duplicate test case ID : {test_case.id}")
        
        self.test_cases.append(test_case)
        
    def get_test_case(self,test_id:str):
        for test in self.test_cases:
            if test.id == test_id:
                return test 
        
        return None 
    
    def size(self):
        return len(self.test_cases)