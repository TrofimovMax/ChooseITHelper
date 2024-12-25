# services/calculate_smart.py

def calculate_smart(frameworks: list[dict], criteria_weights: dict[str, float]) -> list[dict]:
    """
    Calculate SMART scores for a list of frameworks based on criteria weights.

    :param frameworks: List of frameworks with the following structure:
        [
            {
                "name": "Framework1",
                "language_name": "Python",
                "criteria_scores": {
                    "criterion1": 0.8,
                    "criterion2": 0.7,
                    ...
                }
            },
            ...
        ]
    :param criteria_weights: Dictionary of weights for each criterion:
        {
            "criterion1": 0.4,
            "criterion2": 0.6,
            ...
        }
    :return: List of frameworks with calculated SMART scores, sorted in descending order:
        [
            {
                "name": "Framework1",
                "language_name": "Python",
                "smart_score": 0.78
            },
            ...
        ]
    """
    results = []

    for framework in frameworks:
        criteria_scores = framework.get("criteria_scores", {})

        # Calculate the weighted sum for the framework
        smart_score = sum(
            criteria_scores.get(criterion, 0) * weight
            for criterion, weight in criteria_weights.items()
        )

        results.append({
            "name": framework["name"],
            "language_name": framework["language_name"],
            "smart_score": smart_score
        })

    # Sort frameworks by SMART score in descending order
    results.sort(key=lambda x: x["smart_score"], reverse=True)

    return results
