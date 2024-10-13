# models/user.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String, index=True)
    team_id = Column(Integer, ForeignKey("teams.team_id"))

    # Явное указание внешнего ключа для связи с Team
    team = relationship("Team", back_populates="users", foreign_keys=[team_id])
