# services/calculate_adaptive_weighted_method.py

from typing import List, Dict
from sqlalchemy.orm import Session
from services.adaptive_metrics import calculate_adaptive_coefficient
from services.format_results import format_results


def calculate_adaptive_weighted_method(
    frameworks: List[Dict],
    criteria_weights: Dict[str, float],
    raw_frameworks: list,
    db: Session,
    reporter=None
) -> List[Dict]:
    """
    Adaptive Weighted Method (AWM) evaluation using detailed adaptive coefficient calculation.
    Logs step-by-step calculations.
    """
    results = []

    if reporter:
        reporter.add_section("AWM Formula",
                             r"$S_j = \sum_{i=1}^{n} w_i \cdot v_{ij} \cdot p_{ij}$, where $p_{ij}$ is the adaptive coefficient.")

    for fw in frameworks:
        framework_id = fw["id"]
        framework_title = fw["title"]
        language_name = fw["language_name"]

        lines = []
        lines.append(rf"\textbf{{Framework:}} {framework_title} ({language_name})")

        # Adaptive coefficient
        p_ij = calculate_adaptive_coefficient(db, framework_id)
        lines.append(rf"$p_{{ij}}$ (adaptive coefficient): {p_ij:.5f}")

        lines.append(r"\begin{longtable}{l r r r} ")
        lines.append(r"\toprule")
        lines.append(r"Criterion & Weight ($w_i$) & Value ($v_{ij}$) & $w_i \cdot v_{ij} \cdot p_{ij}$ \\ \midrule")

        score = 0.0
        for criterion, weight in criteria_weights.items():
            v_ij = fw["criteria_scores"].get(criterion, 0.0)
            weighted = weight * v_ij * p_ij
            score += weighted
            escaped_criterion = criterion.replace('_', r'\_')
            lines.append(f"{escaped_criterion} & {weight:.2f} & {v_ij:.2f} & {weighted:.5f} \\\\")

        lines.append(r"\bottomrule \end{longtable}")
        lines.append(rf"\textbf{{Final AWM Score}}: {score:.5f} \\\\")

        reporter.add_section(f"AWM Score for {framework_title}", "\n".join(lines))

        results.append({
            "framework_title": framework_title,
            "language_name": language_name,
            "awm_score": score
        })

    if reporter:
        summary_lines = [r"\begin{longtable}{l r} \toprule Framework & AWM Score \\ \midrule"]
        for r in results:
            summary_lines.append(f"{r['framework_title']} & {r['awm_score']:.5f} \\\\")
        summary_lines.append(r"\bottomrule \end{longtable}")
        reporter.add_section("Final AWM Scores", "\n".join(summary_lines))

    return format_results(
        {r["framework_title"]: r["awm_score"] for r in results},
        raw_frameworks,
        db,
        method_key="awm_score"
    )
