import tkinter
window = tkinter.Tk()
window.title("My First GUI horaaaaaaaaaaaaay")
window.minsize(800,600)

def sum_args(*args):
    container = 0
    for i in args:
        container+=i
    return container

my_label = tkinter.Label(text=f"this is the sum(*args) result\n {sum_args(67,99,133,33, 65, 98 ,88)}", font=("Claibri", 30, "bold"))
my_label.pack()

window.mainloop()