class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        """return a boolian , True >> there is more question to ask, False >> the quiz ran out of questions."""
        self.q_list_len = len(self.question_list)
        if self.question_number >= self.q_list_len:
            return False
        else: 
            return True


    def next_question(self):
        self.user_answer = input(
            f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (true/false): "
        )
        self.question_number += 1
