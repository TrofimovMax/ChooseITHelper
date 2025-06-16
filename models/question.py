# models/question.py

from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from models.base import Base


class Question(Base):
    __tablename__ = "questions"

    question_id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)

    options = relationship("Option", back_populates="question", foreign_keys="[Option.question_id]")
    keys = relationship("QuestionKey", back_populates="question")

    def __repr__(self):
        return f"<Question id={self.id} question_id={self.question_id} text={self.text}>"
