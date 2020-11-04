from typing import Optional
import json


class Choice:
    def __init__(self, id, text, metadata):
        self.id = id
        self.text = text
        self.metadata = metadata

    def __repr__(self):
        return json.dumps({"choice_id": self.id,
                           "choice_text": self.text,
                           "choice_metadata": self.metadata}, indent=4)

    @classmethod
    def from_json(cls, json):
        return cls(json["id"], json["text"], json["metadata"])

    def to_json(self):
        return {"id": self.id,
                "text": self.text,
                "metadata": self.metadata
                }


class Choices:
    def __init__(self, choices=[]):
        self.choices = choices

    def add_choice(self, choice: Choice):
        self.choices.append(choice)

    def __repr__(self):
        return str(self.choices)

    def __len__(self):
        return len(self.choices)

    def __getitem__(self, index) -> Choice:
        return self.choices[index]

    @classmethod
    def from_json(cls, availble_choices):
        choices = cls()
        for choice in availble_choices:
            choices.add_choice(Choice.from_json(choice))

        return choices

    def to_json(self):
        return [choice.to_json() for choice in self.choices]


class Question:
    def __init__(self, id, text, choices):
        self.id = id
        self.text = text
        self.choices = choices

    def __repr__(self):
        return json.dumps({"question_id": self.id,
                           "question": self.text,
                            "choices": self.choices.to_json()}, indent=4)

    @classmethod
    def from_json(cls, json):
        choices = Choices.from_json(json["question"]["Choices"])
        return cls(json["question"]["id"], json["question"]["text"], choices)


class Questions:
    def __init__(self, questions=[]):
        self.questions = questions

    def add_question(self, question):
        self.questions.append(question)

    def __len__(self):
        return len(self.questions)

    def __repr__(self):
        return str(self.questions)

    def __getitem__(self, index) -> Question:
        return self.questions[index]

    def create(self):
        #TODO: Connect to DB and create the records using self.to_json
        print(self.to_json())

    def update(self):
        #TODO: Connect to DB and update the records using self.to_json
        print(self.to_json())

    def delete(self):
        #TODO: Connect to DB and delete the records using self.to_json
        print(self.to_json())

    @property
    def are_valid(self):
        #TODO: make the validity check here but for now return True by default
        return True

    @classmethod
    def from_json(cls, questions):
        q = cls()
        q.json = questions
        for question in questions:
            q.add_question(Question.from_json(question))
        return q

    def to_json(self):
        return self.json