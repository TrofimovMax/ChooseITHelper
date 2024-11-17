# controllers/question_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.question_service import (
    fetch_start_question,
    fetch_next_question,
    complete_survey_logic,
)
from database import get_db

router = APIRouter()

@router.get("/questions/start")
def get_start_question(db: Session = Depends(get_db)):
    return fetch_start_question(db)

@router.post("/questions/next")
def get_next_question(option_id: int, db: Session = Depends(get_db)):
    return fetch_next_question(option_id, db)

@router.post("/questions/complete")
def complete_survey(answers: list[int], db: Session = Depends(get_db)):
    return complete_survey_logic(answers, db)
