from tkinter import *
import subprocess as sb; sb.call('cls', shell=True)

window = Tk()
window.minsize(600, 600)
window.title("shitSHOW :)")

#make a label
my_label = Label(text="its gonna be a lable", font=("Calibri", 25, "bold"))
my_label.pack()

# button functionality: change my_label['text'] when clicked
def button_clicked():
    my_label.config(
        text=f"button clicked! <3"
        )
    my_label2.config(
        text=f"{input1.get()} was our entry"
    )
    
# make a button
my_button = Button(text="Click me Motha Fucka", command=button_clicked, pady=20)
my_button.pack()
my_label2 = Label(text="", font=("Calibri", 15, "bold"))
my_label2.pack()

# using Entry module
input1 = Entry(width=50)
input1.pack()




window.mainloop()