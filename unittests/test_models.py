from unittest import TestCase
from BuzzFeedQuiz.models import Choices, Choice, Question, Questions


class TestModels(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_choices(self):
        input_json = [{
            "id": "uuid",
            "text": "Option 1",
            "metadata": {"score": 1}
        },
            {
                "id": "uuid",
                "text": "Option 2",
                "metadata": {"score": 5}
            }]

        choices = Choices.from_json(input_json)
        self.assertEqual(len(input_json), len(choices))
        extra_choice = {
            "id": "uuid",
            "text": "Option 3",
            "metadata": {"score": 15}
        }
        choice = Choice.from_json(extra_choice)
        choices.add_choice(choice)
        self.assertEqual(len(choices), 3)
        self.assertEqual(extra_choice["text"], choices.choices[2].text)

    def test_questions(self):
        questions_json = [{
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

        questions = Questions.from_json(questions_json)
        self.assertEqual(len(questions), 1)
        self.assertEqual(questions[0].choices[1].text, "Option 2")