# Easy version ravesh khodam
import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def main():  # for main program

    print("Welcome to the PyPassword Generator! / salam be PyPassword khosh amadid :)!")
    nr_letters = int(input("How many letters would you like in your password?"))
    nr_symbols = int(input("How many symbols would you like in your password?"))
    nr_numbers = int(input("How many numbers would you like in your password?"))

    # bayad be sorat random be tedadi ke gofte shode char bezarim to javab.

    end_pass = []
    for x in range(nr_letters):
        end_pass.append(random.choice(letters))
    for x in range(nr_symbols):
        end_pass.append(random.choice(symbols))
    for x in range(nr_numbers):
        end_pass.append(random.choice(numbers))

    end_pass_string = ' '
    for x in end_pass:
        end_pass_string += x

    print(end_pass)
    print(end_pass_string)

main()
