from orm import Model


class Question(Model):
    question = str
    choices = str
    answer = str

    def __str__(self):
        return 'Question: {}, Choices: {}, Answer: {}'.format(self.question, self.choices, self.answer)

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

class User(Model):
    name = str
    score = int

    def __str__(self):
        return 'Username: {}, Quiz Score: {}'.format(self.name, self.score)

    def __init__(self, name, score):
        self.name = name
        self.score = score
