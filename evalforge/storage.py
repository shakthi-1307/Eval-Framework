
import json
from dataclasses import asdict
from pathlib import Path
from datetime import datetime, timezone


def save_results(results, metrics, output_dir="results"):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    report = {
        "run_id": datetime.now(timezone.utc).strftime(
            "%Y%m%dT%H%M%S%fZ"
        ),
        "metrics": asdict(metrics),
        "results": [
            {
                "execution": asdict(execution),
                "grading": asdict(grading),
            }
            for execution, grading in results
        ],
    }

    file_path = output_path / f"{report['run_id']}.json"

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    return file_path
