from tkinter import *
import subprocess as sp; sp.call('cls', shell=True)
from CONSTANTS_variable import *
from interface import *
from time_manager import TimeManager

window = PomodoroWindow()
timer = TimeManager()

def reset_but_clicked():
    window.is_reset_clicked = True

def update_timer():
    elapsed = timer.elapsed(timer.start)
    formated = timer.format_time(elapsed)
    window._tomato()
    if window.is_reset_clicked:
        window._raw_time_str()
        window.is_reset_clicked = False
    else:
        window.update_time_str(formated)
        window.after(1000, update_timer)

def start_timer():
    timer.start = timer.current()
    update_timer()

window.make_start_but(start_timer)
window.make_reset_but(reset_but_clicked)

window.mainloop()