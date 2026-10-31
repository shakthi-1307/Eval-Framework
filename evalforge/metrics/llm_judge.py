import json 
import re 

def llm_judge(
    judge_model,
    question: str,
    expected: str,
    actual: str,
) -> bool:
    prompt = f"""
You are an impartial evaluator.
Determine whether the actual answer is factually equivalent to the 
expected answer for the question.
Question: {question}
Expected answer : {expected}
Actual answer: {actual}

Ignore differences in wording and formatting.
Mark FAIL if the answer is incorrect, contradictory or irrelevant.

Return only valid JSON: 
{{"verdict": "PASS" or "FAIL"}}
"""
    response = judge_model.generate(prompt)
    
    match = re.search(r"\{.*?\}", response, re.DOTALL)
    if not match:
        raise ValueError(f"Invalid judge response: {response}")
    
    data = json.loads(match.group())
    
    verdict = data.get("verdict", "").upper()
    
    if verdict not in {"PASS","FAIL"}:
        raise ValueError(f"Unexpected verdict : {verdict}")
    
    return verdict == "PASS"
    