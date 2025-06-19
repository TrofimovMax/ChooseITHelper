# services/calculate_adaptive_weighted_method.py

from typing import List, Dict
from sqlalchemy.orm import Session
from services.adaptive_metrics import calculate_adaptive_coefficient
from services.format_results import format_results


def calculate_adaptive_weighted_method(
    frameworks: List[Dict],
    criteria_weights: Dict[str, float],
    raw_frameworks: list,
    db: Session
) -> List[Dict]:
    """
    Adaptive Weighted Method (AWM) evaluation using detailed adaptive coefficient calculation.
    Logs step-by-step calculations.
    """
    results = []

    for fw in frameworks:
        framework_id = fw["id"]
        framework_title = fw["title"]
        language_name = fw["language_name"]

        print(f"\n┌─────────────────────────────────────────────────────────────────────────────┐")
        print(f"│ Framework: {framework_title:<25} Language: {language_name:<15} │")
        print(f"└─────────────────────────────────────────────────────────────────────────────┘")

        # Calculate adaptive coefficient
        p_ij = calculate_adaptive_coefficient(db, framework_id)
        print(f"→ p_ij (adaptive coefficient): {p_ij:.5f}")

        score = 0.0
        print(f"\n┌─────────────────────────────┬────────────┬──────────┬────────────┐")
        print(f"│ Criterion                   │ Weight (w) │ v_ij     │ w * v * p  │")
        print(f"├─────────────────────────────┼────────────┼──────────┼────────────┤")

        for criterion, weight in criteria_weights.items():
            v_ij = fw["criteria_scores"].get(criterion, 0.0)
            weighted = weight * v_ij * p_ij
            print(f"│ {criterion:<27} │ {weight:<10.2f} │ {v_ij:<8.2f} │ {weighted:<10.5f} │")
            score += weighted

        print(f"└─────────────────────────────┴────────────┴──────────┴────────────┘")
        print(f"✔ Final AWM score for {framework_title}: {score:.5f}")

        results.append({
            "framework_title": framework_title,
            "language_name": language_name,
            "awm_score": score
        })

    return format_results(
        {r["framework_title"]: r["awm_score"] for r in results},
        raw_frameworks,
        db,
        method_key="awm_score"
    )
