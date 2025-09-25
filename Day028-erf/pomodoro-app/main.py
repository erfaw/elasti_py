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
        title="Program Closer Notification",
        message=message,
        timeout=30  # Duration in seconds
    )

def reset_but_clicked():
    window.is_reset_clicked = True

def update_timer(target=(25*60)):
    elapsed = timer.elapsed(timer.start)
    formated = timer.format_time(elapsed)
    window._tomato()
    if window.is_reset_clicked:
        window._raw_time_str()
        window.pomodoro_round = 0
        window.label_tick.config(fg= YELLOW) #for remove it from display
        window.is_reset_clicked = False
    else:
        if elapsed% (10) == 0 and elapsed != 0:
            window.pomodoro_round += 1
            send_notification("You must take a short break! (5min)")
            
            #TODO.we must put here a count-down timer for 5 minute

            
        window.update_time_str(formated)
        window.label_for_ticks()
        window.after(1000, update_timer)


def start_timer():
    timer.start = timer.current()
    update_timer()

window.make_start_but(start_timer)
window.make_reset_but(reset_but_clicked)

window.mainloop()