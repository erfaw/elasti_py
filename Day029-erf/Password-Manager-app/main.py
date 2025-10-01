from tkinter import *
import subprocess as sp; sp.call('cls', shell= True)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(
    padx= 55,
    pady= 55,
    bg= "#454545"
)
window.resizable(False, False)
FONTI = ('Calibri', 12, 'normal')

canvas = Canvas(
    width = 200,
    height = 200,
    bg= "#454545",
    highlightthickness=0
)
bg_img = PhotoImage(file='./Day029-erf/Password-Manager-app/logo.png')

canvas.create_image(
     80, # middle of bg_img x
     100, # middle of bg_img y
    image= bg_img,
)
canvas.grid(row=0, column=1)

website_text = Label(
    text= 'Website: ',
    justify= 'right',
    bg= "#454545",
    fg= 'white',
    font=FONTI
)
website_text.grid(row=1, column=0)

website_entry = Entry(width= 42, justify='left', font=FONTI)
website_entry.grid(row=1, column=1, columnspan= 2, pady=2)
website_entry.focus()

email_username_text = Label(
    text= 'Email/Username: ',
    justify= 'right',
    bg= "#454545",
    fg= 'white',
    font=FONTI    
)
email_username_text.grid(row=2, column= 0)

email_username_entry = Entry(width= 42, justify='left', font=FONTI)
email_username_entry.grid(row=2, column= 1, columnspan= 2, pady=2)
email_username_entry.insert(0, 'erfawn.h@gmail.com')

password_text = Label(
    text='Password :',
    justify= 'right',
    bg= "#454545",
    fg= 'white',
    font=FONTI   
    )
password_text.grid(row=3, column=0)
password_entry = Entry(width=21+11, justify='left', bg="#D4483B", font=FONTI)
password_entry.grid(row=3, column= 1, padx=0, pady=2)
generate_btn = Button(text='Generate', justify='left', highlightthickness= 0, bg= "#5c85d6", font=FONTI)
generate_btn.grid(row=3, column=2, padx=0, pady=2)

add_btn = Button(text='Add', width= 41, justify='left', bg= "#5c85d6", font=FONTI,)
add_btn.grid(row=4, column=1, columnspan=2, pady=2)

window.mainloop()