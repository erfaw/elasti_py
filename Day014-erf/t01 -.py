import art, random
from clear_sc import clear_screen
from follower_data import data 
score = 0

def decide_info():
    '''print infos from A and B to choose at specific situation'''
    print(f"Compare A:\n\t<< {A["name"]}, {A["job"]}, from {A["from"]}. >>{art.vs_logo}Against B:\n\t<< {B["name"]}, {B["job"]}, from {B["from"]}. >>")


def calculate_higher(A, B):
    """returns higher one as a dictionary"""
    if A["follower"] > B["follower"]:
        return A
    else:
        return B
    

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

# ask user to decide more follower
decide_info()

# fill user_pick based on user opinion
user_pick = ''
if input(
    "Who has more followers? Type 'A' or 'B':  "
).lower() == 'a' :
    user_pick = A
else:
    user_pick = B

higher_one = calculate_higher(A, B)
print(higher_one)