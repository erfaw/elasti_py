from art import logo
import random
from clear_sc import clear_screen

def main():
    clear_screen()
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
    attemps = 0
    difficulty = input("choose a difficulty. Type 'easy' or 'hard' : ").lower()
    chosen_number = random.randint(1,100)

    if difficulty == 'easy' :
        attemps = 10
    else :
        attemps = 5

    print(f"you have {attemps} attemps remaining to guess the number.")

    is_game_over = False
    while not is_game_over and attemps >= 1 :
        guess = int(input("Make a guess: "))
        if guess == chosen_number :
            print(f"your guess right, the number is {chosen_number}\n !! WIN !!")
            is_game_over = True
        elif guess > chosen_number and attemps >= 1 :
            attemps -= 1
            print("Too high...")
        elif guess < chosen_number and attemps >= 1:
            attemps -= 1
            print("Too low...")

        if attemps != 0 and is_game_over == False :
            print(
            f"You have {attemps} attemps remaining to guess the number."
            )
        elif is_game_over == True:
            break
        else: 
            print(f"!!!GAME OVER!!!\nthe number was: {chosen_number}")
    
    
while True:
    main()
    if input(
        "retry? (y/n)"
    ).lower() != 'y' :
        print("goodbye!")
        break 
