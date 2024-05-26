from QuizEngine4Trivia import QuizEngine
import html
import os
from Quiz.data import logo


class Quiz:
    quiz_engine: QuizEngine

    def __init__(self):
        self.quiz_engine = QuizEngine()

    def run(self):
        msg = ""
        while self.quiz_engine.still_has_questions():
            self.logo()
            if msg:
                print(f"{msg}\n")
            print(f"Your score: {self.quiz_engine.score}\n\n")
            current = self.quiz_engine.next_question()
            print(f"{html.unescape(current.question)} \n\n")

            count = 0
            for possible_answer in current.possible_answers:
                print(f"{count}: {html.unescape(possible_answer)}")
                count += 1

            user_answer = int(input("Answer .:"))
            if 0 <= user_answer <= count:
                if self.quiz_engine.check_answer(current.possible_answers[user_answer]):
                    msg = "You are right"
                else:
                    msg = "You are wrong"
        print(f"{msg}\n")
        print("There are no more question.\n")
        print(f"Your final score: {self.quiz_engine.score}\n\n")
        input(f"press [enter] to exit")

    def logo(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo.ASCII)


if __name__ == "__main__":
    app = Quiz()
    app.run()
