"""
    COFFEE MACHINE PROJECT
"""

from data import resources, MENU

coffee_machine = True
print("""Welcome! You just turned on this coffee machine!
Core commands:
    report
    espresso
    latte
    cappuccino
    off
""")

while coffee_machine:
    command = input("What would you like to drink(Espresso - $1.50 | Latte - $2.50 | Cappuccino - $3.00)? ").lower()
    coffee_cost = 0
    change = 0
    resource_enough = True

    # Reporting
    if command == 'report':
        for key in resources:
            value = resources[key]
            print(f"{key}: {value}")

    # Coffee ordering
    if command == 'espresso' or command == 'latte' or command == 'cappuccino':
        coffee_type = MENU[command]['ingredients']

        # Resource sufficiency
        for key in resources:
            # is-enough-resources
            if resources[key] > coffee_type[key]:
                resources[key] -= coffee_type[key]
                print(f"Enough {key}")
                # resource_enough = True
            else:
                print(f'Not enough {key} resource')
                fill = input("Do you want to fill resources(yes/no)? ")
                if fill == 'yes':
                    resources = {
                        "water": 300,
                        "milk": 200,
                        "coffee": 100,
                    }
                    print("Resources are full: water - 300ml, milk - 200ml, coffee - 100g")
                else:
                    resource_enough = False
                    coffee_machine = False
                    print("Coffee machine should be turned off! Fill the resources and then turn on!")

        if resource_enough:
            # Payment
            quarter = int(input("Put the quarter ($0.25) coin: "))
            dime = int(input("Put the dime ($0.10) coin: "))
            nickel = int(input("Put the nickel ($0.05) coin: "))
            penny = int(input("Put the penny ($0.01) coin: "))

            inserted_money = 0.25 * quarter + dime * 0.1 + nickel * 0.05 + penny * 0.01
            print(f"Total inserted money: ${inserted_money}")

            # Transaction success
            # Making coffee
            coffee_cost = MENU[command]['cost']
            if inserted_money > coffee_cost:
                change = round(inserted_money - coffee_cost, 2)
                print(f"Transaction success! ${change} for change! And enjoy your {command}")
            else:
                print("Inserted money is not enough, choose other coffee or insert extra money")

    # Turn off the machine
    if command == 'off':
        coffee_machine = False


