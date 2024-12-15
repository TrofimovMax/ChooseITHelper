from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.result import Result
from models.question_key import QuestionKey
from services.create_results_for_keys import create_results_for_keys

router = APIRouter()


@router.post("/calculate_evaluations")
def calculate_evaluations(query_keys: list[str], db: Session = Depends(get_db)):
    question_keys = db.query(QuestionKey).filter(QuestionKey.key.in_(query_keys)).all()
    if not question_keys:
        raise HTTPException(status_code=404, detail="Keys not found")

    results = db.query(Result).filter(Result.query_keys.contains(query_keys)).all()

    if not results:
        create_results_for_keys(query_keys)

        return {"message": "The results will be prepared soon"}

    return {"results": results}
