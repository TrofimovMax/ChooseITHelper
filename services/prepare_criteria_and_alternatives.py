# services/prepare_criteria_and_alternatives.py

from sqlalchemy.orm import Session

from models import Key


def prepare_criteria_and_alternatives(keys_ids: list[int], db: Session):
    """
    Separate full Key objects into criteria and alternatives based on is_criterion.
    """
    keys = db.query(Key).filter(Key.id.in_(keys_ids)).all()

    criteria = [key for key in keys if key.is_criterion]
    alternatives = [key for key in keys if not key.is_criterion]

    return criteria, alternatives
