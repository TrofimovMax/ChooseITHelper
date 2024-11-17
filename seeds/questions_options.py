# seeds/questions_options.py

import sys
import os
import json
import argparse
from sqlalchemy.orm import Session
from models.question import Question
from models.option import Option
from models.question_key import QuestionKey
from database import SessionLocal

# Adding the root directory of the project to sys.path
# $env:PYTHONPATH="G:\myData\magistratura_lab_works\ChooseITHelper"
# python seeds/questions_options.py --questions seeds/json/questions/questions.json --options seeds/json/options/options.json
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)


def seed_questions(questions_file: str):
    db: Session = SessionLocal()

    with open(questions_file, "r", encoding="utf-8") as q_file:
        questions_data = json.load(q_file)

    for question_data in questions_data:
        question = Question(text=question_data["question"])
        db.add(question)
        db.commit()

        keys = [
            QuestionKey(question_id=question.question_id, key=key)
            for key in question_data["key"]
        ]
        db.add_all(keys)
        db.commit()

    db.close()
    print(f"Questions from {questions_file} successfully seeded!")


def seed_options(options_file: str):
    db: Session = SessionLocal()

    with open(options_file, "r", encoding="utf-8") as o_file:
        options_data = json.load(o_file)

    for option_data in options_data:
        keys = option_data["key"]
        questions = (
            db.query(Question)
            .join(QuestionKey)
            .filter(QuestionKey.key.in_(keys))
            .all()
        )

        for question in questions:
            for opt in option_data["options"]:
                db.add(
                    Option(
                        title=opt["title"],
                        description=opt["description"],
                        image_path=opt["image"],
                        question_id=question.question_id,
                    )
                )
        db.commit()

    db.close()
    print(f"Options from {options_file} successfully seeded!")


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
