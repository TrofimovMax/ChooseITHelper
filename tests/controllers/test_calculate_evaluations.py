# tests/controllers/test_calculate_evaluations.py

import pytest
import json
from unittest.mock import patch
from fastapi import BackgroundTasks
from sqlalchemy.orm import Session
from models.key import Key
from models.user import User
from models.result import Result


@pytest.fixture
def example_keys(db_session: Session):
    key1 = Key(title="web_development")
    key2 = Key(title="real_time_data")
    db_session.add_all([key1, key2])
    db_session.commit()
    return [key1.title, key2.title]


@pytest.fixture
def test_user(db_session: Session):
    user = User(
        id=1,
        full_name="test_user",
        email="test@example.com",
        role="tester",
        team_id=None
    )
    db_session.add(user)
    db_session.commit()
    return user


@pytest.fixture
def client():
    from main import app
    from fastapi.testclient import TestClient
    return TestClient(app)


@patch("controllers.calculate_evaluations.create_results_for_keys")
def test_background_task_called(mock_create_task, db_session, client, example_keys, test_user, mocker):
    db_session.query(Result).delete()
    db_session.commit()

    spy = mocker.spy(BackgroundTasks, "add_task")

    response = client.post("/evaluations/calculate_evaluations", json={"query_keys": example_keys})

    assert response.status_code == 200
    assert response.json() == {"message": "The results will be prepared soon"}

    spy.assert_called_with(
        mocker.ANY,
        mock_create_task,
        example_keys,
        1,
    )

    mock_create_task.assert_called_once_with(example_keys, 1)


def test_existing_result_returned(client, db_session, example_keys, test_user):
    result = Result(
        user_id=test_user.id,
        query_keys=example_keys,
        smart_results=[],
        ahp_results=[],
        awm_results=[]
    )
    db_session.add(result)
    db_session.commit()

    response = client.post("/evaluations/calculate_evaluations", json={"query_keys": example_keys})
    assert response.status_code == 200
    assert "result_id" in response.json()
