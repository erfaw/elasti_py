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

def print_report():
    """print the current report for resources"""
    unit = ''
    for x in resources:
        if x == 'water' or x == 'milk':
            unit = 'ml'
        elif x == 'coffee':
            unit = 'g'
        elif x == 'money': 
            unit = '$'
        print(f"{x.title()}: {resources[x]}{unit}")

def is_possible_to_make(order):
    """Return boolian value,check kardan resource mored niaz 'order' va resource haye feli i ke darim. agar beshe TRUE agar nashe FALSE"""
    needs = MENU[order]["ingredients"]
    for need in needs: # inja iterate miknim dakhel niaz haye 'order' harkodom ke bargharar nabod false hame hm bargharar  bashan ke True
        if resources[need] < needs[need]:
            return False
    return True
    
def is_enough_money(order, paid_money):
    """Return a boolian value, agar pooli ke ba coin ha vared shde baraye price order kafee bashe >> True, dar gheyr in sorat False"""
    if MENU[order]['cost'] > paid_money:
        return False    
    else: 
        return True

def update_resources(order):
    """nesbat be order anjam shde mavared masrafi ro az 'resources' kam mikne va money i ke bedast omade ezafe mikne."""
    used_resources = MENU[order]["ingredients"]
    #chizaye masraf shde:
    for r in used_resources:
        resources[r] -= used_resources[r]
    # poole ezafe shde
    resources["money"] += MENU[order]["cost"]
    

subprocess.call('cls', shell=True) # clear console

while True:
    user_choice = input(
        "What would you like? (espresso/latte/cappuccino): "
    )

    if user_choice in MENU:
        if not is_possible_to_make(user_choice):
            input ("Sorry, machine is out of resources!!!")
        else:
            print('please insert coins.')
            quarters = int(input('How many quarters?: '))
            dimes = int(input('How many dimes?: '))
            nickles = int(input('How many nickles?: '))
            pennies = int(input('How many pennies?: '))
            all_money = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies # inja pool be vahed dollar tabdil mishe. chera ke cost order ha hm be dollare, arzesh har type i az coin ha hm baghaleshon zarb shde ke be dollar tabdil beshan
            if not is_enough_money(user_choice, all_money):
                input ("Sorry, these coins aren't enough...")
            else: # inja hame shart ha check shdn o tamome. 
                in_change = all_money - MENU[user_choice.lower()]["cost"] # change is money which left from your paid money
                update_resources(user_choice)
                print(f"Here is ${in_change:.2f} in change")
                print(f"here is your {user_choice}, Enjoy! :) ")
    elif user_choice.lower() == 'report' :
        print_report()
    else: input(
        'your choice isnt in menu'
    )


# DONE 1. check kardan inke aya user_choice ba resource haye feli ke darim ghable anjame ya na. 
# DONE 2. check kardan inke aya pooli ke sekke i vared shde kafie ya na
# TODO 3. coffee ro drst mikne dastgah , bayad be mizan chizi ke drst karde az resource ha kam beshe
# TODO 4. vaghti sefaresh tamom shd, amade sefaresh badi beshe. 
# TODO 5. agar resource ha be hadi nist ke hichkodom az taste haro drst kne benevise ke nadarim . (plus)



