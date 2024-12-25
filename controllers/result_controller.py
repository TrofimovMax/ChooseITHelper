# controllers/result_controller.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.result import Result

router = APIRouter()

@router.get("/{result_id}")
def get_result(result_id: int, db: Session = Depends(get_db)):
    """
    Get a result by its ID.
    """
    result = db.query(Result).filter(Result.id == result_id).first()

    if not result:
        raise HTTPException(status_code=404, detail="Result not found")

    return {
        "id": result.id,
        "query_keys": result.query_keys,
        "smart_results": result.smart_results,
        "ahp_results": result.ahp_results,
        "adaptive_weighted_results": result.adaptive_weighted_results,
    }
