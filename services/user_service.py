# services/user_service.py

from sqlalchemy.orm import Session
from models.user import User

def fetch_users(db: Session):
    users = db.query(User).all()
    return users
