import random
from orm import Database

from models import Question, User

db = None

class quiz:
    def superuser(self):
        print("enter your choice: 1.Create a question 2.Logout")
        options = int(input())
        while options != 2:
            if options == 1:
                try:
                    ques = input("enter a question: ")
                    choices = input("enter choices: ")
                    ans = input("enter your answer: ")
                    Question.manager(db).save(Question(ques, choices, ans))
                except Exception as error:
                    print('Save Question Error: ' + error + ', please try again')
            else:
                print("choose valid option")
            print("enter your choice: 1.Create a question 2.Logout")
            options = int(input())
        print(list(Question.manager(db).all()))
        print("you are logged out")

    def user(self):
        all_questions: [Question] = list(Question.manager(db).all())
        if all_questions:
            print('''\n==========RULES==========\n
            1. Quiz consists of 10 random questions. To answer, you must press A/B/C/D (case-insensitive).
            Your final score will be given at the end.\n
            2. Each question consists of 1 point. There's no negative point for wrong answers.\n''')

            username = input("Enter your name:")
            questions = {}
            score = 0
            for i in range(0, 3):
                q: Question = random.choice(all_questions)
                while questions.get(q.question):
                    q = random.choice(all_questions)
                print(q.question)
                print(q.choices)
                questions[q.question] = 1
                answer = input().lower()
                if answer == q.answer:
                    print("Correct")
                    score += 1
                else:
                    print("Wrong")
            print(User.manager(db).save(User(username, score)))
        else:
            print("No questions in database")


if __name__ == "__main__":
    db = Database('db.sqlite')
    choice = int(input("ENTER YOUR CHOICE: "))
    if choice == 1:
        obj = quiz()
        obj.superuser()
    elif choice == 2:
        obj = quiz()
        obj.user()
    else:
        print("enter a valid choice")
    db.commit()
    db.close()
