import subprocess as sp; sp.call('cls',shell=True)
from tkinter import *
import requests
# URL = 'https://zenquotes.io/api/random'
# URL = 'https://api.kanye.rest/' #this is main but filtered in iran network so...
# URL = 'https://random-quotes-freeapi.vercel.app/api/random'
URL = 'https://dummyjson.com/quotes/random'
def get_quote():
    response = requests.get(URL)
    response.raise_for_status()
    curren_quote = response.json()['quote']
    response.close()
    canvas.itemconfig(
        quote_text,
        text= curren_quote
        )



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="./Day033-erf/Kanye_Quotes/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="./Day033-erf/Kanye_Quotes/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()