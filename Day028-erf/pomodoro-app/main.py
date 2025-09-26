from tkinter import *
import subprocess as sp; sp.call('cls', shell=True)
from CONSTANTS_variable import *
from interface import *
from time_manager import TimeManager
from plyer import notification
import time

window = PomodoroWindow()
timer = TimeManager()
def send_notification(message):
    """Send a notification to the user."""
    notification.notify(
        title="Pomodoro App Notification",
        message=message,
        timeout=30  # Duration in seconds
    )

def reset_but_clicked():
    window.is_reset_clicked = True

def update_timer():
    target_duration_s = 10 # 25 minute
    # target_duration_s = 25*60 # 25 minute
    break_time_s = 10 # 5 minute
    # break_time_s = 5*60 # 5 minute
    elapsed = timer.elapsed(timer.start)
    formated = timer.format_time(elapsed)
    window._tomato()

    if window.is_reset_clicked:
        window._raw_time_str()
        window.pomodoro_round = 0
        window.label_tick.config(fg= YELLOW) #for remove it from display
        window.is_reset_clicked = False
    else:
        if elapsed > target_duration_s:
            window.pomodoro_round += 1
            send_notification("You must take a short break! (5min)")
            window._tomato()
            window.layer_1.create_text(
                102,128,
                text="ON BREAK!!! (5min)\nbe Sharp for Notification",
                fill="White",
                font=(FONT_NAME, 25, "bold")
            )
            time.sleep(break_time_s)
            send_notification("Your Break is DONE, get back to work")
            timer.start= timer.current() 
        window.update_time_str(formated)
        window.label_for_ticks()
        window.after(1000, update_timer)


def start_timer():
    timer.start = timer.current()
    update_timer()

window.make_start_but(start_timer)
window.make_reset_but(reset_but_clicked)

window.mainloop()