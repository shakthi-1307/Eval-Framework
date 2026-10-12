from evalforge.runner import run_test
from evalforge.dataset import load_dataset  
cases = load_dataset("data/test_cases.jsonl")  

def dummy_app(question):
    if question == "What is 2 + 2?":
        return "4"
    return "I don't know."


from evalforge.graders.code_grader import exact_match

result = exact_match("TC001", "4", "4")
print(result)

result = exact_match("TC001", "4", "5")
print(result)