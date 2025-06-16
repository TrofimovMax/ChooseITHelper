# models/language.py

from sqlalchemy import Column, Integer, String
from models.base import Base


class Language(Base):
    __tablename__ = "languages"

    language_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    def __repr__(self):
        return f"<Language language_id={self.language_id} name={self.name}>"
