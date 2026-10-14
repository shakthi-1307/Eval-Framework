
import unittest

from evalforge.graders.code_grader import exact_match


class TestCodeGrader(unittest.TestCase):

    def test_exact_match_passes(self):
        result = exact_match("TC001", "4", "4")

        self.assertEqual(result.score, 1.0)
        self.assertTrue(result.passed)

    def test_mismatch_fails(self):
        result = exact_match("TC002", "4", "5")

        self.assertEqual(result.score, 0.0)
        self.assertFalse(result.passed)

    def test_whitespace_is_ignored(self):
        result = exact_match("TC003", " Paris ", "Paris")

        self.assertTrue(result.passed)

    def test_missing_output_fails(self):
        result = exact_match("TC004", "4", None)

        self.assertEqual(result.score, 0.0)
        self.assertFalse(result.passed)


if __name__ == "__main__":
    unittest.main()
