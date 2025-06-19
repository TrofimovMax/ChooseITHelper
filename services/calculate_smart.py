# services/calculate_smart.py

from services.format_results import format_results
from sqlalchemy.orm import Session


def calculate_smart(frameworks: list[dict], criteria_weights: dict[str, float], db: Session, raw_frameworks: list) -> \
        list[dict]:
    """
    Calculate SMART scores and return in standardized format.
    :param frameworks: list of dicts with criteria_scores.
    :param criteria_weights: dict with weights.
    :param db: SQLAlchemy session for language name lookup.
    :param raw_frameworks: original Framework objects for name/language_id mapping.
    """
    raw_scores = {}

    for framework in frameworks:
        criteria_scores = framework.get("criteria_scores", {})
        smart_score = sum(
            criteria_scores.get(criterion, 0) * weight
            for criterion, weight in criteria_weights.items()
        )
        raw_scores[framework["title"]] = smart_score

    total = sum(raw_scores.values()) or 1e-6

    normalized_scores = {
        k: v / total for k, v in raw_scores.items()
    }

    return format_results(normalized_scores, raw_frameworks, db, method_key="smart_score")
