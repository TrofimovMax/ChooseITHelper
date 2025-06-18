# python seeds/questions.py

import os
import json
import sys
from sqlalchemy.orm import Session

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

from database import SessionLocal
from models import Key, QuestionKey, Question


def seed_questions(questions_file: str):
    """Seed questions and their associated keys into the database."""
    db: Session = SessionLocal()
    print(f"📄 Reading file: {questions_file}")

    try:
        with open(questions_file, "r", encoding="utf-8") as q_file:
            questions_data = json.load(q_file)

        print(f"🔢 Found {len(questions_data)} entries in file.")

        for idx, question_data in enumerate(questions_data, start=1):
            print(f"\n➡️ Processing entry #{idx}: {question_data.get('question', 'NO_QUESTION')}")

            if "question" not in question_data:
                print(f"⚠️ Skipping invalid entry (missing 'question'): {question_data}")
                continue

            question = Question(title=question_data["question"])
            db.add(question)
            db.flush()
            print(f"📝 Added question: {question.title} with ID: {question.id}")

            if "filter_keys" not in question_data:
                print(f"⚠️ No 'filter_keys' in entry: {question_data}. Skipping keys.")
                continue

            for key_name in question_data["filter_keys"]:
                key = db.query(Key).filter(Key.title == key_name).first()
                if not key:
                    key = Key(title=key_name, is_criterion=question_data.get("is_criterion", False))
                    db.add(key)
                    db.flush()
                    print(f"➕ Added new key: {key_name} (is_criterion={key.is_criterion})")
                else:
                    print(f"🔁 Key already exists: {key_name}")

                question_key = QuestionKey(question_id=question.id, key_id=key.id)
                db.add(question_key)
                print(f"🔗 Linked question ID {question.id} to key ID {key.id}")

        db.commit()
        print(f"\n✅ Questions from {questions_file} have been successfully seeded.")

    except Exception as e:
        print(f"❌ Failed to seed questions from {questions_file}: {e}")
        db.rollback()

    finally:
        db.close()
        print("🔚 Database session closed.")
