# services/calculate_ahp.py

import numpy as np
import math
from services.format_results import format_results
from sqlalchemy.orm import Session
from typing import List, Dict


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

        if all(score == 0 for score in scores):
            print(f"⚠️ All scores for criterion '{criterion}' are 0. Skipping this criterion.")
            continue

        comparison_matrix = np.zeros((num_frameworks, num_frameworks))
        for i in range(num_frameworks):
            for j in range(num_frameworks):
                denominator = scores[j] if scores[j] != 0 else 1e-6
                comparison_matrix[i][j] = scores[i] / denominator

        col_sum = comparison_matrix.sum(axis=0)

        col_sum[col_sum == 0] = 1e-6
        normalized_matrix = comparison_matrix / col_sum
        priority_vector = normalized_matrix.mean(axis=1)

        for i, name in enumerate(framework_names):
            value = weight * priority_vector[i]
            if math.isnan(value):
                print(f"❌ NaN detected for {name} — setting to 0.0")
                value = 0.0
            cumulative_scores[name] += value

    return format_results(cumulative_scores, raw_frameworks, db, method_key="ahp_score")
