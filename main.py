# main.py

from fastapi import FastAPI
from models import Base
from database import engine
from routes import init_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

init_routes(app)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
