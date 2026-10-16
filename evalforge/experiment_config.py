from dataclasses import dataclass, field 

@dataclass 
class ExperimentConfig:
    experiment_name: str
    model_name: str 
    prompt_version: str 
    grader: str = "code"
    grader_threshold: float = 0.7
    dataset_name: str = "unknown"
    metadata: dict = field(default_factory = dict)
    