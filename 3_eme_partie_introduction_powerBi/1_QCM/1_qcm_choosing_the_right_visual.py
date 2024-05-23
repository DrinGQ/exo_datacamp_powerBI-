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
    def __init__(self, questions, image_path):
        self.questions = questions
        self.score = 0
        self.image_path = image_path

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
                    self.display_image()
                    break
                else:
                    print("Incorrect. Essayez à nouveau.\n")
        print(f"Votre score final est de {self.score}/{len(self.questions)}.")

    def display_image(self):
        image = Image.open(self.image_path)
        image.show()
        # Pause to allow the image to be viewed
        time.sleep(2)

question1 = Question(
"""Choosing the right visual
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You have just seen a number of visualizations that can be added to Power BI reports. Not every visual is suitable for every situation. It's important to choose the correct one based on what you want to accomplish.

Imagine you are creating a visual that shows nine different regions' sales values in the dataset.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""", 
["Pie chart", "KPI card", "Column chart", "Gauge chart"], 
3,  
"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

"""You could use a pie chart here, but another visualization is better suited. You should only use a pie chart if you want to look at a limited number of categories.

KPIs and gauge charts are used to display actual data compared to budgeted data.

Column charts display more than one data series in vertical columns.

"""
)

image_path = "img/visual_could_be_like.png"

quiz = Quiz([question1], image_path)

print("Bienvenue au QCM Power BI !\n")
quiz.run_quiz()

print("Regardez ce lien hyper important : https://learn.microsoft.com/fr-fr/training/modules/power-bi-effective-reports/?ns-enrollment-type=LearningPath&ns-enrollment-id=learn-bizapps.visual-data-power-bi&wt.mc_id=da100_choosingtherightvisualize_content_wwlgtl_csadai")
