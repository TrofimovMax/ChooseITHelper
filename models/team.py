from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.user import User  # Импортируем модель User

class Team(Base):
    __tablename__ = "teams"

    team_id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String, index=True)
    lead_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    smart_weight = Column(Integer, nullable=True)
    expert_score = Column(Integer, nullable=True)
    ahp_weight = Column(Integer, nullable=True)

    # Указываем на столбец User.team_id
    users = relationship("User", back_populates="team", foreign_keys=[User.team_id])
