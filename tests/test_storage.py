
import json
import tempfile
import unittest

from pathlib import Path

from evalforge.experiment_config import ExperimentConfig
from evalforge.metrics import EvaluationMetrics
from evalforge.storage import save_results


class TestStorage(unittest.TestCase):

    def test_saves_config_and_metrics(self):
        config = ExperimentConfig(
            experiment_name="prompt_comparison",
            model_name="dummy-model",
            prompt_version="v2",
            grader="code",
            dataset_name="python_tests",
        )

        metrics = EvaluationMetrics(
            total_tests=1,
            passed_tests=1,
            failed_tests=0,
            pass_rate=1.0,
            ci_lower=0.2065,
            ci_upper=1.0,
            average_latency_seconds=0.001,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            path = save_results(
                results=[],
                metrics=metrics,
                config=config,
                output_dir=temp_dir,
            )

            with Path(path).open(encoding="utf-8") as file:
                report = json.load(file)

        self.assertEqual(
            report["experiment_config"]["model_name"],
            "dummy-model",
        )
        self.assertEqual(
            report["experiment_config"]["prompt_version"],
            "v2",
        )
        self.assertEqual(report["metrics"]["pass_rate"], 1.0)
        self.assertIn("run_id", report)


if __name__ == "__main__":
    unittest.main()
