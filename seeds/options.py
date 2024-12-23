# python seeds/options.py

import argparse
import sys
import os
import json
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Option, Question
from services.question_service import fetch_question_by_filters

# $env:PYTHONPATH="."
# python seeds/options.py --options seeds/json/options/options.json
# python seeds/options.py --options seeds/json/options/criteria_options.json


current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)


def seed_options(options_file: str):
    """Seed options into the database."""
    db: Session = SessionLocal()

    with open(options_file, "r", encoding="utf-8") as o_file:
        options_data = json.load(o_file)

    for option_data in options_data:
        # Determine question_id using question_text or keys
        question_id = None

        if "question_text" in option_data:
            matching_question = db.query(Question).filter(Question.text == option_data["question_text"]).first()
            if matching_question:
                question_id = matching_question.question_id
            else:
                print(f"Question with text '{option_data['question_text']}' not found. Skipping options.")
                continue
        else:
            matching_question, missing_keys = fetch_question_by_filters(option_data["key"], db)
            if missing_keys is not None or matching_question is None:
                print(f"No question matches keys: {option_data['key']}. Skipping options.")
                continue
            question_id = matching_question["question_id"]

        # Add options to the question
        for opt in option_data["options"]:
            next_question_id = None
            if "next_question_text" in opt:
                next_question = db.query(Question).filter(Question.text == opt["next_question_text"]).first()
                if next_question:
                    next_question_id = next_question.question_id

            existing_option = (
                db.query(Option)
                .filter(Option.key == opt["key"], Option.question_id == question_id)
                .first()
            )
            if existing_option:
                print(f"Option '{opt['key']}' already exists for question_id={question_id}. Skipping.")
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
            print(f"Added option '{opt['key']}' for question_id={question_id}.")

        db.commit()

    db.close()
    print(f"Options from {options_file} have been successfully added!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seed options into the database.")
    parser.add_argument(
        "--options",
        type=str,
        help="Path to the JSON file containing options.",
        required=True,
    )

    args = parser.parse_args()

    seed_options(args.options)
