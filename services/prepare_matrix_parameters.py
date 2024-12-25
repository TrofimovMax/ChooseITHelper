# services/prepare_matrix_parameters.py

from sqlalchemy import func
from sqlalchemy.orm import Session

from models import FrameworkKey


def prepare_matrix_parameters(frameworks: list[int], alternatives: list[int], criteria: list[int], db: Session):
    """
    Prepare parameters for SMART calculation.
    """
    matrix = []
    for framework_id in frameworks:
        matrix_alt_score = db.query(func.sum(FrameworkKey.weight)).filter(
            FrameworkKey.framework_id == framework_id,
            FrameworkKey.key_id.in_(alternatives),
        ).scalar()
        matrix_crit_score = db.query(func.sum(FrameworkKey.weight)).filter(
            FrameworkKey.framework_id == framework_id,
            FrameworkKey.key_id.in_(criteria),
        ).scalar()
        matrix.append({
            "framework_id": framework_id,
            "alt_score": matrix_alt_score or 0.0,
            "crit_score": matrix_crit_score or 0.0,
        })

        matrix_crit_score

    return matrix
