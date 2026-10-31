from evalforge.models.llm import GroqLLM
from evalforge.models.schemas import TestCase 
from evalforge.core.dataset import EvaluationDataset 
from evalforge.core.runner import EvaluationRunner
from evalforge.reporting.report import generate_report 
from evalforge.metrics.llm_judge import llm_judge

llm = GroqLLM()

dataset = EvaluationDataset("General Knowledge")

dataset.add_test_case(
    TestCase(
        id="TC001",
        input = "What is the captial of France?",
        expected_output = "Paris"
    )
)

dataset.add_test_case(
    TestCase(
        id="TC002",
        input = "What is 10 multiplied by 5?",
        expected_output = "50"
    )
)

dataset.add_test_case(
    TestCase(
        id="TC003",
        input = "What is the capital of Japan?",
        expected_output = "Tokyo"
    )
)

runner = EvaluationRunner(dataset)

results = runner.run(
    ai_application = llm.generate,
    evaluator = lambda test, output: llm_judge(
        judge_model = llm,
        question = test.input,
        expected = test.expected_output,
        actual = output,
    ),
)

report = generate_report(
    dataset.name,
    results
)

for result in results:
    print(f"\nTest: {result.test_id}")
    print(f"\nExpected: {result.expected_output}")
    print(f"\nActual: {result.actual_output}")
    print(f"\nPassed: {result.passed}")
    
print("\n============== EVALUATION REPORT ==================")

print(report.model_dump_json(indent = 4))

print("\n============== LLM JUDGE ==================")

actual = llm.generate("What is the capital of France?")

passed = llm_judge(
    judge_model=llm,
    question="What is the capital of France?",
    expected="Paris",
    actual=actual,
)

print("Judge verdict:", passed)