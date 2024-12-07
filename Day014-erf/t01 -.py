import art, random
from clear_sc import clear_screen
from follower_data import data 

def decide_info():
    '''print infos from A and B to choose at specific situation'''
    print(f"Compare A:\n\t<< {A["name"]}, {A["job"]}, from {A["from"]}. >>{art.vs_logo}Against B:\n\t<< {B["name"]}, {B["job"]}, from {B["from"]}. >>")

# showing logo and introduction
clear_screen()
print(art.game_logo)
print("Welcome to Higher Lower game...")

# pick A and B from data randomly
A_random_number = random.randint(0, len(data))
B_random_number = random.randint(0, len(data))
#build A and B based on random numbers
A = data[A_random_number] # a dict
B = data[B_random_number] # a dict

decide_info()
