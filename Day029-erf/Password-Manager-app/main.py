# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
import subprocess as sp; sp.call('cls', shell= True)
root = Tk()

canvas = Canvas(
    width = 200,
    height = 200, 
)
bg_img = PhotoImage(file='./Day029-erf/Password-Manager-app/logo.png')

canvas.create_image(
     100,
     100,
    image= bg_img,
)
canvas.pack()

root.mainloop()