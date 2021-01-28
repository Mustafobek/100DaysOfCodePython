"""
    CALCULATOR APP
"""

from functions import add, sub, multiply, divide
from art import logo


# Declarations
operations = {"+": add, "-": sub, "*": multiply, "/": divide}
calculation = False

print(logo)

number1 = int(input("First number: "))
# shows all possible operations in our program
for key in operations:
    print(key)
operation = input("What operation you want to do: ")
number2 = int(input("Second number: "))

# First process - first operation
answer = operations[operation](number1, number2)
print(f"{number1} {operation} {number2} = {answer}")

# if user wants to continue the process
to_coninue = input(
    f"Type 'y' to continue with calculating {answer}, type 'n' to start program again or stop() to stop the program: "
)

if to_coninue == "y":
    calculation = True
elif to_coninue == "n":
    print(answer)
    answer = int(input("First number: "))
    calculation = True
elif to_coninue == "stop()":
    calculation = False
    print(answer)
else:
    print(f"Invalid command, your last answer was {answer}")
    calculation = False

while calculation:
    operation = input("What next operation you want to do: ")
    number = int(input("What is the next number: "))
    answer = operations[operation](answer, number)
    to_coninue = input(
        f"Type 'y' to continue with calculating {answer}, type 'n' to start program again or stop() to stop the program: "
    )

    if to_coninue == "y":
        calculation = True
    elif to_coninue == "n":
        print(answer)
        answer = int(input("First number: "))
        calculation = True
    elif to_coninue == "stop()":
        calculation = False
        print(answer)
    else:
        print(f"Invalid command, your last answer was {answer}")
        calculation = False
