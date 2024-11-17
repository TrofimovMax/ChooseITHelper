# controllers/user_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.user_service import fetch_users
from database import get_db

router = APIRouter()

@router.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return fetch_users(db)
