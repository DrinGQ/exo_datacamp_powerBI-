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


question1 = Question(
"""Working with hierarchies.

You don't always want to look at all the available data in your Power BI visualizations. 

Depending on the business question you are trying to answer, you may want to drill down to look at additional relevant details. 

Drilling down accomplishes this by using hierarchies. But how much do you know about hierarchies?

Which statement about hierarchies is true?

""", 
["A hierarchy is a new column type.", "A hierarchy enables the ability to show different levels of data without having to create new visuals.", "A hierarchy is a specific drill-down visual you can use in Power BI.", "A hierarchy is an add-on to the data view."], 2, "An example of an hierarchy could be: year-quarter-month-day.")

quiz = Quiz([question1])

print("Bienvenue au QCM !\n")
quiz.run_quiz()
