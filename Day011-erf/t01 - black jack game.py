from clear_sc import clear_screen
from art import logo
import random

main_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#            [A , 2, 3, 4, 5, 6, 7, 8, 9, 10, J , Q , K ]  
picked_cards = {
    "player" : [],
    "computer": [],
}


def show_scors():
    print(
        f"\tYour cards: {picked_cards["player"]}, current score: {sum(picked_cards['player'])}"
    )
    print(
        f"\tComputer's first card: {picked_cards['computer'][0]}\n"
    )


def show_end_scors():
    print(
        f"\tYour cards: {picked_cards["player"]}, current score: {sum(picked_cards['player'])}"
    )
    print(
        f"\tComputer's cards: {picked_cards['computer']}, current score: {sum(picked_cards['computer'])}\n"
    )

    
def pick_1_card_both():
    picked_cards['computer'].append(random.choice(main_cards))
    picked_cards['player'].append(random.choice(main_cards))


def pick_card():
    if input('pick a card?! (y/n)').lower() != 'y':
        picked_cards['computer'].append(random.choice(main_cards))
    else:
        pick_1_card_both()


def want_play():
    if input("\n\n do u want to play a round? :) : ").lower() != 'y':
        print("have a nice day")
        return 'n'
    else:
        return 'y'
    

# intrudoction
clear_screen() 
print(logo)
print("welcome to Black jack\n\n")

play_or_not = input("play a round?(y/n)").lower()
if play_or_not != 'y' :
    print("have a nice day, goodbye!")
else:
    picked_cards['computer'].append(random.choice(main_cards))
    picked_cards['computer'].append(random.choice(main_cards))
    picked_cards['player'].append(random.choice(main_cards))
    picked_cards['player'].append(random.choice(main_cards))
    show_scors()

    want_pick = input("pick a card? (y/n)")
    if want_pick != 'y' :
        







pick_card()


if sum(picked_cards['player']) > 21 :
    show_end_scors()
    print("you Lose")
    
elif sum(picked_cards['player']) == 21:
    if sum(picked_cards['computer']) == 21:
        print("it's a Draw")
    else: 
        show_end_scors()
        print("You Win")

elif sum(picked_cards['player']) < 21:
    show_scors()
    pick_card()
    



print(f"\n\n\n{picked_cards}")