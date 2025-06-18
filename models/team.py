# models/team.py

from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from models.base import Base
from models.user import User


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    lead_id = Column(
        Integer,
        ForeignKey("users.id", name="fk_team_lead"),
        nullable=True
    )

    users = relationship("User", back_populates="team", foreign_keys=[User.team_id])
