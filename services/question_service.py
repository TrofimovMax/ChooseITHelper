# services/question_service.py

from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from models.question import Question
from models.question_key import QuestionKey
from models.key import Key
from services.format_question_response import format_question_response


def fetch_question_by_filters(keys: list[str], db: Session):
    """
    Fetch a question matching all provided keys exactly.
    If keys are missing from the database, return the missing keys.
    """
    # Check if the provided keys exist in the database
    existing_keys = db.query(Key.key).filter(Key.key.in_(keys)).all()
    existing_key_names = {k[0] for k in existing_keys}

    missing_keys = set(keys) - existing_key_names
    if missing_keys:
        return None, missing_keys  # Return missing keys if any

    # Retrieve IDs of the keys in the same order as `keys`
    key_id_map = {key.key: key.id for key in db.query(Key).filter(Key.key.in_(keys)).all()}
    key_ids = [key_id_map[key] for key in keys if key in key_id_map]

    subquery = (
        db.query(QuestionKey.question_id)
        .filter(QuestionKey.key_id.in_(key_ids))
        .group_by(QuestionKey.question_id)
        .having(func.count(QuestionKey.key_id) == len(key_ids))
        .having(func.count(QuestionKey.key_id) == db.query(func.count(QuestionKey.key_id))
                .filter(QuestionKey.question_id == QuestionKey.question_id)
                .correlate(QuestionKey))
        .order_by(QuestionKey.question_id.asc())
        .limit(1)
    ).subquery()

    question = db.query(Question).filter(Question.question_id.in_(subquery)).first()

    if not question:
        return None, None

    return format_question_response(question), None
