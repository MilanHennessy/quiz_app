from flask import Blueprint, request, jsonify
from src.services.quiz_service import QuizService

quiz_bp = Blueprint('quiz', __name__, url_prefix='/api/quizzes')

@quiz_bp.route('', methods=['POST'])
def create_quiz():
    service = QuizService()  # Initialize the QuizService
    data = request.json  # Retrieve JSON data from the request

    # Call the create_quiz method in the service
    quiz_id = service.create_quiz(data)  # Assume create_quiz returns the created quiz ID

    # Return a JSON response with the quiz ID and a 201 status
    return jsonify({"message": "Quiz created successfully", "quiz_id": quiz_id}), 201

@quiz_bp.route('/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    service = QuizService()  # Initialize the QuizService
    quiz = service.get_quiz(quiz_id)  # Retrieve the quiz by its ID

    if quiz:
        return jsonify(quiz.to_dict()), 200  # Convert the quiz to a dict and return it
    else:
        return jsonify({"error": "Quiz not found"}), 404  # Return error message with status 404


@quiz_bp.route('/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
    service = QuizService()  # Initialize the QuizService
    
    # Retrieve answers from the request JSON
    user_answers = request.json.get('answers')  # Get answers from the request

    # Use the service to evaluate the quiz with the provided answers
    score, message = service.evaluate_quiz(quiz_id, user_answers)  # Assume evaluate_quiz returns a score and message

    # Check if evaluation was successful and return the response
    if score is None:
        return jsonify({"error": "Quiz not found or evaluation failed"}), 404  # Return error with status 404
    else:
        return jsonify({"score": score, "message": message}), 200  # Return score and message with status 200
