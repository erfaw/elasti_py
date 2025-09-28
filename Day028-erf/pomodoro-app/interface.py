from tkinter import *
from CONSTANTS_variable import *
tomato_png_file_path = "./Day028-erf/pomodoro-app/tomato.png"
check_mark_char = '✅'

class PomodoroWindow(Tk):

    def __init__(self):
        """makes a Tk window for 'Pomodoro-app' and initiate basics for it."""
        super().__init__()
        self.is_reset_clicked = False
        self.pomodoro_round = 0
        self.set_configuration_window()
        self.make_container()
        self.tomato_png  = PhotoImage(file=tomato_png_file_path)
        self._tomato()
        self.make_timer_label()
        self._raw_time_str()
        self.label_for_ticks()
        self.note_for_break()


    def set_configuration_window(self):
        """set title -Pomodoro App- and padding (x=100, y=50) and makes background color to YELLOW (from CONSTANT_variable.py)"""
        self.title('-Pomodoro App-')
        self.config(
            padx=100,
            pady=50,
            bg=YELLOW
        )
        self.resizable(False, False) 

    def make_timer_label(self):
        """makes a 'Timer' string on top of tomato timer, with foreground color GREEN (from CONSTANT_variable.py)"""
        self.label_1 = Label(
        text= 'Timer',
        font= (FONT_NAME, 36, "bold"),
        bg= YELLOW,
        foreground=GREEN
        )
        self.label_1.grid(row=0,column=1)

    def make_container(self):
        """make a Canvas() object with width 202 and height 226 and set background color to YELLOW (from CONSTANT_variable.py) and set highlightthickness=0"""
        self.layer_1 = Canvas(
        width=202,
        height=226,
        bg=YELLOW,
        highlightthickness=0
        )

    def _tomato(self):
        """create_image from tomato.png on a Canvas() object names 'layer_1', (width, height)= (102,114) then grid whole Canvas() object"""
        self.tomato_id = self.layer_1.create_image(
            102,
            114,
            image=self.tomato_png
        )
        self.layer_1.grid(row=1,column=1)
    
    def _raw_time_str(self):
        """set a 00:00 string on tomato without any functionality on Canvas() object"""
        self.time_str_id = self.layer_1.create_text(
            102,128,
            text="00:00",
            font=(FONT_NAME, 22, "bold"),
            fill="white"
            )
        self.layer_1.grid(row=1,column=1)

    def update_time_str(self, formated_time):
        self.layer_1.create_text(
            102,128,
            text=formated_time,
            font=(FONT_NAME, 22, "bold"),
            fill="white"
        )
        self.layer_1.grid(row=1, column=1)

    def make_start_but(self, start_timer):
        """makes start button below tomato and grid it"""
        self.start_but = Button(
            text='Start',
            bg='white',
            borderwidth=1,
            font=("Arial", 8,"bold"),
            highlightthickness= 0,
            command=start_timer
            )
        self.start_but.grid(row=2,column=0)

    def make_reset_but(self, reset_but_clicked):
        """makes start button below tomato and grid it"""
        self.reset_but = Button(
            text='Reset',
            bg='white',
            borderwidth=1,
            font=("Arial", 8,"bold"),
            highlightthickness= 0,
            command=reset_but_clicked,
            )
        self.reset_but.grid(row=2,column=2)

    def label_for_ticks(self):
        """makes a label to make some margin between button and ticks, and make a label to print ticks for each period of Pomodoro Technique"""
        self.label_for_space = Label(text='', bg=YELLOW,font=(FONT_NAME, 10))
        self.label_for_space.grid(row=3, column=1)
        self.label_tick = Label(
            text= check_mark_char * self.pomodoro_round,
            bg= YELLOW,
            fg= GREEN,
            font=(FONT_NAME, 20)
            )
        self.label_tick.grid(row=4, column=1)     

    def note_for_break(self):
        """print a note for 5min break between periods"""
        self.label_note_5min = Label(
            text= "ON BREAK!!!\nbe sharp for Notification",
            bg= YELLOW,
            fg= YELLOW,
            font= (FONT_NAME, 10, "bold")
        )
        self.label_note_5min.grid(row=5,column=1)
