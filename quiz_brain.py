
class QuizBrain:
    def __init__(self, q_List):
#question number
        self.question_number = 0
#question list
        self.question_list = q_List
#Method next question
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q. {self.question_number}: {current_question.text} (True/False)")
