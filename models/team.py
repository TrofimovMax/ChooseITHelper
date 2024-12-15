# models/team.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.user import User


class Team(Base):
    __tablename__ = "teams"

    team_id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String, index=True)
    lead_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)

    users = relationship("User", back_populates="team", foreign_keys=[User.team_id])
