class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        """return a boolian , True >> there is more question to ask, False >> the quiz ran out of questions."""
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number].text
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question} (true/false): "
        )
        self.check_answer(user_answer, self.question_list[self.question_number].answer)

    def check_answer(self, user_answer, right_answer):
        if user_answer.lower() == right_answer.lower():
            print("You got it right.")
        else:
            print("That's wrong")
        print(f"right answer was {right_answer}")
