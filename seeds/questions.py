# python seeds/questions.py

import argparse

import sys
import os
import json
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Key, QuestionKey, Question

# $env:PYTHONPATH="."
# python seeds/questions.py --questions seeds/json/questions/questions.json
# python seeds/questions.py --questions seeds/json/questions/criteria_questions.json


current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)


def seed_questions(questions_file: str):
    """Seed questions and their associated keys into the database."""
    db: Session = SessionLocal()

    with open(questions_file, "r", encoding="utf-8") as q_file:
        questions_data = json.load(q_file)

    for question_data in questions_data:
        if "question" not in question_data:
            print(f"Skipping invalid entry: {question_data}")
            continue
        # Create a question
        question = Question(text=question_data["question"])
        db.add(question)
        db.commit()  # Commit to generate question_id

        # Add keys (check existence in 'keys' table, add if missing) and create relationships
        for key_name in question_data["key"]:
            key = db.query(Key).filter(Key.key == key_name).first()
            if not key:
                key = Key(key=key_name, is_criterion=question_data.get("is_criterion", False))
                db.add(key)
                db.commit()
                print(f"Added new key: {key_name}")

            question_key = QuestionKey(question_id=question.question_id, key_id=key.id)
            db.add(question_key)

        db.commit()

    db.close()
    print(f"Questions from {questions_file} have been successfully added!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seed questions and options into the database.")
    parser.add_argument(
        "--questions",
        type=str,
        help="Path to the JSON file containing questions.",
        required=True,
    )

    args = parser.parse_args()

    seed_questions(args.questions)
