THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        """make a Tkinter UI for the Quizzler app."""
        self.window = Tk()

        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.window.config(
            bg= THEME_COLOR,
            padx=20,
            pady=20
        )
        self.score_label()
        self.question_canvas()
        self.true_btn()
        self.false_btn()

        self.window.mainloop()

    def score_label(self):
        self.label_score = Label(
            text= 'Score:',
            bg= THEME_COLOR,
            fg= 'white',
            font= ("Arial", 16, "bold")
        )
        self.label_score.grid(row=0, column=1)

    def question_canvas(self):
        self.canvas_question = Canvas(width=300, height= 250)
        self.canvas_question.create_text(
            150,125,
            # text='something to ask',
            text=self.quiz.next_question(),
            font= ("Arial", 20, "italic"),
            fill= THEME_COLOR,
            width= 290
            )
        self.canvas_question.grid(row=1, column=0, columnspan=2, pady=50)

    def empty_label(self,):
        self.label_empty = Label(text='', bg= THEME_COLOR)
        self.label_empty.grid(row=2, column=0, columnspan=2)

    def true_btn(self):
        self.true_img = PhotoImage(file="./Day034-erf/Quizzler/images/true.png")
        self.btn_true = Button(
            image= self.true_img,
            highlightthickness= 0,
            
            )
        
        self.btn_true.grid(row=3, column=0)
    def false_btn(self):
        self.false_img = PhotoImage(file="./Day034-erf/Quizzler/images/false.png")
        self.btn_false = Button(
            image= self.false_img,
            highlightthickness= 0,
            )
        
        self.btn_false.grid(row=3, column=1)