# services/question_service.py

from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from models.question import Question
from models.question_key import QuestionKey


def fetch_question_by_filters(keys: list[str], db: Session):
    if not keys:
        return {"message": "Filters are required"}, 400

    if "first_question" in keys:
        start_key = db.query(QuestionKey).filter(QuestionKey.key == "first_question").first()
        if not start_key:
            return {"message": "No start question key found"}, 404

        question = db.query(Question).filter(Question.question_id == start_key.question_id).first()
        if not question:
            return {"message": "No start question found"}, 404

        return format_question_response(question)

    subquery = (
        db.query(QuestionKey.question_id)
        .filter(QuestionKey.key.in_(keys))
        .group_by(QuestionKey.question_id)
        .having(func.count(QuestionKey.key) == len(keys))
        .subquery()
    )

    question = db.query(Question).filter(Question.question_id.in_(subquery)).first()

    if not question:
        return {"message": "No matching question found"}, 404

    return format_question_response(question)


def format_question_response(question: Question):
    return {
        "question_id": question.question_id,
        "text": question.text,
        "options": [
            {"option_id": opt.option_id, "text": opt.title, "image_url": opt.image_path}
            for opt in (question.options or [])
        ],
    }
