# tests/models/test_user.py

# run test with
# $env:PYTHONPATH="."
# $env:ENV_FILE=".env.test"; pytest tests/models/test_user.py

import pytest
from models.user import User
from models.team import Team


def test_create_user_with_team(db_session):
    team = Team(team_name="DevOps")
    db_session.add(team)
    db_session.commit()
    db_session.refresh(team)

    user = User(
        name="Admin",
        email="admin@example.com",
        role="admin",
        team_id=team.team_id,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    assert user.user_id is not None
    assert user.name == "Admin"
    assert user.email == "admin@example.com"
    assert user.role == "admin"
    assert user.team_id == team.team_id
    assert user.team.team_name == "DevOps"
