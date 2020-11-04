from flask import Flask, request, jsonify
from BuzzFeedQuiz.models import Questions
from BuzzFeedQuiz.utils import get_response_for_question
app = Flask(__name__)


@app.route('/quiz', methods=['POST'])
def crud_quiz_create():
    # print(request.json)
    questions = Questions.from_json(request.json)
    if not questions.are_valid:
        return "Record not found", 400
    questions.create()

    return "Quiz created", 200


@app.route('/quiz', methods=['PUT'])
def crud_quiz_update():
    questions = Questions.from_json(request.json)
    if not questions.are_valid:
        return "Record not found", 400
    questions.update()
    return "Quiz updated", 200


@app.route('/quiz', methods=['DELETE'])
def crud_quiz_delete():
    questions = Questions.from_json(request.json)
    if not questions.are_valid:
        return "Record not found", 400
    questions.delete()
    return "Quiz deleted", 200


@app.route('/execute/<quiz_id>', methods=['POST'])
def get_question_response(quiz_id):
    return get_response_for_question(quiz_id, request.json)


if __name__ == '__main__':
    app.run(debug=True)