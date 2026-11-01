import json 
from pathlib import Path 
from evalforge.reporting.report import EvaluationReport 

def export_report(
    report: EvaluationReport,
    output_dir: str = "reports",
) -> None:
    directory = Path(output_dir)
    directory.mkdir(parents=True,exist_ok = True)
    
    timestamp = report.generated_at.strftime("%Y%m%d_%H%M%S")
    filename = f"eval_{timestamp}_{report.run_id[:8]}.json"
    path = directory/filename
    
    with path.open("w",encoding = "utf-8") as file:
        json.dump(
            report.model_dump(mode = "json"),
            file,
            indent = 4,
        )
        
    print(f"Report saved to: {path}")