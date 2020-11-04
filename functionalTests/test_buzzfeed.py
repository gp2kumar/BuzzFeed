import requests
from unittest import TestCase


class TestBuzzFeed(TestCase):

    def test_quiz_api(self):
        data = [{
            "question": {
                "id": "uuid",
                "text": "What is the question?",
                "Choices": [{
                    "id": "uuid",
                    "text": "Option 1",
                    "metadata": {},
                },
                    {
                        "id": "uuid",
                        "text": "Option 2",
                        "metadata": {},
                    }],
                "metadata": {}
            }}]
        res = requests.post('http://127.0.0.1:5000/quiz', json=data)
        self.assertEqual(res.status_code, 200)

    def test_quiz_update_api(self):
        data = [{
            "question": {
                "id": "uuid",
                "text": "What is the question?",
                "Choices": [{
                    "id": "uuid",
                    "text": "Option 1",
                    "metadata": {},
                },
                    {
                        "id": "uuid",
                        "text": "Option 2",
                        "metadata": {},
                    }],
                "metadata": {}
            }}]
        res = requests.put('http://127.0.0.1:5000/quiz', json=data)
        self.assertEqual(res.status_code, 200)

    def test_execute_quiz(self):
        data = [{
            "question": {
                "id": "uuid",
                "text": "What is the question?",
                "Choices": [{
                    "id": "uuid",
                    "text": "Option 1",
                    "metadata": {},
                },
                    {
                        "id": "uuid",
                        "text": "Option 2",
                        "metadata": {},
                    }],
                "metadata": {}
            }}]
        res = requests.post('http://127.0.0.1:5000/execute/123', json=data)
        self.assertEqual(res.status_code, 200)
