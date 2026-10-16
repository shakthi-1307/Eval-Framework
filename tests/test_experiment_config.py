
import unittest

from evalforge.experiment_config import ExperimentConfig


class TestExperimentConfig(unittest.TestCase):

    def test_create_config(self):
        config = ExperimentConfig(
            experiment_name="prompt_comparison",
            model_name="dummy-model",
            prompt_version="v2",
            grader="llm",
            dataset_name="python_tests",
        )

        self.assertEqual(config.model_name, "dummy-model")
        self.assertEqual(config.prompt_version, "v2")
        self.assertEqual(config.grader_threshold, 0.7)

    def test_metadata_is_independent(self):
        first = ExperimentConfig(
            experiment_name="experiment_1",
            model_name="model-a",
            prompt_version="v1",
        )

        second = ExperimentConfig(
            experiment_name="experiment_2",
            model_name="model-b",
            prompt_version="v2",
        )

        first.metadata["temperature"] = 0.2

        self.assertEqual(second.metadata, {})


if __name__ == "__main__":
    unittest.main()
