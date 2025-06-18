# services/calculate_ahp.py

from services.format_results import format_results
from sqlalchemy.orm import Session
from typing import List, Dict
import numpy as np


def calculate_ahp(frameworks: List[Dict], criteria_weights: Dict[str, float], db: Session, raw_frameworks: list) -> \
        List[dict]:
    """
    Calculate AHP scores using pairwise comparisons and return standardized format.
    """
    framework_names = [fw["title"] for fw in frameworks]
    num_frameworks = len(frameworks)
    cumulative_scores = {name: 0.0 for name in framework_names}

    for criterion, weight in criteria_weights.items():
        scores = [fw["criteria_scores"].get(criterion, 0.0) for fw in frameworks]

        comparison_matrix = np.zeros((num_frameworks, num_frameworks))
        for i in range(num_frameworks):
            for j in range(num_frameworks):
                denominator = scores[j] if scores[j] != 0 else 1e-6
                comparison_matrix[i][j] = scores[i] / denominator

        normalized_matrix = comparison_matrix / comparison_matrix.sum(axis=0)
        priority_vector = normalized_matrix.mean(axis=1)

        for i, name in enumerate(framework_names):
            cumulative_scores[name] += weight * priority_vector[i]

    return format_results(cumulative_scores, raw_frameworks, db, method_key="ahp_score")
