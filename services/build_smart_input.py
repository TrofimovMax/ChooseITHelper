from sqlalchemy.orm import Session


def build_smart_input(frameworks: list, criteria: list, db: Session):
    from models import FrameworkKey, Language

    # Get all the FrameworkKey in one request
    framework_ids = [framework.id for framework in frameworks]
    criterion_ids = [c.id for c in criteria]

    fk_records = db.query(FrameworkKey).filter(
        FrameworkKey.framework_id.in_(framework_ids),
        FrameworkKey.key_id.in_(criterion_ids)
    ).all()

    # Map for quick access
    scores_map = {
        (fk.framework_id, fk.key_id): fk.smart_score for fk in fk_records
    }

    # Compare id → key
    id_to_key = {c.id: c.key for c in criteria}

    # Getting the names of the languages
    lang_ids = [f.language_id for f in frameworks]
    lang_map = {
        lang.language_id: lang.title
        for lang in db.query(Language).filter(Language.id.in_(lang_ids)).all()
    }

    result = []

    for fw in frameworks:
        crit_scores = {
            id_to_key[c.id]: scores_map.get((fw.framework_id, c.id), 0.0)
            for c in criteria
        }
        result.append({
            "title": fw.title,
            "language_name": lang_map.get(fw.language_id, "Unknown"),
            "criteria_scores": crit_scores
        })

    return result
