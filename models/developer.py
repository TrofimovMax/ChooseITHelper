# models/developer.py

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base import Base


class Developer(Base):
    __tablename__ = "developers"

    developer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    technology_id = Column(Integer, ForeignKey("languages.language_id"))
    framework_id = Column(Integer, ForeignKey("frameworks.framework_id"), nullable=True)
    team_id = Column(Integer, ForeignKey("teams.team_id"))
    smart_weight = Column(Integer, nullable=True)
    expert_score = Column(Integer, nullable=True)
    ahp_weight = Column(Integer, nullable=True)
