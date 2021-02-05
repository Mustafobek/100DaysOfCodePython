"""
    HIGHER or LOWER GAME
"""

from art import logo, vs
from database import data
from random import randint, choice
from function import player

print(logo + "\n")


score = 0
game = True
option_1 = player(choice(data))
option_2 = player(choice(data))

while game:
    # Option 1
    option_1_name = option_1[0]
    option_1_desc = option_1[1]
    option_1_followers = option_1[2]
    option_1_country = option_1[3]
    print(f"Compare A: {option_1_name}, {option_1_desc}, from {option_1_country}")

    print(vs)

    # Option 2
    option_2_name = option_2[0]
    option_2_desc = option_2[1]
    option_2_followers = option_2[2]
    option_2_country = option_2[3]
    print(f"Against B: {option_2_name}, {option_2_desc}, from {option_2_country}")

    # user input
    user_input = input("Who has more followers in instagram? Choose A or B: ").lower()

        
    

    # user wins
    # todo: won option must be fisrt option of next level
    if (option_1_followers > option_2_followers and user_input == "a") or (option_1_followers < option_2_followers and user_input == "b"):
        # Chaining
        if option_1_followers > option_2_followers and user_input == "a":
            option_1 = player(choice(data))    
            option_1_name = option_1[0]
            option_1_desc = option_1[1]
            option_1_followers = option_1[2]
            option_1_country = option_1[3]

        elif option_1_followers < option_2_followers and user_input == "b":
            option_2 = player(choice(data))
            option_2_name = option_2[0]
            option_2_desc = option_2[1]
            option_2_followers = option_2[2]
            option_2_country = option_2[3]
        score += 1
        print(f"Your current score is {score}")

    # user loses
    else:
        print(f"You lose! Your current score is {score}")
        print(
            f"{option_1_name}: {option_1_followers} vs {option_2_name}: {option_2_followers}"
        )
        game = False
