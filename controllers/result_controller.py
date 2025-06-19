# controllers/result_controller.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Option, Key
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

    query_keys = result.query_keys

    option_titles = {
        o.key: o.title
        for o in db.query(Option).filter(Option.key.in_(query_keys)).all()
    }

    key_flags = {
        k.title: k.is_criterion
        for k in db.query(Key).filter(Key.title.in_(query_keys)).all()
    }

    criteria = []
    alternatives = []

    for key in query_keys:
        title = option_titles.get(key, key)
        is_criterion = key_flags.get(key, False)
        if is_criterion:
            criteria.append(title)
        else:
            alternatives.append(title)

    return {
        "id": result.id,
        "alternatives": alternatives,
        "criteria": criteria,
        "smart_results": result.smart_results,
        "ahp_results": result.ahp_results,
        "adaptive_weighted_results": result.awm_results,
    }
