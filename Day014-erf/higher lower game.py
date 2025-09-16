import art, random
from clear_sc import clear_screen
from follower_data import data

def main():

    game_data = data
    score = 0
    user_pick = ''


    def calculate_higher(A, B):
        """returns higher one in number of followers as a dictionary"""
        if A["follower"] > B["follower"]:
            return A
        elif A["follower"] < B["follower"]:
            return B
        elif A["follower"] == B["follower"]:
            return user_pick
        


    def decide_info():
        '''print infos from A and B to choose at specific situation, maded for test during development'''
        # print(f"A follower == > {A["follower"]}")
        # print(f"B follower == > {B["follower"]}")
        # print(f"higher is ============= >{calculate_higher(A, B)["name"]}")
        print(f"Compare A:\n\t<< {A["name"]}, {A["job"]}, from {A["from"]}. >>{art.vs_logo}Against B:\n\t<< {B["name"]}, {B["job"]}, from {B["from"]}. >>")


    # showing logo and introduction
    clear_screen()
    print(art.game_logo)
    print("Welcome to Higher Lower game...")


    game_is_over = False

    # pick A and B from game_data randomly for first run
    A_random_number = random.randint(0, len(game_data))
    B_random_number = random.randint(0, len(game_data))
    #build A and B based on random numbers for first run
    A = game_data[A_random_number] # a dict
    del game_data[A_random_number] # delete from game_database after assign as an element in game
    B = game_data[B_random_number] # a dict
    del game_data[A_random_number] # delete from game_database after assign as an element in game


    while not game_is_over:
        if score >= 1:
            clear_screen()
            print(art.game_logo)
            print(f'right, current score: {score}')
        # ask user to decide more follower
        decide_info()

        # fill user_pick based on user opinion
        
        if input(
            "Who has more followers? Type 'A' or 'B':  "
        ).lower() == 'a' :
            user_pick = A
        else:
            user_pick = B

        higher_one = calculate_higher(A, B)

        

        # user choose right or wrong?
        if higher_one == user_pick :
            score += 1
            
        else: # game should be ended
            clear_screen()
            print(art.game_logo)
            print(f'wrong!!!, final score: {score}\n\n')
            game_is_over = True

        # prepare for next round
        if game_is_over == False :
            if higher_one == A :
                if score >= 1:
                    del game_data[B_random_number]
                if score >= 10:
                    print("gz you WIN reached highest score")
                    game_data = data
                    break
                B_random_number = random.randint(0, len(game_data))
                B = game_data[B_random_number] # a dict

            elif higher_one == B :
                if score >= 1:    
                    del game_data[A_random_number]
                if score >= 10:
                    print("gz you WIN reached highest score")
                    game_data = data
                    break
                A = B 
                B_random_number = random.randint(0, len(game_data))
                B = game_data[B_random_number] # a dict

            else:
                input("we have a fucking problem!!!!!!!!!")

while True:
    main()
    if input("retry? (y/n) : ").lower() != 'y':
        print('have a nice day good bye')