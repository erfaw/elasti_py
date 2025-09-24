from tkinter import *
import time
import subprocess as sp; sp.call('cls', shell=True)
from CONSTANTS_variable import *

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global start_time
    start_time= time.time() #current moment
    update_timer()

def update_timer():
    global reset_but_click
    elapsed = int(time.time() - start_time)
    formated = time.strftime("%M:%S", time.gmtime(elapsed))
    layer_1.create_image(
    102,
    114,
    image=tomato_png
    )
    if reset_but_click:
        layer_1.create_text(
        102,128,
        text="00:00",
        font=(FONT_NAME, 22, "bold"),
        fill="white"
        )
        layer_1.grid(row=1,column=1)
        reset_but_click= False
    else:
        layer_1.create_text(
            102,128,
            text=formated,
            font=(FONT_NAME, 22, "bold"),
            fill="white"
        )
        layer_1.grid(row=1, column=1)
        window.after(1000, update_timer)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('-Pomodoro App-')
window.config(
    padx=100,
    pady=50,
    bg=YELLOW
    )

#make a label for Timer
label_1 = Label(
    text= 'Timer',
    font= (FONT_NAME, 36, "bold"),
    bg= YELLOW,
    foreground=GREEN
    )
label_1.grid(row=0,column=1)

#build canvas for pic and timer
layer_1 = Canvas(
    width=202,
    height=226,
    bg=YELLOW,
    highlightthickness=0
    )
tomato_png = PhotoImage(file="./Day028-erf/pomodoro-app/tomato.png")
layer_1.create_image(
    102,
    114,
    image=tomato_png
    )
layer_1.create_text(
    102,128,
    text="00:00",
    font=(FONT_NAME, 22, "bold"),
    fill="white"
    )
layer_1.grid(row=1,column=1)

#make 2 button 'Start' and 'Reset'
start_but = Button(
    text='Start',
    bg='white',
    borderwidth=1,
    font=("Arial", 8,"bold"),
    command=start_timer
    )
start_but.grid(row=2,column=0)

reset_but_click= False
def reset_but_clicked():
    global reset_but_click
    reset_but_click = True

reset_but = Button(
    text='Reset',
    bg='white',
    borderwidth=1,
    font=("Arial", 8,"bold"),
    command=reset_but_clicked,
    )
reset_but.grid(row=2,column=2)
check_mark_char = '✅'
#make label for tick of each period
label_for_space = Label(text='', bg=YELLOW,font=(FONT_NAME, 10))
label_for_space.grid(row=3, column=1)
label_tick = Label(
    text= check_mark_char,
    bg= YELLOW,
    fg= GREEN,
    font=(FONT_NAME, 20)
    )
label_tick.grid(row=4, column=1)

window.mainloop()