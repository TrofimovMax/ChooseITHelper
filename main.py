from typing import Union

from models import User, Technology, Framework, Team, Developer
from database import engine, get_db
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models.base import Base


app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

