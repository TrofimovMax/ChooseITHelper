# controllers/question_controller.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from services.question_service import fetch_question_by_filters
from database import get_db

router = APIRouter()


@router.get("/")
def get_question(filters: str = Query(None), db: Session = Depends(get_db)):
    keys = filters.split(",") if filters else None
    return fetch_question_by_filters(keys, db)
