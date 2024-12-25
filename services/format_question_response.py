from models import Question


def format_question_response(question: Question):
    """
    Format the question and its options for the response.
    """
    return {
        "question_id": question.question_id,
        "text": question.text,
        "options": [
            {
                "option_id": opt.option_id,
                "title": opt.title,
                "description": opt.description,
                "key": opt.key,
                "image_url": opt.image_path,
                "next_question_id": opt.next_question_id
            }
            for opt in (question.options or [])
        ],
    }