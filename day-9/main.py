"""
    AUCTION PROGRAMM
"""

from art import logo 
from functions import new_player, find_max, users

bidding_condition_controller = True
print(logo)

# first launch and when user wants more and more bids
while bidding_condition_controller:

    name = input("What is your full name?: ")
    bid = int(input("What is your bid?: $"))
    new_player(name, bid)
    controller = input("Are there any other bidders? (yes/no) ")

    if controller == 'yes':
        bidding_condition_controller = True
    else:
        bidding_condition_controller = False
        # Summarizing
        highest_bidder = find_max(users)
        highest_bid_owner = highest_bidder["name"].upper()
        highest_bid_cost = highest_bidder["bid"] 
        print(f"Highest bid in this auction was {highest_bid_cost}, and it belongs to {highest_bid_owner}!!!!!!!!!!")
    

