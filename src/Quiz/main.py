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
        user_answer: int = -1
        while self.quiz_engine.still_has_questions():
            user_input_loop = True
            current = self.quiz_engine.next_question()
            while user_input_loop:
                count = 0
                self.logo()
                if msg:
                    print(f"{msg}\n")
                print(f"Your score: {self.quiz_engine.score}\n")
                print(f"{html.unescape(current.category)}")
                print(f"{html.unescape(current.question)} \n")

                for possible_answer in current.possible_answers:
                    print(f"{count}: {html.unescape(possible_answer)}")
                    count += 1
                count -= 1  # roll back last increment
                try:
                    user_answer = int(input("Answer .:"))
                except ValueError:
                    msg = "Inputted wrong value"
                else:
                    if not 0 <= int(user_answer) <= count:
                        user_answer = -1
                        msg = "Inputted wrong value"
                    else:
                        user_input_loop = False
            if 0 <= user_answer <= count:
                if self.quiz_engine.check_answer(current.possible_answers[user_answer]):
                    msg = "You are right"
                else:
                    msg = "You are wrong"

        print(f"{msg}\n")
        print("There are no more question.\n")
        print(f"Your final score: {self.quiz_engine.score}\n\n")
        input(f"press [enter] to see result\n")
        results = self.quiz_engine.get_result()
        count = 0
        for result in results:
            count += 1
            if result[0]:
                print(f"Q.{count} Your answer was correct")
            else:
                print(f"Q.{count} Your answer was wrong")
                print(f"Your answer.: {result[1]}")
                print(f"Correct answer.:{result[1]}\n")

        input(f"press [enter] to exit")

    @staticmethod
    def logo():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo.ASCII)


if __name__ == "__main__":
    app = Quiz()
    app.run()
