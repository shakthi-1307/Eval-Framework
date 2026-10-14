
import json
import unittest

from evalforge.models import TestCase
from evalforge.graders.llm_grader import llm_grade


class TestLLMGrader(unittest.TestCase):

    def setUp(self):
        self.case = TestCase(
            test_id="TC001",
            input="Say hello politely.",
            expected_output="A polite greeting",
            grading_criteria="The response must be polite.",
        )

    def valid_judge(self, prompt):
        return json.dumps({
            "score": 0.95,
            "passed": True,
            "reason": "The response is polite.",
        })

    def test_valid_judge_response(self):
        result = llm_grade(
            self.case,
            "Hello! How are you?",
            self.valid_judge,
        )

        self.assertEqual(result.score, 0.95)
        self.assertTrue(result.passed)

    def test_invalid_json(self):
        def broken_judge(prompt):
            return "This is not JSON"

        with self.assertRaisesRegex(ValueError, "invalid JSON"):
            llm_grade(self.case, "Hello!", broken_judge)

    def test_score_out_of_range(self):
        def invalid_judge(prompt):
            return json.dumps({
                "score": 1.5,
                "passed": True,
                "reason": "Invalid score.",
            })

        with self.assertRaisesRegex(ValueError, "finite number"):
            llm_grade(self.case, "Hello!", invalid_judge)

    def test_inconsistent_pass_decision(self):
        def inconsistent_judge(prompt):
            return json.dumps({
                "score": 0.2,
                "passed": True,
                "reason": "Inconsistent result.",
            })

        with self.assertRaisesRegex(ValueError, "conflicts"):
            llm_grade(self.case, "Hello!", inconsistent_judge)


if __name__ == "__main__":
    unittest.main()
