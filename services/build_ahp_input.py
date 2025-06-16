# services/helpers/build_ahp_input.py

from typing import List
from sqlalchemy.orm import Session
from models import Framework, FrameworkKey, Key, Language


def build_ahp_input(frameworks: List[Framework], criteria: List[Key], db: Session) -> List[dict]:
    """
    Prepare input for AHP calculation.
    Each framework should include a summed ahp_score across all selected criteria.
    """
    input_data = []
    for framework in frameworks:
        language_name = db.query(Language.name).filter(Language.language_id == framework.language_id).scalar()

        criteria_scores = {}
        for key in criteria:
            score = (
                db.query(FrameworkKey.ahp_score)
                .filter(FrameworkKey.framework_id == framework.framework_id,
                        FrameworkKey.key_id == key.id)
                .scalar()
            )
            criteria_scores[key.key] = score or 0.0

        input_data.append({
            "name": framework.name,
            "language_name": language_name,
            "criteria_scores": criteria_scores
        })

    return input_data
