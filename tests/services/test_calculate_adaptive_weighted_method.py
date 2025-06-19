# tests/services/test_calculate_adaptive_weighted_method.py

import pytest
from services.calculate_adaptive_weighted_method import calculate_adaptive_weighted_method
from models.framework import Framework
from models.resource import Resource, ResourceType


@pytest.fixture
def sample_data(db_session):
    from models.language import Language

    js = Language(id=10, title="JavaScript")
    py = Language(id=14, title="Python")
    go = Language(id=48, title="Golang")
    db_session.add_all([js, py, go])
    db_session.commit()
    framework = Framework(
        id=1001,
        title="GinTest",
        language_id=48,
        feasibility=0.72,
        novelty=0.68,
        usefulness=0.6,
    )
    db_session.add(framework)
    db_session.commit()

    resources = [
        # Feasibility
        Resource(id=2001, title="hh.ru", framework_id=1001, language_id=48, type=ResourceType.feasibility, rank=50, total=800),
        Resource(id=2002, title="LinkedIn", framework_id=1001, language_id=48, type=ResourceType.feasibility, rank=29000, total=29000),
        Resource(id=2003, title="Indeed", framework_id=1001, language_id=48, type=ResourceType.feasibility, rank=1722, total=1829),
        # Novelty
        Resource(id=2004, title="GitHub", framework_id=1001, language_id=48, type=ResourceType.novelty, rank=82800, total=89000),
        # Usefulness
        Resource(id=2005, title="StackOverflow", framework_id=1001, language_id=48, type=ResourceType.usefulness, rank=25000, total=400000),
    ]
    db_session.bulk_save_objects(resources)
    db_session.commit()

    return framework


def test_calculate_adaptive_weighted_method(db_session, sample_data):
    frameworks = [
        {
            "id": 1001,
            "title": "GinTest",
            "language_name": "Golang",
            "criteria_scores": {
                "low_cost": 0.65,
                "standard_security": 0.65,
                "small_scale": 0.0,
                "low_priority": 0.65,
                "basic_customization": 0.65,
            },
            "feasibility": sample_data.feasibility,
            "novelty": sample_data.novelty,
            "usefulness": sample_data.usefulness,
        }
    ]

    criteria_weights = {
        "low_cost": 0.2,
        "standard_security": 0.2,
        "small_scale": 0.2,
        "low_priority": 0.2,
        "basic_customization": 0.2,
    }

    raw_frameworks = [sample_data]

    result = calculate_adaptive_weighted_method(
        frameworks=frameworks,
        criteria_weights=criteria_weights,
        raw_frameworks=raw_frameworks,
        db=db_session
    )

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["framework_title"] == "GinTest"

    # Checking the approximate value (from calculations: ~0.19952)
    assert abs(result[0]["awm_score"] - 0.19952) < 0.0005
