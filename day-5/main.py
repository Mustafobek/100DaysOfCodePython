"""
    PASSWORD GENERATOR
"""


import random



# Welcoming message
print("Welcome to password generator program!")

# Setting Basic Datastore

number_list = []
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol_list = []


# digits
 
for i in range(0, 10):
    number_list.append(str(i))


# upper and lower letters

for l in range(len(letter_list)):
    letter_list.append(letter_list[l].upper())


# symbols 

symbol_list = [
    '!', '@', '#',
    '$', '%', '^',
    '&', '*', '(',
    ')', '_', '+',
    '-', '=', '~'
    ] 




# Password configuration INPUTS
letters_in_password = int(input("How many LETTERS would you like in your password? "))
symbol_in_password = int(input("How many SYMBOLS would you like in your password? "))
number_in_password = int(input("How many NUMBERS would you like in your password? "))



# EASY LEVEL - there is an order letters, then numbers, then symbols 

easy_password = ""

for i in range(0, letters_in_password): 
    easy_password += letter_list[random.randint(0, len(letter_list) - 1)]

for j in range(0, number_in_password):
    easy_password += number_list[random.randint(0, len(number_list) - 1)]

for k in range(0, symbol_in_password):
    easy_password += symbol_list[random.randint(0, len(symbol_list) - 1)]


print(easy_password)



# HARD LEVEL - random values with given params

hard_password = ""
password_list = []

for i in range(0, letters_in_password): 
    password_list.append(letter_list[random.randint(0, len(letter_list) - 1)])

for j in range(0, number_in_password):
    password_list.append(number_list[random.randint(0, len(number_list) - 1)])

for k in range(0, symbol_in_password):
    password_list.append(symbol_list[random.randint(0, len(symbol_list) - 1)])

random.shuffle(password_list)               # password_list = random.shuffle(password_list)

for element in password_list:
    hard_password += element

print(hard_password)