# services/calculate_criteria_weights.py

from sqlalchemy.orm import Session
from models.framework_key import FrameworkKey
from models.key import Key
from typing import List, Dict
from collections import Counter


def calculate_criteria_weights(criteria_keys: List[Key], top_frameworks: list, db: Session) -> Dict[str, float]:
    """
    Calculate adaptive weights for each criterion key based on how frequently
    it is associated with the selected top frameworks.

    Args:
        criteria_keys (List[Key]): List of Key objects that are criteria (is_criterion=True).
        top_frameworks (list): List of framework ORM objects (selected by user).
        db (Session): Active database session.

    Returns:
        Dict[str, float]: Dictionary mapping criterion key titles to their normalized weight.
    """

    # Collect key_id occurrences for top frameworks
    framework_ids = [f.id for f in top_frameworks]

    # Query FrameworkKey table to get all key_ids linked to the selected top frameworks
    records = db.query(FrameworkKey.key_id).filter(FrameworkKey.framework_id.in_(framework_ids)).all()
    all_key_ids = [r.key_id for r in records]

    # Count how many times each criterion key_id appears
    key_usage_counter = Counter(all_key_ids)

    # Build raw weight map: key title -> count
    raw_weights = {}
    for key in criteria_keys:
        raw_weights[key.title] = key_usage_counter.get(key.id, 0)

    total = sum(raw_weights.values())

    # Avoid division by zero: fallback to uniform weights
    if total == 0:
        fallback_weight = 1 / len(criteria_keys)
        return {key.title: fallback_weight for key in criteria_keys}

    # Normalize the weights
    return {title: count / total for title, count in raw_weights.items()}
