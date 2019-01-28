#StackOverflow-lite/app/api/v1/questions/views.py
"""views for questions"""
from flask import jsonify, request
from flask_restful import Resource

from .models import QuestionModel

class Questions(Resource):
    """docstring for Questions class"""

    def __init__(self):
        """initiliase the Questions class"""
        self.db = QuestionModel()

    def post(self):
        """docstring for saving a Question"""
        question_id = self.db.save()

        return jsonify({
            "status": 201,
            "data": {
                "id": question_id,
                "message": "Created a question record"
            }
        })
