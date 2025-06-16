# models/question_key.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class QuestionKey(Base):
    __tablename__ = "question_keys"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.question_id"), nullable=False)
    key_id = Column(Integer, ForeignKey("keys.id"), nullable=False)

    question = relationship("Question", back_populates="keys")
    key = relationship("Key", back_populates="question_keys")

    def __repr__(self):
        return f"<QuestionKey id={self.id} question_id={self.question_id} key_id={self.key_id}>"
