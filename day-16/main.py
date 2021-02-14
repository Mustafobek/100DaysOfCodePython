"""
    COFFEE MACHINE PROJECT with OOP
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

# espresso = MenuItem("espresso", 50, 0, 18, 1.5)
# latte = MenuItem("latte", 200, 150, 24, 2.5)
# cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)


while is_on:
    options = menu.get_items()
    command = input(f"What would you like today? ({options}): ")

    if command == 'off':
        is_on = False

    elif command == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(command)
        enough_resources = coffee_maker.is_resource_sufficient(drink)
        if enough_resources:
            enough_money = money_machine.make_payment(drink.cost)
            if enough_money:
                coffee_maker.make_coffee(drink)

        # here we could simplify code like
        # if enough_resources and enough_money
        # but logically it is wrong, b'coz even if resources was not enough it will ask for insert money
