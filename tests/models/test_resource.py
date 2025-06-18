# tests/models/test_resource.py

from models.resource import Resource
from models.language import Language
from models.framework import Framework


def test_create_resource_model(db_session):
    language = Language(title="Python")
    db_session.add(language)
    db_session.flush()

    framework = Framework(
        title="FastAPI",
        language_id=language.id,
        feasibility=0.9,
        novelty=0.8,
        usefulness=0.95
    )
    db_session.add(framework)
    db_session.flush()

    resource = Resource(
        title="GitHub Stars",
        language_id=language.id,
        framework_id=framework.id,
        rank=42000,
        total=89000
    )
    db_session.add(resource)
    db_session.commit()

    result = db_session.query(Resource).first()
    assert result is not None
    assert result.id is not None
    assert result.title == "GitHub Stars"
    assert result.rank == 42000
    assert result.total == 89000
    assert result.language.title == "Python"
    assert result.framework.title == "FastAPI"
