from flask import Blueprint, request, jsonify
from src.services.quiz_service import QuizService

quiz_bp = Blueprint('quiz', __name__, url_prefix='/api/quizzes')


@quiz_bp.route('', methods=['POST'])
def create_quiz():
    service = QuizService()
    data = request.json
    quiz_id = service.create_quiz(data)
    return jsonify({
        "message": "Quiz created successfully",
        "quiz_id": quiz_id
    }), 201


@quiz_bp.route('/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    service = QuizService()
    quiz = service.get_quiz(quiz_id)
    if quiz:
        return jsonify(quiz.to_dict()), 200
    else:
        return jsonify({
            "error": "Quiz not found"
        }), 404


@quiz_bp.route('/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
    service = QuizService()
    user_answers = request.json.get('answers')
    score, message = service.evaluate_quiz(quiz_id, user_answers)
    if score is None:
        return jsonify({
            "error": "Quiz not found or evaluation failed"
        }), 404
    else:
        return jsonify({
            "score": score,
            "message": message
        }), 200
