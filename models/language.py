# models/language.py

from sqlalchemy import Column, Integer, String
from models.base import Base


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

    def __repr__(self):
        return f"<Language id={self.id} title={self.title}>"
