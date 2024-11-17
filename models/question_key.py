# models/question_key.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class QuestionKey(Base):
    __tablename__ = "question_keys"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.question_id"))
    key = Column(String, nullable=False)

    question = relationship("Question", back_populates="keys")
