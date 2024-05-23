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


question1 = Question("Quelle est la capitale de la France ?", ["Paris", "Londres", "Berlin", "Rome"], 1, "C'est une ville très romantique.")
question2 = Question("Quel est l'organe principal du système respiratoire ?", ["Cerveau", "Reins", "Poumons", "Foie"], 3, "C'est l'organe qui vous permet de respirer.")
question3 = Question("Combien de continents y a-t-il sur Terre ?", ["5", "6", "7", "8"], 3, "Il y en a un situé en haut du globe, un autre en bas, et quelques-uns entre les deux.")

quiz = Quiz([question1, question2, question3])

print("Bienvenue au QCM !\n")
quiz.run_quiz()
