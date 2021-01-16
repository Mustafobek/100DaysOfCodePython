"""
    BUILDING A TIP CALCULATOR
"""

print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $"))
people_quantity = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tup would you like to give? "))

with_tip = total_bill * (1 + percentage/100) / people_quantity

print(f"Each person should pay {round(with_tip, 2)}")