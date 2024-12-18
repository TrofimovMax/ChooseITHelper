# services/question_service.py

from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from models.question import Question
from models.question_key import QuestionKey
from models.key import Key


def fetch_question_by_filters(keys: list[str], db: Session):
    if not keys:
        return {"message": "Filters are required"}, 400

    existing_keys = db.query(Key.key).filter(Key.key.in_(keys)).all()
    existing_key_names = {k[0] for k in existing_keys}

    missing_keys = set(keys) - existing_key_names
    if missing_keys:
        return {"message": "No questions found", "missing_keys": list(keys)}, 404

    key_ids = [key.id for key in db.query(Key).filter(Key.key.in_(keys)).all()]
    matching_question_id = (
        db.query(QuestionKey.question_id)
        .filter(QuestionKey.key_id.in_(key_ids))
        .group_by(QuestionKey.question_id)
        .having(func.count(QuestionKey.key_id) == len(key_ids))
        .first()
    )

    if not matching_question_id:
        return {"message": f"No questions found for keys: {keys}"}, 404

    question = db.query(Question).filter(Question.question_id == matching_question_id[0]).first()

    return format_question_response(question)


def format_question_response(question: Question):
    return {
        "question_id": question.question_id,
        "text": question.text,
        "options": [
            {
                "option_id": opt.option_id,
                "text": opt.title,
                "key": opt.key,
                "image_url": opt.image_path,
            }
            for opt in (question.options or [])
        ],
    }
