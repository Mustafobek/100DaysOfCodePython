"""
    CAESAR CIPHER
"""

from art import logo
from my_functions import caeser


print(logo)

# UX

wish = True
while wish:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt: \n")
    text = input(f"Type your message to {direction}: \n")
    shift = int(input("Type the shift number: \n"))
    caeser(text=text, shift=shift % 26, direction=direction)

    wish = input('Would you like to go again? (yes/no): \n')
    
    # Bye message
    if wish == 'no':
        wish = False
        print("Goodbye")
