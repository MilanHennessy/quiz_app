from unittest.mock import patch, MagicMock
from src.services.quiz_service import QuizService


# Test for creating a new quiz
@patch.object(QuizService, 'create_quiz')
def test_create_quiz(mock_create_quiz, client):
    # Set up the mock return value
    mock_create_quiz.return_value = 1  # A mock quiz ID

    # Make a POST request to create a quiz
    response = client.post('/api/quizzes',
                           json={'title': 'Sample Quiz', 'questions': []})

    # Write assertions to check the response
    assert response.status_code == 201
    assert response.json['quiz_id'] == 1
    mock_create_quiz.assert_called_once()


# Test for retrieving a quiz by ID
@patch.object(QuizService, 'get_quiz')
def test_get_quiz(mock_get_quiz, client):
    # Set up the mock to simulate a QuizModel object
    mock_quiz = MagicMock()
    mock_quiz.title = "Sample Quiz"
    mock_quiz.questions = ['Question 1', 'Question 2']

    # Add the to_dict method to the mock_quiz
    mock_quiz.to_dict.return_value = {
        'title': mock_quiz.title,
        'questions': mock_quiz.questions
    }

    # Assign the mock quiz to `mock_get_quiz.return_value`
    mock_get_quiz.return_value = mock_quiz

    # Make a GET request to retrieve the quiz
    response = client.get('/api/quizzes/1')

    # Write assertions to check the response
    assert response.status_code == 200
    assert response.json['title'] == "Sample Quiz"
    mock_get_quiz.assert_called_once_with(1)


# Test for submitting answers and evaluating a quiz
@patch.object(QuizService, 'evaluate_quiz')
def test_submit_quiz(mock_evaluate_quiz, client):
    # Set up the mock to simulate score calculation
    mock_evaluate_quiz.return_value = (1, "Quiz evaluated successfully")

    # Make a POST request to submit answers for a quiz
    response = client.post('/api/quizzes/1/submit',
                           json={'answers': ['Answer 1', 'Answer 2']})

    # Write assertions to check the response
    assert response.status_code == 200
    assert response.json['score'] == 1
    assert response.json['message'] == "Quiz evaluated successfully"
    mock_evaluate_quiz.assert_called_once_with(1, ['Answer 1', 'Answer 2'])
