from data import welcome_message, MENU

print(welcome_message)

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# 0. user command
# 1. check the resources
# 2. payment
# 3. making coffee


def report():
    for item in resources:
        value = resources[item]
        print(f"{item} - {value}gr")


def resource_sufficiency(coffee_type):
    """Checks sufficiency of stoke resources with coffee resource requirement"""
    for item in MENU[coffee_type]["ingredients"]:
        if resources[item] >= MENU[coffee_type]["ingredients"][item]:
            print(f"{item} enough for your coffee")
        else:
            print(f"{item} is NOT enough for your coffee")
            return False
    return True


def resource_use(coffee_type):
    """According to coffee type resources will be used"""
    if resource_sufficiency:
        for item in resources:
            if resources[item] >= MENU[coffee_type]['ingredients'][item]:
                resources[item] -= MENU[coffee_type]['ingredients'][item]
        return True


def inserted_money_amount(coffee_type):
    """Takes coffee type and according to its cost and inserted money decleares change and profit"""
    penny = int(input("How many penny-coins you want to put in? "))
    nickel = int(input("How many nickel-coins you want to put in? "))
    dime = int(input("How many dime-coins you want to put in? "))
    quarter = int(input("How many quarter-coins you want to put in? "))
    total = penny * 0.01 + nickel * 0.05 + dime * 0.1 + quarter * 0.25
    return total


coffee_machine = True
profit = 0

while coffee_machine:
    command = input("""
What kind of coffee you want?
Espresso - $1.50
Latte - $2.50
Cappuccino - $3.00    
    """).lower()

    # reporting resources balance
    if command == 'report':
        report()

    # ordering coffee
    elif command == 'espresso' or command == 'latte' or command == 'cappuccino':
        # checking resources sufficiency for ordered coffee
        if resource_sufficiency(command):
            inserted_money = inserted_money_amount(command)
            coffee_cost = MENU[command]['cost']
            # checking inserted money amount
            if inserted_money > coffee_cost:
                change = round(inserted_money - coffee_cost, 2)
                resource_use(command)
                profit += coffee_cost
                print(f"Total inserted money is ${round(inserted_money, 2)}! Take your change of ${change}")
                print(f"This is your {command}! Enjoy it!")
            else:
                print(f"You inserted only {round(inserted_money, 2)}, but your coffee costs {coffee_cost}")
        else:
            refill = input("There are not enough resources! Do you want to refill them? Refilling cost $1.00. (yes/no)")
            if refill == 'yes':
                profit -= 1
                resources = {
                    "water": 300,
                    "milk": 200,
                    "coffee": 100,
                }

    elif command == 'profit':
        print(f"For now your profit is ${profit}")

    elif command == 'off':
        coffee_machine = False
        print(f"For today coffee machine is off! Today's total profit is ${profit}")