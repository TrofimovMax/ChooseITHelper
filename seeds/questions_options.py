# seeds/questions_options.py

import sys
import os
import json
import argparse
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from models.question import Question
from models.option import Option
from models.question_key import QuestionKey
from models.key import Key
from database import SessionLocal

# Adding the root directory of the project to sys.path
# $env:PYTHONPATH="G:\myData\magistratura_lab_works\ChooseITHelper"
# python seeds/questions_options.py --questions seeds/json/questions/questions.json --options seeds/json/options/options.json
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)


def seed_questions(questions_file: str):
    """Seed questions and their associated keys into the database."""
    db: Session = SessionLocal()

    with open(questions_file, "r", encoding="utf-8") as q_file:
        questions_data = json.load(q_file)

    for question_data in questions_data:
        # Create a question
        question = Question(text=question_data["question"])
        db.add(question)
        db.commit()  # Commit to generate question_id

        # Add keys (check existence in 'keys' table, add if missing) and create relationships
        for key_name in question_data["key"]:
            key = db.query(Key).filter(Key.key == key_name).first()
            if not key:
                key = Key(key=key_name)
                db.add(key)
                db.commit()
                print(f"Added new key: {key_name}")

            question_key = QuestionKey(question_id=question.question_id, key_id=key.id)
            db.add(question_key)

        db.commit()

    db.close()
    print(f"Questions from {questions_file} have been successfully added!")


def seed_options(options_file: str):
    """Seed options into the database based on keys."""
    db: Session = SessionLocal()

    with open(options_file, "r", encoding="utf-8") as o_file:
        options_data = json.load(o_file)

    for option_data in options_data:
        keys = option_data["key"]

        # Retrieve key IDs from the 'keys' table
        key_ids = [key.id for key in db.query(Key).filter(Key.key.in_(keys)).all()]
        if not key_ids:
            print(f"Keys {keys} not found in 'keys' table. Skipping.")
            continue

        # Find question_id matching all the given keys
        matching_question_id = (
            db.query(QuestionKey.question_id)
            .filter(QuestionKey.key_id.in_(key_ids))
            .group_by(QuestionKey.question_id)
            .having(func.count(QuestionKey.key_id) == len(key_ids))
            .first()
        )

        if not matching_question_id:
            print(f"No question matches keys: {keys}. Skipping.")
            continue

        question_id = matching_question_id[0]

        # Add options to the question
        for opt in option_data["options"]:
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
                description=opt["description"],
                image_path=opt["image"],
                key=opt["key"],
                question_id=question_id,
            )
            db.add(new_option)
            print(f"Added option '{opt['key']}' for question_id={question_id}.")

        db.commit()

    db.close()
    print(f"Options from {options_file} have been successfully added!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seed questions and options into the database.")
    parser.add_argument(
        "--questions",
        type=str,
        help="Path to the JSON file containing questions.",
        required=True,
    )
    parser.add_argument(
        "--options",
        type=str,
        help="Path to the JSON file containing options.",
        required=True,
    )

    args = parser.parse_args()

    seed_questions(args.questions)
    seed_options(args.options)
