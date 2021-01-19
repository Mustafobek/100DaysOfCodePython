"""
    ROCK - PAPER - SCISSORS GAME with Computer
"""

import random

print("""What do you choose? Type 
0 for ROCK, 
1 for PAPER or 
2 for SCISSORS""")

user = int(input('Your choice: '))
pc = random.randint(0, 2)

# DRAW CASES
if (user == pc):
    print('Draw!!!')

# USER WIN CASES
elif (user == 1 and pc == 0) or (user == 2 and pc == 1) or (user == 0 and pc == 2):
    print(f'user {user} : {pc} computer')
    print('You win! Computer loses!')

# PC WIN CASES
elif (user == 0 and pc == 1) or (user == 1 and pc == 2) or (user == 2 and pc == 0):
    print(f'user {user} : {pc} computer')
    print('You lose! Computer wins!')