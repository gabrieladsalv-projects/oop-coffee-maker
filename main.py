from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

# Create objects
menu_info = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

print(logo)
print('-----------------------------------------')
print("      Welcome to the Coffee Maker!")
print('-----------------------------------------')
print()

# ask user 

while True:
    which = input(f"Do you want a report, turn-off or a {menu_info.get_items()} ? ").lower()
    print()

    # Print report
    if which == 'report':
        machine.report()
        money.report()

    # Turn off the machine

    elif which == 'turn-off':
        break

    else:
        # find drink
        drink = menu_info.find_drink(which)

        # see if resources are enough
        if machine.is_resource_sufficient(drink):

        # see if payment is sufficient
            if money.make_payment(drink.cost):
                print()

        # make coffee
                machine.make_coffee(drink)

