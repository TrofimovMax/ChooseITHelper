# tests/seeds/test_resources.py

import tempfile
import json
from models import Language, Framework, Resource
from models.resource import ResourceType
from seeds.resources import seed_resources


def test_seed_resources_creates_entries(db_session):
    # Подготовка данных: языки и фреймворки
    golang = Language(title="Golang")
    javascript = Language(title="JavaScript")
    db_session.add_all([golang, javascript])
    db_session.flush()

    gin = Framework(title="Gin", language_id=golang.id, feasibility=0.8, novelty=0.7, usefulness=0.9)
    nest = Framework(title="Node.js + NestJS", language_id=javascript.id, feasibility=0.85, novelty=0.75, usefulness=0.92)
    db_session.add_all([gin, nest])
    db_session.commit()

    test_data = [
        {
            "framework_title": "Gin",
            "language_name": "Golang",
            "title": "GitHub Stars",
            "rank": 61000,
            "total": 89000,
            "type": "novelty"
        },
        {
            "framework_title": "Node.js + NestJS",
            "language_name": "JavaScript",
            "title": "GitHub Stars",
            "rank": 59000,
            "total": 89000,
            "type": "novelty"
        }
    ]

    with tempfile.NamedTemporaryFile(mode="w+", suffix=".json", delete=False) as tmpfile:
        json.dump(test_data, tmpfile)
        tmpfile.flush()

        seed_resources(tmpfile.name, db_session)
        db_session.commit()

    resources = db_session.query(Resource).all()
    assert len(resources) == 2

    titles = [res.title for res in resources]
    assert all(t == "GitHub Stars" for t in titles)

    scores = [res.rank for res in resources]
    assert 61000 in scores and 59000 in scores
