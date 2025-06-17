# routes.py

from fastapi import FastAPI
from controllers import calculate_evaluations
from controllers.result_controller import router as result_router
from controllers.question_controller import router as question_router
from controllers.user_controller import router as user_router


def init_routes(app: FastAPI):
    app.include_router(calculate_evaluations.router, prefix="/evaluations", tags=["Evaluations"])
    app.include_router(result_router, prefix="/results", tags=["Results"])
    app.include_router(question_router, prefix="/questions", tags=["Questions"])
    app.include_router(user_router, prefix="/users", tags=["Users"])
