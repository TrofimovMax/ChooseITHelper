# models/framework_key.py

from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.base import Base


class FrameworkKey(Base):
    __tablename__ = "frameworks_keys"

    id = Column(Integer, primary_key=True, index=True)
    framework_id = Column(Integer, ForeignKey("frameworks.id"), index=True, nullable=False)
    key_id = Column(Integer, ForeignKey("keys.id"), index=True, nullable=False)

    smart_score = Column(Float, nullable=True)
    ahp_score = Column(Float, nullable=True)

    framework = relationship("Framework", back_populates="keys")
    key = relationship("Key", back_populates="frameworks")

    def __repr__(self):
        return (
            f"<FrameworkKey id={self.id} framework_id={self.framework_id} "
            f"key_id={self.key_id} smart_score={self.smart_score} ahp_score={self.ahp_score}>"
        )
