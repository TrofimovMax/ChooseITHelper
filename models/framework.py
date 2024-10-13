# models/framework.py

from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from models.base import Base
import enum


class ApplicationArea(enum.Enum):
    WEB_DEVELOPMENT = "Web Development"
    MOBILE_DEVELOPMENT = "Mobile Development"
    GAME_DEVELOPMENT = "Game Development"
    DATA_SCIENCE = "Data Science"
    MACHINE_LEARNING = "Machine Learning"
    EMBEDDED_SYSTEMS = "Embedded Systems"
    SYSTEMS_PROGRAMMING = "Systems Programming"
    BUSINESS_SYSTEMS = "Business Systems"
    SCIENTIFIC_COMPUTING = "Scientific Computing"
    AUTOMATION = "Automation"
    SCRIPTING = "Scripting"
    GENERAL_PURPOSE = "General-purpose"
    DOMAIN_SPECIFIC = "Domain-specific"


class Framework(Base):
    __tablename__ = "frameworks"

    framework_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    language_id = Column(Integer, ForeignKey("languages.language_id"))
    application_area = Column(Enum(ApplicationArea), nullable=True)
    smart_weight = Column(Integer, nullable=True)
    expert_score = Column(Integer, nullable=True)
    ahp_weight = Column(Integer, nullable=True)
