# Hard version ravesh khodam
import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letters = ['a', 'A','b', 'B','c', 'C','d', 'D','e', 'E','f', 'F','g', 'G','h', 'H','i', 'I','j', 'J','k', 'K','l', 'L','m', 'M','n', 'N','o', 'O','p','P',
           'q', 'Q','r', 'R','s', 'S','t', 'T','u', 'U','v', 'V','w', 'W','x', 'X','y', 'Y','z','Z']


def main():

    print("Welcome to the PyPassword Generator! / salam be PyPassword khosh amadid :)!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like in your password?\n"))
    nr_numbers = int(input("How many numbers would you like in your password?\n"))

    # har char 3 ta halat dre , letter/symbol/number aval bayad random in entekhab beshe. badesh mirim soragh inke az hmon masalan letter ye random entekhab knim bezarim sare jaash. 

    # positions = [letters, symbols, numbers]
    # password = ' '
    # chosen_list = random.choice(positions)
    # nr_let = nr_letters, nr_num = nr_numbers, nr_sym = nr_symbols
    # def randomization(chosen_list):
    #     #check kardan adad
    #     if nr_let <= 0: 
    #         break
    #     p = random.choice(chosen_list)
    #     password += p
    #     # kam kardan adad 
    #     if chosen_list == letters:
    #         nr_let -= 1
    #     elif chosen_list == symbols:
    #         nr_sym -= 1
    #     else:
    #         nr_num -= 1
    # randomization(chosen_list)

    #ya inke mitonim hmon meghdar ghabli ke gereftim ro berizimesh beham va az random estefade knim.
    end_pass = []
    for x in range(nr_letters):
        end_pass.append(random.choice(letters))
    for x in range(nr_symbols):
        end_pass.append(random.choice(symbols))
    for x in range(nr_numbers):
        end_pass.append(random.choice(numbers))

    harder_pass = ''
    for x in range(len(end_pass)):
        choice = random.choice(end_pass)
        harder_pass += choice
        end_pass.remove(choice)
        # if x == ' ':
        #     break
    print(f"your password will be:\n\n{harder_pass}\n\n")


while True:
    main()
    if input("restart?(y/n)\n").lower() != 'y':
        print("Good Bye!")
        break        

