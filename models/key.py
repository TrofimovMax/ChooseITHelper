# models/key.py

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from models.base import Base


class Key(Base):
    __tablename__ = "keys"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    is_criterion = Column(Boolean, nullable=False, default=False)

    frameworks = relationship("FrameworkKey", back_populates="key")
    question_keys = relationship("QuestionKey", back_populates="key")

    def __repr__(self):
        return f"<Key id={self.id} title={self.title} is_criterion={self.is_criterion}>"
