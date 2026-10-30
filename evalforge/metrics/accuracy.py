def calculate_accuracy(results):
    if not results:
        return 0.0 
    correct = 0 
    for result in results:
        if result.passed:
            correct +=1 
    return correct/len(results)