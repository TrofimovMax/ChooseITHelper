# models/framework.py

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.base import Base


class Framework(Base):
    __tablename__ = "frameworks"

    framework_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    language_id = Column(Integer, ForeignKey("languages.language_id"))

    feasibility = Column(Float, nullable=True)
    novelty = Column(Float, nullable=True)
    usefulness = Column(Float, nullable=True)

    keys = relationship("FrameworkKey", back_populates="framework")
