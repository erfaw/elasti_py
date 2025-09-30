from tkinter import *
import subprocess as sp; sp.call('cls', shell=True)
from CONSTANTS_variable import *
from interface import *

window = PomodoroWindow()

def reset_but_clicked():
    global REPS
    window.layer_1.itemconfig(
        window.time_str_id,
        text = "00:00",
    )
    window.label_tick.config(
        text= 0 * check_mark_char
    )
    window.label_1.config(text="Timer", fg= GREEN)
    window.after_cancel(after_id)
    REPS = 0
    window.label_note_5min.config(fg=YELLOW)

  
def count_down(count):
    global after_id
    window.layer_1.itemconfig(
        window.time_str_id,
        text = window.format_time(count),
    )
    if count > 0 :
        after_id = window.after(1000, count_down, count - 1)
    else:
        if REPS%8 == 0:
            window.notification(
                "Long Break is Done, get back to start another one."
            )
        elif REPS%2 == 0 :
            window.notification(
                "Break is done, get back to work!"
            )
        elif REPS == 7:
            window.notification(
                "Gz! You fully completed one pomodoro round, take a long Break! Cya"
            )
        else:
            window.notification("Time to Break!")
        start_timer()
        window.label_tick.config(text= int(REPS/2) * check_mark_char )

def start_timer():
    global REPS
    REPS += 1 # 7
    if REPS <= 8:
        if REPS % 8 == 0:
            count_down(LONG_BREAK_MIN*60)
            window.label_1.config(text="L-BREAK", fg=RED)
            window.label_note_5min.config(text="On Break!\nbe sharp for notification", fg=RED)
        elif REPS % 2 == 0:
            count_down(SHORT_BREAK_MIN*60)
            window.label_1.config(text="BREAK", fg=PINK)
            window.label_note_5min.config(text="On Break!\nbe sharp for notification", fg=RED)
        else:
            count_down(WORK_MIN*60)
            window.label_1.config(text="WORK", fg=GREEN)
            window.label_note_5min.config(fg=YELLOW)

    else: 
        window.label_note_5min.config(
            text= "This is end of one pomodoro,\nstart another one",
            fg= RED
        )

        





window.make_start_but(start_timer)
window.make_reset_but(reset_but_clicked)

window.mainloop()



#TODO: loop baraye najam shodanesh ta 4 bar
#TODO: add kardane 30min break ba notification
#TODO: add kardane title task be ebtedaye barname
#TODO: assign kardane 'golden-pomodoro' baraye anjam shdne yek doreye pomodoro be sorate kamel va porsidane mojadad baraye title task 