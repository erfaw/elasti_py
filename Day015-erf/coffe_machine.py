import subprocess

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50, # unit: mg
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
    """return 1 if resources is enough to make 'order' , otherwise if isnt enough, return a list of out of resources."""
    needs = MENU[order]["ingredients"]
    empty_resources = []
    for need in needs: # inja iterate miknim dakhel niaz haye 'order' harkodom ke bargharar nabod false hame hm bargharar  bashan ke True
        if resources[need] < needs[need]:
            empty_resources.append(need)

    if len(empty_resources) == 0 :
        return 1
    else: 
        return empty_resources
    
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

# Starting main program
while True:
    user_choice = input(
        "What would you like? (espresso/latte/cappuccino): "
    )

    if user_choice in MENU:
        possibility = is_possible_to_make(user_choice)
        if possibility != 1 : # so we have a List
            input(f"Sorry, machine is out of {' and '.join(possibility)}!!!")
        else:
            print('please insert coins.')
            quarters = int(input('How many quarters?: '))
            dimes = int(input('How many dimes?: '))
            nickles = int(input('How many nickles?: '))
            pennies = int(input('How many pennies?: '))
            all_money = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies # inja pool be vahed dollar tabdil mishe. chera ke cost order ha hm be dollare, arzesh har type i az coin ha hm baghaleshon zarb shde ke be dollar tabdil beshan
            if not is_enough_money(user_choice, all_money):
                input ("Sorry, these coins aren't enough..., money refunded")
            else: # inja hame shart ha check shdn o tamome. 
                in_change = all_money - MENU[user_choice.lower()]["cost"] # change is money which left from your paid money
                update_resources(user_choice)
                print(f"Here is ${in_change:.2f} in change")
                print(f"here is your ☕{user_choice}☕, Enjoy! :) ")
    elif user_choice.lower() == 'report' :
        print_report()
    elif user_choice.lower() == 'off' : # this will shut down the machine or actually close the program.
        print("shuting down...")
        break
    else: input(
        'your choice isnt in menu'
    )


# DONE 1. check kardan inke aya user_choice ba resource haye feli ke darim ghable anjame ya na. 
# DONE 2. check kardan inke aya pooli ke sekke i vared shde kafie ya na
# DONE 3. coffee ro drst mikne dastgah , bayad be mizan chizi ke drst karde az resource ha kam beshe
# DONE 4. vaghti sefaresh tamom shd, amade sefaresh badi beshe. 
# DONE 5. agar resource ha be hadi nist ke hichkodom az taste haro drst kne benevise ke nadarim . (plus)



