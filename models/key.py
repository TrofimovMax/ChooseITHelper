# models/key.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base


class Key(Base):
    __tablename__ = "keys"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, nullable=False)

    frameworks = relationship("FrameworkKey", back_populates="key")