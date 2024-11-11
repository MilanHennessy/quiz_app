from src.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import PickleType


class QuizModel(db.Model):
    __tablename__ = 'quizzes'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    questions = Column(PickleType, nullable=False)

    def __init__(self, title, questions):
        self.title = title
        self.questions = questions

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_quiz(cls, quiz_id):
        return cls.query.get(quiz_id)

    def to_dict(self):
        """Convert the QuizModel instance to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'questions': self.questions
        }
