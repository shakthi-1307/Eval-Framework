from evalforge.metrics.contains_answer import contains_answer

def test_answer_inside_sentence():
    assert contains_answer(
        "The capital of France is **Paris**.",
        "Paris"
    )
    
def test_number_inside_response():
    assert contains_answer("10 x 5 = **50**.","50")
        
def test_wrong_answer():
    assert not contains_answer(
        "The capital of France is London.",
        "Paris"
    )
    
def test_does_not_match_partial_number():
    assert not contains_answer("The answer is 150.","50")