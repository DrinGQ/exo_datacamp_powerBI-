from PIL import Image
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


image_path = "img/views_in_powerbi.png"  
image = Image.open(image_path)

image.show()


question1 = Question("""Views in Power BI
-------------------------------------------------------------------------
When opening a new Power BI Desktop file, how many different "views" are available in Power BI Desktop?
one Answers """, ["0", "1", "3"], 3, 
"""When opening a new Power BI Desktop file, by default you will start working in the Report view.
The model view shows the different tables and any relationships between them.
The data view gives more detail about each data table connected to your Power BI Desktop file.""")

quiz = Quiz([question1])

print("Bienvenue au QCM de PowerBI !\n")
quiz.run_quiz()
