from sqlalchemy import Column, Integer, String
from models.base import Base

class Technology(Base):
    __tablename__ = "technologies"

    technology_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String, index=True)
    smart_weight = Column(Integer, nullable=True)
    expert_score = Column(Integer, nullable=True)
    ahp_weight = Column(Integer, nullable=True)
