# seeds/main.py

import sys
import os
import glob

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

from sqlalchemy.orm import Session
from database import SessionLocal
from seeds.questions import seed_questions
from seeds.options import seed_options
from seeds.technologies_frameworks import seed_languages, seed_frameworks


def find_json_files(directory: str) -> list[str]:
    """Recursively finds all JSON files in the specified directory."""
    return sorted(glob.glob(os.path.join(directory, "**", "*.json"), recursive=True))


def run_seeding():
    print("🔄 Starting full database seeding...")
    db: Session = SessionLocal()

    try:
        # questions
        question_files = find_json_files("seeds/json/questions")
        for q_file in question_files:
            print(f"📥 Seeding questions from: {q_file}")
            seed_questions(q_file)

        # options
        option_files = find_json_files("seeds/json/options")
        for o_file in option_files:
            print(f"📥 Seeding options from: {o_file}")
            seed_options(o_file)

        # languages
        languages_files = find_json_files("seeds/json/languages")
        for l_file in languages_files:
            print(f"📥 Seeding languages from: {l_file}")
            seed_languages(l_file)

        # frameworks
        frameworks_files = find_json_files("seeds/json/frameworks")
        for f_file in frameworks_files:
            print(f"📥 Seeding frameworks from: {f_file}")
            seed_frameworks(f_file)

        db.commit()
        print("✅ Seeding completed successfully.")

    except Exception as e:
        print(f"❌ Seeding failed: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    run_seeding()
