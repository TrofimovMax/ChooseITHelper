# seeds/users.py

from models.user import User
from sqlalchemy.orm import Session


def seed_admin_user(db: Session):
    existing = db.query(User).filter(User.email == "admin@example.com").first()
    if existing:
        print("⚠️ Admin user already exists, skipping.")
        return

    admin = User(
        full_name="SystemAdministrator",
        email="admin@example.com",
        role="Admin",
        team_id=None
    )

    db.add(admin)
    print("✅ Admin user seeded.")
