# models/developer.py

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base import Base


class Developer(Base):
    __tablename__ = "developers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    technology_id = Column(Integer, ForeignKey("languages.id"))
    framework_id = Column(Integer, ForeignKey("frameworks.id"), nullable=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
