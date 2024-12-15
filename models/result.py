# models/result.py

from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from models.base import Base


class Result(Base):
    __tablename__ = "results"

    result_id = Column(Integer, primary_key=True, index=True)
    query_keys = Column(JSONB, nullable=False)
    smart_results = Column(JSONB, nullable=True)  # results SMART
    ahp_results = Column(JSONB, nullable=True)  # results AHP
    adaptive_weighted_results = Column(JSONB, nullable=True)  # results Adaptive Weighted Method

    user = relationship("User", back_populates="results")
