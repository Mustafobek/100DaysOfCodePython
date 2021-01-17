"""
    TREASURE ISLAND PROJECT
"""

print("""
    Welcome to Treasure Island.
    Your mission is to find the treasure.
""")

road = input("You're at a cross road. Where do you want to go? \"left\" or \"right\"").lower()

if (road == "left"):
    lake = input("You come to lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across")
    if lake == "swim":
        print("I dont know why but according to Technical requirements GAME OVER")
    elif lake == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        if door == 'red':
            print("You enter a room of fire! GAME OVER")
        elif door == 'yellow':
            print("I dont know why but according to Technical requirements YOU WIN!!!)))")
            # 
        elif door == 'blue':
            print("You enter a room of beast! GAME OVER")
            # 
elif (road == "right"):
    print("I dont know why but according to Technical requirements GAME OVER")