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
            while True:
                question.display_question()
                user_answer = input("Votre réponse (entrez le numéro correspondant ou 'hint' pour obtenir un indice) : ")
                if user_answer.lower() == 'hint':
                    question.display_hint()
                elif question.check_answer(int(user_answer)):
                    print("Correct !\n")
                    self.score += 1
                    break
                else:
                    print("Incorrect. Essayez à nouveau.\n")
        print(f"Votre score final est de {self.score}/{len(self.questions)}.")


question1 = Question("""The essentials of Power BI
-------------------------------------------------------------------------
Microsoft Power BI is a Business Intelligence tool. 
But what can it actually do for us?
Possible Answers """, ["Clean and structure any data connected", "Connect to data sources", "Create reports containing visualizations", "Share findings and insights with colleagues", "all the four"], 5, 
"""Think about how Microsoft Power BI organizes data and connects to different data sources.
It also has the ability to create visual reports and allows the sharing of insights.""")

quiz = Quiz([question1])

print("Bienvenue au QCM de PowerBI !\n")
quiz.run_quiz()
