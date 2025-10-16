class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question: str = None
        self.user_answer: str

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self) -> bool:
        correct_answer = self.current_question.answer
        if self.user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

