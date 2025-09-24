from tkinter import *
import time
import subprocess as sp; sp.call('cls', shell=True)
from CONSTANTS_variable import *
from interface import *
tomato_png_file_path = "./Day028-erf/pomodoro-app/tomato.png"

#make UI
window = PomodoroWindow()
reset_but_click= False
def reset_but_clicked():
    global reset_but_click
    reset_but_click = True
def update_timer():
    global reset_but_click
    elapsed = int(time.time() - start_time)
    formated = time.strftime("%M:%S", time.gmtime(elapsed))
    window.layer_1.create_image(
    102,
    114,
    image=window._tomato()
    )
    if reset_but_click:
        window.layer_1.create_text(
        102,128,
        text="00:00",
        font=(FONT_NAME, 22, "bold"),
        fill="white"
        )
        window.layer_1.grid(row=1,column=1)
        reset_but_click= False
    else:
        window.layer_1.create_text(
            102,128,
            text=formated,
            font=(FONT_NAME, 22, "bold"),
            fill="white"
        )
        window.layer_1.grid(row=1, column=1)
        window.after(1000, update_timer)
def start_timer():
    global start_time
    start_time= time.time() #current moment
    update_timer()
window.make_start_but(start_timer)
window.make_reset_but(reset_but_clicked)

window.mainloop()