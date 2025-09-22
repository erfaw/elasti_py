from tkinter import *
import subprocess as sb; sb.call('cls', shell=True)
window_size = (
    300,
    150
)
font_inf = ("Calibri", 14, "bold")
# make windows
window = Tk()
window.minsize(
    width= window_size[0],
    height= window_size[1]
)
window.maxsize(
    width= window_size[0],
    height= window_size[1]
)
window.title("Mile to Km Converter")
window.config(
    padx=30,
    pady=25,
    # background='black'
)

def calculate_click():
    global km_value
    mile_value = float(input_mile.get())
    km_value = mile_value*1.609
    label_3.config(
        text=f"{km_value:.2f}"
    )
    

# make entry for (1,1)
input_mile = Entry(
    font=font_inf,
    justify="center",
    width= 10
    )
input_mile.grid(row=0, column=1)

# make label
label_1 = Label(
    text="Miles",
    font=font_inf
)
label_1.grid(row=0, column=2)

# make label
label_2 = Label(
    text="is equal to",
    font=font_inf,
    # background='black',
)
label_2.grid(row=1, column=0)

# make label for showing calculation result
km_value = 0
label_3 = Label(
    text=f"{km_value:.2f}",
    font=font_inf
)
label_3.grid(row=1, column=1)

#make Km label
label_4 = Label(
    text="Km",
    font=font_inf
)
label_4.grid(row=1, column=2)

#make button 'calculate' below all of them
cal_button = Button(text="Calculate", font=font_inf, command=calculate_click)
cal_button.grid(row=2, column=1)


window.mainloop()