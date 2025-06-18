# seeds/technologies_frameworks.py

"""
List of websites with information about programming languages
https://medium.com/web-development-zone/a-complete-list-of-computer-programming-languages-1d8bc5a891f
https://en.wikipedia.org/wiki/List_of_relational_database_management_systems
https://en.wikipedia.org/wiki/NoSQL
"""

import os
import sys
import json
from sqlalchemy.orm import Session

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

from models.language import Language
from models.framework import Framework
from models.framework_key import FrameworkKey
from models.key import Key


def seed_languages(languages_file: str):
    """Seed languages into the database."""
    from database import SessionLocal
    db: Session = SessionLocal()

    try:
        with open(languages_file, "r", encoding="utf-8") as file:
            languages_data = json.load(file)

        for lang in languages_data:
            name = lang["name"]
            existing = db.query(Language).filter(Language.title == name).first()
            if existing:
                print(f"🔁 Language exists: {name}")
                continue

            db.add(Language(title=name))
            print(f"➕ Added language: {name}")

        db.commit()
        print(f"✅ Languages seeded from {languages_file}")

    except Exception as e:
        db.rollback()
        print(f"❌ Error seeding languages: {e}")
    finally:
        db.close()


def seed_frameworks(frameworks_file: str):
    """Seed frameworks and their associated keys into the database."""
    from database import SessionLocal
    db: Session = SessionLocal()

    try:
        with open(frameworks_file, "r", encoding="utf-8") as file:
            frameworks_data = json.load(file)

        for lang_block in frameworks_data:
            language_name = lang_block.get("language")
            frameworks = lang_block.get("frameworks", [])

            if not frameworks:
                print(f"⚠️ No frameworks for language '{language_name}'. Skipping.")
                continue

            language = db.query(Language).filter(Language.title == language_name).first()
            if not language:
                print(f"❌ Language not found: {language_name}")
                continue

            for fw in frameworks:
                fw_title = fw["name"]
                existing_fw = db.query(Framework).filter(Framework.title == fw_title).first()
                if existing_fw:
                    print(f"🔁 Framework exists: {fw_title}")
                    continue

                framework = Framework(
                    title=fw_title,
                    language_id=language.id,
                    feasibility=fw.get("feasibility"),
                    novelty=fw.get("novelty"),
                    usefulness=fw.get("usefulness"),
                )
                db.add(framework)
                db.flush()

                # Привязка ключей
                for key_name in fw.get("keys", []):
                    key = db.query(Key).filter(Key.title == key_name).first()
                    if not key:
                        key = Key(title=key_name, is_criterion=False)
                        db.add(key)
                        db.flush()
                        print(f"➕ Added key: {key_name}")

                    framework_key = FrameworkKey(
                        framework_id=framework.id,
                        key_id=key.id,
                        smart_score=fw.get("smart_score"),
                        ahp_score=fw.get("ahp_score"),
                    )
                    db.add(framework_key)
                    print(f"🔗 Linked key '{key_name}' to framework '{fw_title}'")

        db.commit()
        print(f"✅ Frameworks seeded from {frameworks_file}")

    except Exception as e:
        db.rollback()
        print(f"❌ Error seeding frameworks: {e}")
    finally:
        db.close()
