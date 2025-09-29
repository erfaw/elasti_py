from tkinter import *
import subprocess as sp; sp.call('cls', shell=True)
from CONSTANTS_variable import *
from interface import *
from time_manager import TimeManager
from plyer import notification

window = PomodoroWindow()
timer = TimeManager()
def send_notification(message):
    """Send a notification to the user."""
    notification.notify(
        title="Pomodoro App",
        message=message,
        timeout=3  # Duration in seconds
        # timeout=30  # Duration in seconds
    )

def reset_but_clicked():
    window.is_reset_clicked = True
    window.layer_1.itemconfig(
        window.time_str_id,
        text = "00:00",
    )
    window.pomodoro_round = 0
    window.label_tick.config(
        text= window.pomodoro_round * check_mark_char
    )
    window.label_tick.grid(row=4, column=1)
    window.is_reset_clicked = False
    window.after_cancel(after_id)
        
def count_down(count):
    global after_id
    window.layer_1.itemconfig(
        window.time_str_id,
        text = timer.format_time(count),
    )
    if count > 0 :
        after_id = window.after(1000, count_down, count - 1)
    elif count == 0 and not window.is_break_time:
        # send_notification("You must take a short break! (5min)")
        print("You must take a short break! (5min)")
        window.pomodoro_round += 1
        window.is_break_time = True
        window.label_tick.config(text=check_mark_char * window.pomodoro_round)
        window.label_tick.grid(row=4, column=1) 
        window.after_cancel(after_id)
        count_down(20)
        # return True
    elif count == 0 and window.is_break_time:
        # send_notification("Your Break is DONE, get back to work!")
        print("Your Break is DONE, get back to work!")
        window.is_break_time = False
        window.after_cancel(after_id)
        # return True


# after_update_timer = None
# after_update_timer_5 = None
def start_timer():
    count_down(10) 




window.make_start_but(start_timer)
window.make_reset_but(reset_but_clicked)

window.mainloop()



#TODO: loop baraye najam shodanesh ta 4 bar
#TODO: add kardane 30min break ba notification
#TODO: add kardane title task be ebtedaye barname
#TODO: assign kardane 'golden-pomodoro' baraye anjam shdne yek doreye pomodoro be sorate kamel va porsidane mojadad baraye title task 