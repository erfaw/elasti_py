from interface import FlashyWindow
from card_manager import CardManager
import subprocess as sp; sp.call('cls', shell= True)
#DONE: make UI
window = FlashyWindow()
cards = CardManager()

def show_flip():
    # change bg color done
    window.canvas.itemconfig(
        window.card_bg,
        image= window.card_back_img
    )
    # change title_str done
    window.canvas.itemconfig(
        window.title_str,
        text= 'Persian',
        fill= 'white'
    )
    # change word_str to persian 
    window.canvas.itemconfig(
        window.word_str,
        text= cards.show_card['Persian'],
        fill= 'white'
    )

def push_right_btn():
    cards.show_card = cards.random_choice()
    window.canvas.itemconfig(
        window.card_bg,
        image= window.card_front_img
    )
    window.canvas.itemconfig(
        window.title_str,
        text = 'English',
        fill= 'black'
    )
    window.canvas.itemconfig(
        window.word_str,
        text = cards.show_card['English'].title(),
        fill= 'black'
    )
    window.after(3000, show_flip)

window.right_btn.config(command=push_right_btn)
window.wrong_btn.config(command=push_right_btn)


window.mainloop()