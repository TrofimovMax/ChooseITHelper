# seeds/technologies_frameworks.py

"""
List of websites with information about programming languages
https://medium.com/web-development-zone/a-complete-list-of-computer-programming-languages-1d8bc5a891f
https://en.wikipedia.org/wiki/List_of_relational_database_management_systems
https://en.wikipedia.org/wiki/NoSQL
"""

# $env:PYTHONPATH="."
# python seeds/technologies_frameworks.py

import json
from sqlalchemy.orm import Session
from database import SessionLocal
from models.language import Language
from models.framework import Framework
from models.framework_key import FrameworkKey
from models.key import Key


def seed_languages(db: Session, languages_file: str):
    """Seed languages into the database."""
    with open(languages_file, "r", encoding="utf-8") as file:
        languages_data = json.load(file)

    for language_data in languages_data:
        # Check if language exists
        existing_language = db.query(Language).filter(Language.name == language_data["name"]).first()
        if not existing_language:
            language = Language(name=language_data["name"])
            db.add(language)
            print(f"Added language: {language_data['name']}")
        else:
            print(f"Language already exists: {language_data['name']}")

    db.commit()


def seed_frameworks(db: Session, frameworks_file: str):
    """Seed frameworks and their keys into the database."""
    with open(frameworks_file, "r", encoding="utf-8") as file:
        frameworks_data = json.load(file)

    for language_data in frameworks_data:
        # Check if 'frameworks' key exists
        if "frameworks" not in language_data:
            print(f"Language {language_data.get('language', 'Unknown')} does not contain frameworks. Skipping.")
            continue

        # Find language
        language = db.query(Language).filter(Language.name == language_data["language"]).first()
        if not language:
            print(f"Language not found for language: {language_data['language']}")
            continue

        for framework_data in language_data["frameworks"]:
            # Check if framework exists
            existing_framework = db.query(Framework).filter(Framework.name == framework_data["name"]).first()
            if not existing_framework:
                framework = Framework(
                    name=framework_data["name"],
                    language_id=language.language_id,
                    feasibility=framework_data.get("feasibility"),
                    novelty=framework_data.get("novelty"),
                    usefulness=framework_data.get("usefulness"),
                )
                db.add(framework)
                db.flush()

                # Add missing keys and framework keys
                if "keys" in framework_data:
                    for key_name in framework_data["keys"]:
                        # Check if key exists, add if missing
                        key = db.query(Key).filter(Key.key == key_name).first()
                        if not key:
                            key = Key(key=key_name, is_criterion=False)
                            db.add(key)
                            db.commit()
                            print(f"Added new key: {key_name}")

                        # Add framework key
                        framework_key = FrameworkKey(
                            framework_id=framework.framework_id,
                            key_id=key.id,
                            smart_score=framework_data.get("smart_score"),
                            ahp_score=framework_data.get("ahp_score"),
                        )
                        db.add(framework_key)
                        print(f"Added key '{key_name}' for framework '{framework.name}'")
            else:
                print(f"Framework already exists: {framework_data['name']}")

    db.commit()


def main():
    db = SessionLocal()
    try:
        # Seed languages
        seed_languages(db, "seeds/json/languages/languages.json")

        # Seed frameworks
        seed_frameworks(db, "seeds/json/frameworks/frameworks.json")

        # Commit after both seeds
        db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    main()
