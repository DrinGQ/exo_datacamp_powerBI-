class Question:
    def __init__(self, prompt, options, correct_answer, hint):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer
        self.hint = hint
        self.hints_remaining = 2

    def display_question(self):
        print(self.prompt)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

    def display_hint(self):
        if self.hints_remaining > 0:
            print("Indice:", self.hint)
            self.hints_remaining -= 1
        else:
            print("Vous avez utilisé tous vos indices pour cette question.")

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for question in self.questions:
            question.display_question()
            user_answer = input("Votre réponse (entrez le numéro correspondant ou 'hint' pour obtenir un indice) : ")
            if user_answer.lower() == 'hint':
                question.display_hint()
                user_answer = input("Votre réponse (entrez le numéro correspondant) : ")
            if question.check_answer(int(user_answer)):
                print("Correct !\n")
                self.score += 1
            else:
                print("Incorrect.\n")
        print(f"Votre score final est de {self.score}/{len(self.questions)}.")


question1 = Question("Which is not a reason for cleaning data?", ["Often times there are processing errors that cause extra characters and blank values.", "Datasets can be very large and you don't always need all of the data for your report.", "When creating a report, you need to rearrange and resize the visualizations so everything is readable.", ], 3, "Datasets rarely arrive in the exact form you need for your analysis. This is where cleaning data comes in.")

quiz = Quiz([question1])

print("Bienvenue au QCM de Power BI !\n")
quiz.run_quiz()
