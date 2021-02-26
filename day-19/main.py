import turtle as t
import random as rd

# screen
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle is gonna win the race: ")


# functions
def start_position(turtle, color, x, y):
    turtle.shape("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)


# turtle colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# turtles list
turtles = []

# top turtle position and according to it other turtles will be placed
for_y = 180

for color in colors:
    turtle = t.Turtle()
    for_y -= 50
    start_position(turtle, color, -240, for_y)
    turtles.append(turtle)


# racing
is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        distance = rd.randint(1, 10)
        turtle.forward(distance)

        if turtle.xcor() >= 222.5:
            winner_turtle = turtle.color()[0]
            if user_bet == winner_turtle:
                print(f"You won! Your {user_bet}-turtle won the race!")
            else:
                print(f"You lose! Race was won by {winner_turtle}-turtle!")
            is_race_on = False


screen.exitonclick()
