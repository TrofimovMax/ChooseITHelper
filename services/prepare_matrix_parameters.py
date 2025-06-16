# services/prepare_matrix_parameters.py

from sqlalchemy import func
from sqlalchemy.orm import Session
from models import FrameworkKey


def prepare_matrix_parameters(framework_ids: list[int], alternatives: list[int], criteria: list[int], db: Session):
    """
    Prepare parameters for SMART calculation using smart_score.
    """
    matrix = []
    for framework_id in framework_ids:
        alt_score = db.query(func.sum(FrameworkKey.smart_score)).filter(
            FrameworkKey.framework_id == framework_id,
            FrameworkKey.key_id.in_(alternatives),
        ).scalar() or 0.0

        crit_score = db.query(func.sum(FrameworkKey.smart_score)).filter(
            FrameworkKey.framework_id == framework_id,
            FrameworkKey.key_id.in_(criteria),
        ).scalar() or 0.0

        matrix.append({
            "framework_id": framework_id,
            "alt_score": alt_score,
            "crit_score": crit_score,
        })

    return matrix
