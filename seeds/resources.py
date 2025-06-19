# seeds/resources.py

import json
from sqlalchemy.orm import Session
from models.resource import Resource
from models.language import Language
from models.framework import Framework


def seed_resources(file_path: str, db: Session):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"🌱 Seeding resources from {file_path}...")

    for item in data:
        framework_title = item.get("framework_title")
        language_name = item.get("language_name")
        resource_title = item.get("title")
        rank = item.get("rank")
        total = item.get("total")
        type = item.get("type")

        print(f"🔍 Checking: {framework_title=} {language_name=}")

        language_id = db.query(Language.id).filter(Language.title == language_name).scalar()
        framework_id = db.query(Framework.id).filter(Framework.title == framework_title).scalar()

        print(f"🎯 Resolved: {language_id=} {framework_id=}")

        if not all([framework_title, language_name, resource_title, rank, total]):
            print(f"⚠️ Skipping incomplete entry: {item}")
            continue

        if not language_id or not framework_id:
            print(f"❌ Not found in DB: {framework_title} or {language_name}")
            continue

        resource = Resource(
            title=resource_title,
            language_id=language_id,
            framework_id=framework_id,
            rank=rank,
            total=total,
            type=type
        )

        db.add(resource)
        print(f"✅ Added resource: {resource_title} for {framework_title} ({rank}/{total})")

    print(f"✅ Finished seeding resources from {file_path}")

