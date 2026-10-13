
import math


def wilson_interval(
    passed: int,
    total: int,
    confidence_z: float = 1.96,
) -> tuple[float, float]:
    """Return the Wilson confidence interval for a pass rate."""

    if total <= 0:
        raise ValueError("total must be greater than zero.")

    if not 0 <= passed <= total:
        raise ValueError("passed must be between 0 and total.")

    p = passed / total
    z = confidence_z
    denominator = 1 + z**2 / total

    center = (p + z**2 / (2 * total)) / denominator

    margin = (
        z
        * math.sqrt(
            p * (1 - p) / total
            + z**2 / (4 * total**2)
        )
        / denominator
    )

    return max(0.0, center - margin), min(1.0, center + margin)

    