# services/fetch_frameworks_by_filters.py

from sqlalchemy import func
from sqlalchemy.orm import Session

from models import FrameworkKey, Framework


def fetch_frameworks_by_filters(keys_ids: list[int], db: Session):
    """
    Fetch frameworks based on the provided key IDs.
    Returns a list of framework IDs sorted by the count of matching keys.
    """
    top_framework_ids = (
        db.query(FrameworkKey.id)
        .filter(FrameworkKey.key_id.in_(keys_ids))
        .group_by(FrameworkKey.framework_id)
        .order_by(func.count(FrameworkKey.key_id).desc())
        .limit(5)
        .all()
    )

    ids = [row.framework_id for row in top_framework_ids]

    return db.query(Framework).filter(Framework.id.in_(ids)).all()
