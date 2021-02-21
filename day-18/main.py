"""
    Painting project with Turtle module - Hirst Spot Painting
"""

import turtle as t
import random as rd
from colors import colors

# turtlization
tim = t.Turtle()
t.colormode(255)

# Taking starting point out of the screen centre to (-125, -125)
tim.penup()
tim.goto(-100, -100)
tim.pendown()


# Hirst spot paints
def paint(space, x):
    """Draws spot painting with given params - space: space between dots; x - side of square you wanna make"""
    # going vertically upper
    for __ in range(x):
        # each line horizontal
        for _ in range(x):
            tim.dot(10, rd.choice(colors))
            tim.penup()
            tim.forward(space)
            tim.pendown()
        tim.penup()
        tim.backward(space * x)

        # taking turtle upper
        tim.left(90)
        tim.forward(space)
        tim.right(90)


# Just hides turtle
tim.hideturtle()

paint(25, 10)

# Screen
screen = t.Screen()
screen.exitonclick()
