from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import subprocess

#3 flavour of drinks:
latte = MenuItem(name= 'latte', water= 200, milk= 150, coffee= 24, cost= 2.5) #1

espresso = MenuItem(name='espresso', water=50, milk=0, coffee=18, cost=1.5) #2

capppuccino = MenuItem(name='capppuccino', water=250, milk=100, coffee=24, cost=3.0) #3

my_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

def get_cls():
    subprocess.call('cls', shell=True)

while True:
    get_cls()
    user_choice = input (
        f"What would you like? ({my_menu.get_items()}) : "
    )
    if user_choice.lower() == 'report':
        coffee_machine.report()
        money_machine.report()
        input('press any to continue...')
        continue
    elif user_choice.lower() == 'off' :
        print("shuting down...")
        break
    order = my_menu.find_drink(user_choice)
    if order and coffee_machine.is_resource_sufficient(order):
            is_paid = money_machine.make_payment(order.cost)
            if is_paid:
                coffee_machine.make_coffee(order)
                input('press any to continue...')

    else: input("please try again...")
            

