# routes.py

from fastapi import FastAPI
from controllers import question_router, user_router

def init_routes(app: FastAPI):
    app.include_router(question_router, prefix="/questions", tags=["Questions"])
    app.include_router(user_router, prefix="/users", tags=["Users"])
