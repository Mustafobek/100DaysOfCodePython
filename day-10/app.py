"""
    CALCULATOR APP with RECURSION
"""

from functions import add, sub, multiply, divide
from art import logo

# Declarations
operations = {"+": add, "-": sub, "*": multiply, "/": divide}
print(logo)


def calculator():
    number1 = float(input("First number: "))
    # shows all possible operations in our program
    for key in operations:
        print(key)

    calculation = True

    while calculation:
        operation = input("What operation you want to do: ")
        number2 = float(input("Second number: "))

        # First process - first operation
        answer = operations[operation](number1, number2)
        print(f"{number1} {operation} {number2} = {answer}")

        to_coninue = input(
            f"Type 'y' to continue with calculating {answer}, type 'n' to start program again or stop() to stop the program: "
        )

        if to_coninue == "y":
            number1 = answer
        elif to_coninue == "n":
            print(answer)
            calculator()
        elif to_coninue == "stop()":
            print(answer)
            calculation = False
        else:
            print(f"Invalid command, your last answer was {answer}")
            calculation = False


calculator()