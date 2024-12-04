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
    """just showing in game scores, whole user and first computer"""
    print(
        f"\tYour cards: {picked_cards["player"]}, current score: {sum(picked_cards['player'])}"
    )
    print(
        f"\tComputer's first card: {picked_cards['computer'][0]}\n"
    )


def show_end_scors():
    """print end game scores for ending game"""
    print(
        f"\tYour cards: {picked_cards["player"]}, current score: {sum(picked_cards['player'])}"
    )
    print(
        f"\tComputer's cards: {picked_cards['computer']}, current score: {sum(picked_cards['computer'])}\n"
    )

    
def pick_1_card_both():
    """operate adding one card value to each player and computer list"""
    computer_card = random.choice(main_cards)
    player_card = random.choice(main_cards)

    if computer_card == 11 and sum(picked_cards['computer']) + computer_card > 21:
            computer_card = 1
    if player_card == 11 and sum(picked_cards['player']) + computer_card > 21:
            player_card = 1

    picked_cards['computer'].append(computer_card)
    picked_cards['player'].append(random.choice(main_cards))
    

def calculate_winer():
    """check end situation and release the winner (for using this function user hasn't to  want pick a card)"""
    if sum(picked_cards['computer']) < 17 :
        computer_card = random.choice(main_cards)
        if computer_card == 11 and sum(picked_cards['computer']) + computer_card > 21:
            computer_card = 1
        picked_cards['computer'].append(computer_card)

    if sum(picked_cards['player']) > 21 :
        show_end_scors()
        print("you Lose")
        if sum(picked_cards['computer']) <= 21:
            print("pc win") 
        else:
            print("pc lose")
        
    elif sum(picked_cards['player']) == 21:
        show_end_scors()
        if sum(picked_cards['computer']) == 21:
            print("it's a Draw")
        else: 
            print("You Win\npc lose")

    elif sum(picked_cards['player']) < 21:
        show_end_scors()
        if sum(picked_cards['computer']) > 21:
            print("you win\npc lose")
        elif sum(picked_cards['computer']) == 21 :
            print("you lose\npc win")
        #both of them are below 21    
        elif sum(picked_cards['computer']) > sum(picked_cards['player']) :
            print("you lose\npc win")
        elif sum(picked_cards['computer']) < sum(picked_cards['player']) :
            print("you win\npc lose")
    else:
        print("i think there is a problem here")


def reset_values():
    picked_cards['computer'] = []
    picked_cards['player'] = []


def main():
 #actualy start game
    pick_1_card_both()
    pick_1_card_both()
    show_scors()
    
    while True:
        want_pick = input("pick a card? (y/n)")
        if want_pick == 'n' :
            calculate_winer()
            input("press any to continue...")
            break
        
        elif want_pick == 'y' :
            pick_1_card_both()
            show_scors()
            if sum(picked_cards['player']) >= 21:
                calculate_winer()
                input("press any to continue")
                break
            
            else: # player < 21
                continue
                

while True :
    clear_screen() 
    print(logo)
    print("welcome to Black jack\n\n")

    play_or_not = input("play a round?(y/n)").lower()
    if play_or_not == 'n' :
        print("have a nice day, goodbye!")
        break
    elif play_or_not == 'y':
        reset_values()
        main()
    else: 
        print("you chose wrong answer")
