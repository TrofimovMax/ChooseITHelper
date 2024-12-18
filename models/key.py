# models/key.py

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from models.base import Base


class Key(Base):
    __tablename__ = "keys"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, nullable=False)
    is_criterion = Column(Boolean, nullable=False, default=False)

    frameworks = relationship("FrameworkKey", back_populates="key")
    question_keys = relationship("QuestionKey", back_populates="key")
