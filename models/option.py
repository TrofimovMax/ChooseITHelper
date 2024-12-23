# models/option.py

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from models.base import Base


class Option(Base):
    __tablename__ = "options"

    option_id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    image_path = Column(String, nullable=True)
    key = Column(String, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.question_id"), nullable=False)
    next_question_id = Column(Integer, ForeignKey("questions.question_id"), nullable=True)

    question = relationship("Question", back_populates="options", foreign_keys=[question_id],)
    next_question = relationship("Question", foreign_keys=[next_question_id])
