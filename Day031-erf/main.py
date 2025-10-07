from interface import FlashyWindow
from card_manager import CardManager
import subprocess as sp; sp.call('cls', shell= True)
#DONE: make UI
window = FlashyWindow()
cards = CardManager()

def push_right_btn():
    cards.show_card = cards.random_choice()
    window.canvas.itemconfig(
        window.title_str,
        text = 'English'
    )
    window.canvas.itemconfig(
        window.word_str,
        text = cards.show_card['English'].title()
    )

window.right_btn.config(command=push_right_btn)
window.wrong_btn.config(command=push_right_btn)


window.mainloop()