from sqlalchemy import Column, Integer, String, ForeignKey
from models.base import Base

class Framework(Base):
    __tablename__ = "frameworks"

    framework_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    technology_id = Column(Integer, ForeignKey("technologies.technology_id"))
    smart_weight = Column(Integer, nullable=True)
    expert_score = Column(Integer, nullable=True)
    ahp_weight = Column(Integer, nullable=True)