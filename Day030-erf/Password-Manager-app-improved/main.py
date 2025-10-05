from tkinter import *
import subprocess as sp; sp.call('cls', shell= True)
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_', '-', '=', '{', '}']
letters = ['a', 'A','b', 'B','c', 'C','d', 'D','e', 'E','f', 'F','g', 'G','h', 'H','i', 'I','j', 'J','k', 'K','l', 'L','m', 'M','n', 'N','o', 'O','p','P','q', 'Q','r', 'R','s', 'S','t', 'T','u', 'U','v', 'V','w', 'W','x', 'X','y', 'Y','z','Z']
def generate_pass():
    end_pass = []
    end_pass += ([choice(letters) for x in range(randint(2,4))]) # random choice letters
    end_pass += ([choice(symbols) for x in range(randint(2,4))]) # random choice symbols
    end_pass += ([choice(numbers) for x in range(randint(8,10))]) # random choice numbers
    shuffle(end_pass)
    str_end_pass = ''.join(end_pass)
    password_entry.delete(0, END)
    password_entry.insert(0, str_end_pass) # insert to entry password
    pyperclip.copy(str_end_pass) # copy generated password to clipboard

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

def save():
    site = website_entry.get()
    username_email = email_username_entry.get()
    password = password_entry.get()

    if len(site) == 0 or len(username_email) == 0 or len(password) == 0:
        messagebox.showwarning('Oops!', "Please don't leave any fileds empty!", icon='warning')
    elif messagebox.askokcancel(
        'Is it OK to save?',
        f'These are the details entered:\n\tSite: {site}\n\tPass: {password}\n\tEmail: {username_email}',
        icon='question',
        ):

        new_data = {
            site: {
                "email": username_email,
                "password": password
            }
        }

        pyperclip.copy(password)
    # dealnig with exception which json file doesnt exist
        try: 
            f= open('./Day030-erf/Password-Manager-app-improved/data.json', mode='r')
        except FileNotFoundError:
            with open('./Day030-erf/Password-Manager-app-improved/data.json', mode='w') as f:
                json.dump({},f)
        else: 
            pass
        finally: f.close()

        with open('./Day030-erf/Password-Manager-app-improved/data.json', mode='r') as file:
            #dealing with exception which json file is empty and json.load() raise json.decoder.JSONDecodeError for this emptiness
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                data = {}
            data.update(new_data) # ta inja file ro ba json jadid update karim

        with open('./Day030-erf/Password-Manager-app-improved/data.json', mode='w') as file:        
            json.dump(data, file, indent=4)

        # clearing fields after write data on file
        website_entry.delete(0,END)
        password_entry.delete(0,END)
    else: 
        pass

canvas = Canvas(
    width = 200,
    height = 200,
    bg= "#454545",
    highlightthickness=0
)
bg_img = PhotoImage(file='./Day030-erf/Password-Manager-app-improved/logo.png')

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
generate_btn = Button(text='Generate', justify='left', highlightthickness= 0, bg= "#5c85d6", font=FONTI, command=generate_pass)
generate_btn.grid(row=3, column=2, padx=0, pady=2)

add_btn = Button(text='Add', width= 41, justify='left', bg= "#5c85d6", font=FONTI, command= save)
add_btn.grid(row=4, column=1, columnspan=2, pady=2)

window.mainloop()


#done: create function called save()
#done: write to the data inside the entries to a 'data.txt' file when the add button is clicked.
#done: each website, email, and password combination should be on a new line iside the file.
#done: all fields need to be cleared after add button is pressed.

#TODO: add a 'search' button next to the website entry field.
#TODO: adjust the layout and the other widgets as needed to get the desired look.
#TODO: create a function called fin_password() that gets triggered when the 'search' button is pressed.
#TODO: check if the user's text entry matches an item in the 'data.json' file
#TODO:  if yes, show a messagebox with te website's name and password.
#TODO: catch an exception that might occur tring to access the 'data.json' showing a messagebox with the text: 'No Data File Found'
#TODO: if the user's website does not exist inside the 'data.json', show a messagebox that reads "No details for the website exists"

#TODO: check if repeated value, dont added to file and show a popup to user
#TODO: good to be a field at end to log the day of insertation
#TODO: good to be a popup to tell user 'your changes has been saved!' (mitonim image ro begirim va be ye raveshi hamin ro green knim, zamani ke Add-btn zade mishe on ro baraye masalan 3s green knim, bahal mishe)

