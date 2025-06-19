# models/resource.py

import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from models.base import Base


class ResourceType(enum.Enum):
    feasibility = "feasibility"
    novelty = "novelty"
    usefulness = "usefulness"


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    language_id = Column(Integer, ForeignKey("languages.id"), nullable=False)
    framework_id = Column(Integer, ForeignKey("frameworks.id"), nullable=False)
    rank = Column(Integer)
    total = Column(Integer)
    type = Column(Enum(ResourceType), nullable=False)

    language = relationship("Language")
    framework = relationship("Framework")
