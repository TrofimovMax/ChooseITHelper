# services/prepare_criteria_and_alternatives.py

from sqlalchemy.orm import Session

from models import Key


def prepare_criteria_and_alternatives(keys_ids: list[int], db: Session):
    """
    Separate keys into criteria and alternatives based on the is_criterion field.
    """
    criteria_keys = (
        db.query(Key.id)
        .filter(Key.id.in_(keys_ids), Key.is_criterion.is_(True))
        .all()
    )
    alternative_keys = (
        db.query(Key.id)
        .filter(Key.id.in_(keys_ids), Key.is_criterion.is_(False))
        .all()
    )

    criteria = [key.id for key in criteria_keys]
    alternatives = [key.id for key in alternative_keys]

    return criteria, alternatives
