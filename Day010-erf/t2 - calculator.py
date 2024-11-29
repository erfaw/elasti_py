from clear_sc import clear_screen
from art import logo

clear_screen()
print(logo)
def main():
    def add(n1, n2):
        return n1 + n2
    def subtract(n1, n2):
        return n1 - n2
    def multipy(n1, n2):
        return n1 * n2
    def divide(n1, n2):
        return n1 / n2
    operators = {
        "+" : add,
        "-" : subtract,
        "*" : multipy,
        "/" : divide,
    }

    want_continue = 'y'
    number1 = float(input("What's the first number?: "))
    while want_continue == 'y':
        
        operator = input("+\n-\n*\n/\nPick an operation:\t")
        while operator not in operators:
            print("WRONG VALUE!! try again")
            operator = input("Pick an operation:\t")

        number2 = float(input("What's the next number: "))

        result = operators[operator](number1, number2)
        print(
            f"{number1} {operator} {number2} = {result}"
        )
        number1 = result
        want_continue = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:"
        )
    
    # if input(
    #     f"Type 'y' to continue calculating with {}, or type 'n' to start a new calculation:\t"
    # ).lower() == 'y':
    #     operator = input(
    #     "+\n-\n*\n/\nPick an operation:\t"
    #     )




while True:
    main()
    clear_screen()
    if input(
        'retry? (y/n)'
    ).lower() != 'y':
        break