# models/framework.py

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.base import Base


class Framework(Base):
    __tablename__ = "frameworks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    language_id = Column(Integer, ForeignKey("languages.id"))

    feasibility = Column(Float, nullable=True)
    novelty = Column(Float, nullable=True)
    usefulness = Column(Float, nullable=True)

    keys = relationship("FrameworkKey", back_populates="framework")

    def __repr__(self):
        return f"<Framework id={self.id} title={self.title} language_id={self.language_id}, " \
                f"feasibility={self.feasibility} novelty={self.novelty} usefulness={self.usefulness}> "
