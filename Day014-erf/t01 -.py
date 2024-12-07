import art, random
from clear_sc import clear_screen
from follower_data import data 


# showing logo and introduction
clear_screen()
print(art.game_logo)
print("Welcome to Higher Lower game...")

# pick A and B from data randomly
A_random_number = random.randint(0, len(data))
B_random_number = random.randint(0, len(data))
#build A and B based on random numbers
A = data[A_random_number]
B = data[B_random_number]

print(A)
print(B)




