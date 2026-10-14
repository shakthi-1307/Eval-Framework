
import unittest

from evalforge.models import TestCase
from evalforge.runner import run_test


class TestRunner(unittest.TestCase):

    def setUp(self):
        self.case = TestCase(
            test_id="TC001",
            input="What is 2 + 2?",
            expected_output="4",
        )

    def test_successful_execution(self):
        result = run_test(self.case, lambda question: "4")

        self.assertEqual(result.actual_output, "4")
        self.assertIsNone(result.error)
        self.assertGreaterEqual(result.latency_seconds, 0)

    def test_application_error(self):
        def broken_app(question):
            raise RuntimeError("Simulated failure")

        result = run_test(self.case, broken_app)

        self.assertIsNone(result.actual_output)
        self.assertIn("Simulated failure", result.error)


if __name__ == "__main__":
    unittest.main()
