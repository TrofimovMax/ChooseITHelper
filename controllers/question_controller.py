# controllers/question_controller.py

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from services.fetch_question_by_id import fetch_question_by_id
from services.question_service import fetch_question_by_filters
from database import get_db

router = APIRouter()


@router.get("/")
def get_question(
        filters: str = Query(None),
        next_question_id: int = Query(None),
        db: Session = Depends(get_db)
):
    """
    Fetch a question based on the provided filters or next_question_id.
    If next_question_id is provided, it takes precedence over filters.
    """
    if next_question_id is not None:
        question = fetch_question_by_id(next_question_id, db)
        if question:
            return question

    if not filters:
        raise HTTPException(
            status_code=400, detail="Either filters or next_question_id must be provided"
        )

    keys = filters.split(",")
    question, missing_keys = fetch_question_by_filters(keys, db)

    if missing_keys is None:
        return {
            "message": "No questions found",
            "all_keys": keys,
        }

    if not question:
        raise HTTPException(status_code=404, detail=f"No questions found for filters: {filters}")

    return question
