# services/fetch_frameworks_by_filters.py

from sqlalchemy import func
from sqlalchemy.orm import Session

from models import FrameworkKey


def fetch_frameworks_by_filters(keys_ids: list[int], db: Session):
    """
    Fetch frameworks based on the provided key IDs.
    Returns a list of framework IDs sorted by the count of matching keys.
    """
    frameworks = (
        db.query(FrameworkKey.framework_id, func.count(FrameworkKey.key_id).label("key_count"))
        .filter(FrameworkKey.key_id.in_(keys_ids))
        .group_by(FrameworkKey.framework_id)
        .order_by(func.count(FrameworkKey.key_id).desc())
        .limit(5)  # Fetch top 5 frameworks
        .all()
    )
    return [framework.framework_id for framework in frameworks]
