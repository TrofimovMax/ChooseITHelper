# services/format_results.py

from models.language import Language
from sqlalchemy.orm import Session


def format_results(raw_scores: dict, frameworks: list, db: Session, method_key: str = "score") -> list[dict]:
    """
    Converts the dictionary {name: score} to a list of dictionaries with the added language.
    """
    framework_map = {f.title: f for f in frameworks}
    results = []
    for framework_title, score in raw_scores.items():
        framework = framework_map.get(framework_title)
        if framework:
            language_name = db.query(Language.title).filter(Language.id == framework.language_id).scalar()
            results.append({
                "framework_title": framework_title,
                "language_name": language_name,
                method_key: round(float(score), 5)
            })
    results.sort(key=lambda x: x[method_key], reverse=True)
    return results
