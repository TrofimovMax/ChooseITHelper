# services/fetch_question_by_id.py

from sqlalchemy.orm import Session
from models.question import Question
from sqlalchemy.exc import NoResultFound

from services.format_question_response import format_question_response


def fetch_question_by_id(question_id: int, db: Session):
    """
    Fetch a question from the database based on its ID.

    :param question_id: The ID of the question to fetch.
    :param db: SQLAlchemy Session instance.
    :return: The question object or None if not found.
    """
    try:
        question = db.query(Question).filter(Question.id == question_id).one_or_none()
        return format_question_response(question)
    except NoResultFound:
        return None
