from tkinter import *
class FlashyWindow(Tk):
    def __init__(self):
        super().__init__()
        self.BACKGROUND_COLOR = "#B1DDC6"
        self.FONTI = ("Ariel", 40, "italic")
        self.card_front_img = PhotoImage(file="./Day031-erf/images/card_front.png")
        self.card_back_img = PhotoImage(file="./Day031-erf/images/card_back.png")
        self.right_img = PhotoImage(file="./Day031-erf/images/right.png")
        self.wrong_img = PhotoImage(file="./Day031-erf/images/wrong.png")
        self.make_root_window()
        self.make_card_canvas()
        self.make_right_btn()
        self.make_wrong_btn()

    def make_root_window(self):
        self.title("Flashy")
        self.config(
            width=800,
            height=526,
            padx=50,
            pady=50,
            bg= self.BACKGROUND_COLOR
            )
        
    def make_card_canvas(self):
        self.canvas = Canvas(width=800, height=526, highlightthickness=0, bg=self.BACKGROUND_COLOR)
        self.canvas.create_image(400, 262, image= self.card_front_img)
        self.canvas.grid(row=0, column=0, columnspan=2)

    def make_right_btn(self):
        self.right_btn = Button()
        self.right_btn.config(
            image= self.right_img,
            highlightthickness=0
        )
        self.right_btn.grid(row=1, column=1)

    def make_wrong_btn(self):
        self.wrong_btn = Button()
        self.wrong_btn.config(
            image= self.wrong_img,
            highlightthickness=0
        )
        self.wrong_btn.grid(row=1, column=0)        

    
