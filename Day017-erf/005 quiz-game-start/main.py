from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [] # its a list contains objects of questions 

for each_dict in question_data: #make and append question objects to 'question_bank' list.
    question_bank.append(
        Question(
            each_dict['text'] ,
            each_dict['answer']
        )
    )

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")