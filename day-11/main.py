"""
    BLACKJACK GAME or 21
"""

from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
yes_or_no = input("Do you wanna try BlackJack game? (y/n): ")
game = ""

if yes_or_no == "y":
    game = True
else:
    game = False

while game:
    # Game start
    user_cards = [choice(cards), choice(cards)]
    computer_cards = [choice(cards), choice(cards)]

    dealer_score = sum(computer_cards)
    if dealer_score < 17:
        computer_cards.append(choice(cards))

    print(f"Your cards are {user_cards}")
    print(f"Computer's first card is {computer_cards[0]}")

    # Continue or making summarize
    wanna_take_another_card = input("Type 'hit' to get another card, type 'stand' to pass: ")

    # user takes another card
    while wanna_take_another_card == 'hit':
        user_cards.append(choice(cards))
        print(f"Your cards are {user_cards}")
        print(f"Computer's first card is {computer_cards[0]}")
        wanna_take_another_card = input("Type 'hit' to get another card, type 'stand' to pass: ")

    # user stands
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    print(f"Your cards are {user_cards}")
    print(f"Computer cards are {computer_cards}")

    # Draws
    # if more 
    if user_score > 21 or computer_score > 21:
        # specific situations
        if user_score > 21 and computer_score > 21:
            print("DRAW! Try again!")
        elif user_score > 21 and computer_score < 21:
            print("COMPUTER (DEALER) WINS!")
        elif computer_score > 21 or user_score < 21:
            print("YOU WIN!")
    # general sitautions
    elif user_score == computer_score:
        print("DRAW! Try again!")
    # Computer wins
    elif user_score < computer_score:
        print("COMPUTER (DEALER) WINS!")
    # User wins
    elif user_score > computer_score:
        print("YOU WIN!")

    # Stop or restart game
    yes_or_no = input("Do you wanna try BlackJack game? (y/n): ")

    if yes_or_no == "y":
        game = True
    else:
        game = False