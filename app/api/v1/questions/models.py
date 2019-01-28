#StackOverflow-lite/app/api/v1/questions/models.py
"""model for view for questions"""
import datetime

from flask import jsonify,request
from flask_restful import Resource

questions = []
deleted_questions = []

class QuestionModel():
    """Class with methods to perform CRUD operations on the list data structure"""

    def __init__(self):
        self.db = questions
        self.db2 = deleted_questions

        if len(questions) == 0:
            self.id = 1
        else:
            self.id = questions[-1]['id'] + 1
        self.id = len(questions) + 1

    def save(self):
        data = {
            'id': self.id,
            'createdOn': datetime.datetime.utcnow(),
            'createdBy': request.json.get('createdBy'),
            'title': request.json.get('title'),
            'question': request.json.get('question')
        }

        self.db.append(data)
        return self.id

    def get_all(self):
        if not self.db:
            return None
        return self.db

    def find(self, question_id):
        for question in self.db:
            if question['id'] == question_id:
                return question

        return "question does not exist"

    def delete(self, question):
        self.db.remove(question)
        self.db2.append(question)
        return "deleted"

    def edit_question_title(self, question):
        "Method to edit a questions title"
        question['title'] = request.json.get('title')
        return "updated"

    def edit_question_body(self, question):
        "Method to edit a questions body"
        question['question'] = request.json.get('question')
        return "updated"
