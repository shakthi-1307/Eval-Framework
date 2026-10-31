import json 
from pathlib import Path 
from evalforge.reporting.report import EvaluationReport 

def export_report(
    report: EvaluationReport,
    output_path: str = "reports/evaluation_report.json",
) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents = True, exist_ok = True)
    
    with path.open("w",encoding = "utf-8") as file:
        json.dump(
            report.model_dump(mode = "json"),
            file,
            indent = 4,
        )
        
    print(f"Report saved to: {path}")