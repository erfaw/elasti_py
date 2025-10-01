from tkinter import *
import subprocess as sp; sp.call('cls', shell= True)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(
    padx= 20,
    pady= 20,
)

canvas = Canvas(
    width = 200,
    height = 200,
)
bg_img = PhotoImage(file='./Day029-erf/Password-Manager-app/logo.png')

canvas.create_image(
     100, # middle of bg_img x
     100, # middle of bg_img y
    image= bg_img,
)
canvas.pack()

window.mainloop()