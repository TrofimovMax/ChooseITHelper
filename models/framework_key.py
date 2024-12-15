# models/framework_key.py

from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.base import Base


class FrameworkKey(Base):
    __tablename__ = "frameworks_keys"

    framework_id = Column(Integer, ForeignKey("frameworks.framework_id"), primary_key=True)
    key_id = Column(Integer, ForeignKey("keys.id"), primary_key=True)

    smart_score = Column(Float, nullable=True)
    ahp_score = Column(Float, nullable=True)

    framework = relationship("Framework", back_populates="keys")
    key = relationship("Key", back_populates="frameworks")
