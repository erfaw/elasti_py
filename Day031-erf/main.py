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

def click_right_btn():
    #when user clicl on 'right_btn' that word must deleted from cards.data to dont showup again 

    #here we must delete whats on 'cards.show_card' from db
    cards.delete_record(cards.show_card)

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

def click_wrong_btn():
    # when user press 'wrong_btn' we havent to do anything 
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

window.right_btn.config(command=click_right_btn)
window.wrong_btn.config(command=click_wrong_btn)

window.mainloop()