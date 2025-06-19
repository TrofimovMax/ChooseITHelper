# services/calculate_smart.py

from services.format_results import format_results
from sqlalchemy.orm import Session


def calculate_smart(
        frameworks: list[dict],
        criteria_weights: dict[str, float],
        db: Session,
        raw_frameworks: list,
        reporter=None
) -> list[dict]:
    """
    Calculate SMART scores and return in standardized format.
    :param frameworks: list of dicts with criteria_scores.
    :param criteria_weights: dict with weights.
    :param db: SQLAlchemy session for language name lookup.
    :param raw_frameworks: original Framework objects for name/language_id mapping.
    """
    raw_scores = {}
    table = []

    table.append(r"\textbf{Formula:} $S_j = \sum_{i=1}^{n} w_i \cdot v_{ij}$")
    table.append(r"\par\vspace{1em}")

    table.append(r"\textbf{Criteria Weights:}")
    table.append(r"\begin{longtable}{l r} \toprule Criterion & Weight \\ \midrule")

    for criterion, weight in criteria_weights.items():
        escaped_criterion = criterion.replace('_', r'\_')
        table.append(f"{escaped_criterion} & {weight:.2f} \\\\")

    table.append(r"\bottomrule \end{longtable}")
    table.append(r"\par\vspace{1em}")

    detailed_rows = []
    for framework in frameworks:
        title = framework["title"]
        criteria_scores = framework.get("criteria_scores", {})
        score_components = []
        smart_score = 0.0

        for criterion, weight in criteria_weights.items():
            value = criteria_scores.get(criterion, 0.0)
            component = weight * value
            smart_score += component
            score_components.append(f"{weight:.2f} \\cdot {value:.2f} = {component:.4f}")

        raw_scores[title] = smart_score
        detailed_rows.append(
            r"\textbf{%s}: $%s$\\[0.5em]" % (title, " + ".join(score_components))
        )

    table.extend(detailed_rows)
    table.append(r"\vspace{1em}")
    table.append(r"\begin{longtable}{l r} \toprule Framework & Normalized SMART Score \\ \midrule")

    total = sum(raw_scores.values()) or 1e-6
    normalized_scores = {}
    for title, score in raw_scores.items():
        normalized = score / total
        normalized_scores[title] = normalized
        table.append(f"{title} & {normalized:.5f} \\\\")

    table.append(r"\bottomrule \end{longtable}")

    if reporter:
        reporter.add_section("SMART Calculation", "\n".join(table))

    return format_results(normalized_scores, raw_frameworks, db, method_key="smart_score")
