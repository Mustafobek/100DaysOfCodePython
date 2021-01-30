"""
    THE NUMBER GUESSING GAME
"""

from random import randint

def check(guessed_number, attemp):
    while attemp > 0:
        user_guess = int(input("What is your guess: "))
        if user_guess > guessed_number:
            attemp -= 1
            print(f"Your guess is too high, {attemp} chances left")
        elif user_guess < guessed_number:
            attemp -= 1
            print(f"Your guess is too low, {attemp} chances left")
        elif user_guess == guessed_number:
            attemp = -1
            print(f"You win! Guessed number was {guessed_number}")

    if attemp == 0:
        print(f"You lose! Guessed number was {guessed_number}")

print(
    """
Welcome to the Number Guessing Game!
Im' thinking of a number between 1 and 100. 
"""
)

level = input("Choose a difficulty. Type 'easy' or 'hard': ")
guessed_number = randint(1, 100)
attemp = 0

# Easy level with 10 attemps
if level == "easy":
    print("You have 10 chances, let's go!")
    attemp = 10
    check(guessed_number=guessed_number, attemp=attemp)
    
# Hard level with 5 attemps
elif level == "hard":
    print("You have 5 chances, let's go!")
    attemp = 5
    check(guessed_number=guessed_number, attemp=attemp)

else:
    print("Invalid level! Try again!")