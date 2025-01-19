from data import question_data
from question_model import Question

question_bank = [] # its a list contains objects of questions 

for each_dict in question_data: #make and append question objects to 'question_bank' list.
    question_bank.append(
        Question(
            each_dict['text'] ,
            each_dict['answer']
        )
    )


