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

# def update_timer():
#     global after_update_timer
#     target_duration_s = 25*60 # 25 minute
#     # target_duration_s = 25*60 # 25 minute
#     # break_time_s = 10 # 5 minute
#     # break_time_s = 5*60 # 5 minute
#     timer.elapsed_s = timer.elapsed(timer.start)
#     timer.formated_str = timer.format_time(timer.elapsed_s)
#     window._tomato()

#     if window.is_reset_clicked:
#         window._raw_time_str()
#         window.pomodoro_round = 0
#         window.label_tick.config(fg= YELLOW) #for remove it from display
#         window.is_reset_clicked = False
#         window.after_cancel(after_update_timer)
#     else:
#         if timer.elapsed_s > target_duration_s:
#             # for achieving target time for one period
#             window.pomodoro_round += 1
#             send_notification("You must take a short break! (5min)")
#             window._tomato()
#             window.label_note_5min.config(fg=RED)
#             window.label_for_ticks()
#             window.after_cancel(after_update_timer)
#             # time.sleep(break_time_s)
#             # send_notification("Your Break is DONE, get back to work")
#             timer.start= timer.current() 
#         else:
#             window.update_time_str(timer.formated_str)
#             window.label_for_ticks()
#             after_update_timer = window.after(1000, update_timer)

# def update_timer_for_5minute():
#     #ّFAILEDTODO: use 'elapsed_reverse' here to count-down timer 
#     global after_update_timer_5
#     target_duration_s = 5*60 # must be 5 minute
#     timer.elapsed_s = timer.elapsed(timer.start)
#     timer.formated_str = timer.format_time(timer.elapsed_s)
#     window._tomato()

#     if window.is_reset_clicked:
#         window._raw_time_str()
#         window.pomodoro_round = 0
#         window.label_tick.config(fg= YELLOW) #for remove it from display
#         window.is_reset_clicked = False
#         window.after_cancel(after_update_timer_5)
#     else:
#         if timer.elapsed_s > target_duration_s:
#             # for achieving target time for one period
#             send_notification("Your Break is DONE, get back to work!")
#             window._tomato()
#             window.after_cancel(after_update_timer_5)
#             window.label_for_ticks()
#             window.label_note_5min.config(fg=YELLOW)
#         else:
#             window.update_time_str(timer.formated_str)
#             window.label_for_ticks()
#             after_update_timer_5 = window.after(1000, update_timer_for_5minute)
        
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
        window.label_for_ticks()
        window.after_cancel(after_id)
        return True
    elif count == 0 and window.is_break_time:
        # send_notification("Your Break is DONE, get back to work!")
        print("Your Break is DONE, get back to work!")
        window.is_break_time = False
        window.after_cancel(after_id)
        return True


# after_update_timer = None
# after_update_timer_5 = None
def start_timer():
    # PREVIOUS WAY OF MINE MIND:
        # timer.start = timer.current()
        # # update_timer()
        # timer.start = timer.current()
        # # update_timer_for_5minute()
    count_down(10) 




window.make_start_but(start_timer)
window.make_reset_but(reset_but_clicked)

window.mainloop()