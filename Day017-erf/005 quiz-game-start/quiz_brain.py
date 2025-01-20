class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """return a boolian , True >> there is more question to ask, False >> the quiz ran out of questions."""
        return self.question_number < len(self.question_list)


    def next_question(self):
        """Do things for asking question and triger check answer"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1 # nokte: question_number az 0 shoro mishe (chera ke bayad azash baraye gereftan question az question bank estefade knim, oon hm indexesh az 0 shoro mishe pas bayad 0 bashe) vali baraye inke shomaresh tebgh question ha drst bashe inja +1 mishe (daghighan baad az line ghabli ke question ro gereft va dige niazi behesh nist.)
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (true/false): "
        )
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, right_answer):
        """Check the user answer with right answer and manage score."""
        if user_answer.lower() == right_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong")
        print(f"right answer was {right_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
