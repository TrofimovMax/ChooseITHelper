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
from database import SessionLocal

# Adding the root directory of the project to sys.path
# $env:PYTHONPATH="G:\myData\magistratura_lab_works\ChooseITHelper"
# python seeds/questions_options.py --questions seeds/json/questions/questions.json --options seeds/json/options/options.json
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)


def seed_questions(questions_file: str):
    """Seeding the questions and their keys into the database"""
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
    print(f"Вопросы из {questions_file} успешно добавлены!")


def seed_options(options_file: str):
    """Seeding options into a database with an exact key match"""
    db: Session = SessionLocal()

    with open(options_file, "r", encoding="utf-8") as o_file:
        options_data = json.load(o_file)

    for option_data in options_data:
        keys = option_data["key"]

        matching_question_id = (
            db.query(QuestionKey.question_id)
            .filter(QuestionKey.key.in_(keys))
            .group_by(QuestionKey.question_id)
            .having(func.count(QuestionKey.key) == len(keys))
            .first()
        )

        if not matching_question_id:
            print(f"No questions for keys: {keys}. Skip it.")
            continue

        question_id = matching_question_id[0]

        for opt in option_data["options"]:
            existing_option = (
                db.query(Option)
                .filter(
                    Option.key == opt["key"],
                    Option.question_id == question_id,
                )
                .first()
            )
            if existing_option:
                print(
                    f"The option '{opt['key']}' already exists for question_id={question_id}. Skip it."
                )
                continue

            new_option = Option(
                title=opt["title"],
                description=opt["description"],
                image_path=opt["image"],
                key=opt["key"],
                question_id=question_id,
            )
            db.add(new_option)
            print(f"Added the option '{opt['key']}' for question_id={question_id}.")

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
