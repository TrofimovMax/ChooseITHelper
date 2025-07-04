# models/user.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))

    team = relationship("Team", back_populates="users", foreign_keys=[team_id])
    results = relationship("Result", back_populates="user")
