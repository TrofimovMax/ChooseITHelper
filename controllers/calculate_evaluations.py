# controllers/calculate_evaluations.py

from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from database import get_db
from models.result import Result
from models.key import Key
from services.create_results_for_keys import create_results_for_keys
from pydantic import BaseModel
from typing import List

router = APIRouter()


class EvaluationRequest(BaseModel):
    query_keys: List[str]


@router.post("/calculate_evaluations")
def calculate_evaluations(
    request: EvaluationRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    """
    Calculate evaluations for the given keys. If results are not found,
    an asynchronous task is initiated to compute and store the results.
    """
    query_keys = request.query_keys

    # Getting the key IDs from the database
    key_ids = [key_id[0] for key_id in db.query(Key.id).filter(Key.title.in_(query_keys)).all()]

    if not key_ids:
        raise HTTPException(status_code=404, detail="Keys not found")

    # Checking if there are already results for these keys.
    result_id = db.query(Result.id).filter(Result.query_keys.contains(query_keys)).limit(1).first()

    if not result_id:
        # Running a background task for the calculation
        # TODO: Replace hardcoded user_id when auth is ready
        background_tasks.add_task(create_results_for_keys, query_keys, 1)
        return {"message": "The results will be prepared soon"}

    # Returning already existing results
    return {
        "result_id": result_id[0]
    }
