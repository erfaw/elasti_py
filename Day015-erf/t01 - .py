import subprocess

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,        
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

subprocess.call('cls', shell=True) # clear console

user_choice = input(
    "What would you like? (espresso/latte/cappuccino): "
)

if user_choice.lower() != 'report' :
    if user_choice in MENU:
        print('please insert coins.')
        quarters = int(input('How many quarters??: '))
        dimes = int(input('How many dimes??: '))
        nickles = int(input('How many nickles??: '))
        pennies = int(input('How many pennies??: '))
        all_money = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
        in_change = all_money - MENU[user_choice.lower()]["cost"]
        print(f"Here is ${in_change:.2f} in change")
    else: input(
        'your choice isnt in menu'
    )
else: #print report
    for x in resources:
        unit = ''
        if x == 'water' or x == 'milk':
            unit = 'ml'
        elif x == 'coffee':
            unit = 'g'
        elif x == 'money': 
            unit = '$'
        print(f"{x.title()}: {resources[x]}{unit}")



