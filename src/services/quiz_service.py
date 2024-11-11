from src.models.quiz_model import QuizModel


class QuizService:
    def create_quiz(self, quiz_data):
        title = quiz_data.get("title")
        questions = quiz_data.get("questions")

        quiz = QuizModel(title=title, questions=questions)

        quiz.save()
        return quiz.id

    def get_quiz(self, quiz_id):
        return QuizModel.get_quiz(quiz_id)

    def evaluate_quiz(self, quiz_id, user_answers):
        quiz = self.get_quiz(quiz_id)

        if quiz is None:
            return None, "Quiz not found"

        correct_answers = quiz.questions
        score = sum(
            1 for question, answer in zip(correct_answers, user_answers)
            if question['answer'] == answer
        )

        return score, "Evaluation complete"
