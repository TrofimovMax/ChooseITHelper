# python seeds/options.py

import os
import sys
import json
from sqlalchemy.orm import Session

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

from database import SessionLocal
from models import Option, Question
from services.question_service import fetch_question_by_filters


def seed_options(options_file: str):
    """Seed options into the database."""
    db: Session = SessionLocal()

    try:
        with open(options_file, "r", encoding="utf-8") as o_file:
            options_data = json.load(o_file)

        for option_data in options_data:
            question_id = None

            if "question_text" in option_data:
                matching_question = db.query(Question).filter(Question.title == option_data["question_text"]).first()
                if matching_question:
                    question_id = matching_question.id
                else:
                    print(f"⚠️ Question not found: '{option_data['question_text']}'. Skipping block.")
                    continue
            else:
                matching_question, missing_keys = fetch_question_by_filters(option_data["key"], db)
                if missing_keys or matching_question is None:
                    print(f"⚠️ No matching question for keys: {option_data['key']}. Skipping.")
                    continue
                question_id = matching_question["id"]

            for opt in option_data["options"]:
                next_question_id = None
                if "next_question_text" in opt:
                    next_q = db.query(Question).filter(Question.title == opt["next_question_text"]).first()
                    if next_q:
                        next_question_id = next_q.id

                existing_option = (
                    db.query(Option)
                    .filter(Option.key == opt["key"], Option.question_id == question_id)
                    .first()
                )
                if existing_option:
                    print(f"🔁 Option '{opt['key']}' already exists for question_id={question_id}. Skipping.")
                    continue

                new_option = Option(
                    title=opt["title"],
                    description=opt.get("description"),
                    image_path=opt.get("image"),
                    key=opt["key"],
                    question_id=question_id,
                    next_question_id=next_question_id,
                )
                db.add(new_option)
                print(f"➕ Added option '{opt['key']}' to question_id={question_id}.")

        db.commit()
        print(f"✅ Options from {options_file} seeded successfully.")

    except Exception as e:
        print(f"❌ Failed to seed options from {options_file}: {e}")
        db.rollback()

    finally:
        db.close()
