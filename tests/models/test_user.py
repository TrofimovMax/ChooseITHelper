# tests/models/test_user.py

import pytest
from models.user import User
from models.team import Team


def test_create_user_with_team(db_session):
    team = Team(title="DevOps")
    db_session.add(team)
    db_session.commit()
    db_session.refresh(team)

    user = User(
        full_name="Admin",
        email="admin@example.com",
        role="admin",
        team_id=team.id,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    assert user.id is not None
    assert user.full_name == "Admin"
    assert user.email == "admin@example.com"
    assert user.role == "admin"
    assert user.team_id == team.id
    assert user.team.title == "DevOps"
