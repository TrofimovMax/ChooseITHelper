# services/question_service.py

from sqlalchemy.orm import Session
from models.question import Question
from models.option import Option
from models.question_key import QuestionKey

def fetch_start_question(db: Session):
    question = db.query(Question).filter(Question.parent_option_id == None).first()
    if not question:
        return {"message": "No start question found"}, 404
    return {
        "question_id": question.question_id,
        "text": question.text,
        "options": [
            {"option_id": opt.option_id, "text": opt.text, "image_url": opt.image_url}
            for opt in question.options
        ],
    }

def fetch_next_question(option_id: int, db: Session):
    option = db.query(Option).filter(Option.option_id == option_id).first()
    if not option:
        return {"message": "Option not found"}, 404

    selected_keys = [key.key for key in option.question.keys]

    next_question = (
        db.query(Question)
        .join(QuestionKey)
        .filter(QuestionKey.key.in_(selected_keys))
        .first()
    )

    if next_question:
        return {
            "question_id": next_question.question_id,
            "text": next_question.text,
            "options": [
                {"option_id": opt.option_id, "text": opt.text, "image_url": opt.image_url}
                for opt in next_question.options
            ],
        }
    return {"message": "complete"}

def complete_survey_logic(answers: list[int], db: Session):
    selected_options = db.query(Option).filter(Option.option_id.in_(answers)).all()
    result = [opt.text for opt in selected_options]
    return {"message": f"Спасибо за ваши ответы: {', '.join(result)}"}
