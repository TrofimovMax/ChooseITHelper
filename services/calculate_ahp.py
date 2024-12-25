# services/calculate_ahp.py

from typing import List, Dict
import numpy as np


def calculate_ahp(frameworks: List[Dict[str, any]]) -> Dict[str, float]:
    """
    Calculate AHP scores for a list of frameworks based on their criteria scores.

    :param frameworks: List of frameworks with criteria scores in the form:
                       [
                           {
                               "name": "Framework 1",
                               "language_name": "Python",
                               "ahp_score": 10.5
                           },
                           ...
                       ]
    :return: Dictionary with framework names as keys and their final AHP scores as values.
    """
    # Extract AHP scores into a matrix
    scores = [framework['ahp_score'] for framework in frameworks]
    num_frameworks = len(scores)

    # Create pairwise comparison matrix
    pairwise_matrix = np.zeros((num_frameworks, num_frameworks))
    for i in range(num_frameworks):
        for j in range(num_frameworks):
            pairwise_matrix[i][j] = scores[i] / scores[j] if scores[j] != 0 else 0

    # Normalize the pairwise matrix
    column_sums = pairwise_matrix.sum(axis=0)
    normalized_matrix = pairwise_matrix / column_sums

    # Calculate priority vector (average of rows)
    priority_vector = normalized_matrix.mean(axis=1)

    # Map priority vector back to framework names
    ahp_results = {
        frameworks[i]['name']: priority_vector[i] for i in range(num_frameworks)
    }

    return ahp_results
