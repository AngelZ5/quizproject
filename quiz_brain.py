#question number
#question list
#Methor next question

class QuizBrain:
    def __init__(self, q_List):
        self.question_number = 0
        self.question_list = q_List
    def new_question(self):
        for question in self.question_list:
            self.question_number = self.question_number + 1
            input(question, q-)
