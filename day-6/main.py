"""
    KAREL THE ROBOT INSTRUCTION CODE
"""

src_link = f"https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json"

# DESCRIPTION: KAREL the ROBOT STARTS ACTION IN RANDOM POSITION IN MAZE, GOAL IS TAKING ROBO TO FINISH

"""
INITIAL FUNCTIONS:
    turn_left() - robot turns left
    at_goal() - checks is robot in the finish or not
    wall_on_right() - check is there a wall on right side
    front_is_clear() - checks is the front of robot clear or not
    move() - robot does one step
"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    elif front_is_clear():
        move()
    else:
        turn_right() 
        move()