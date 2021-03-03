import turtle as t
import random as rd


class Food(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = rd.randint(-280, 280)
        rand_y = rd.randint(-280, 280)
        self.goto(rand_x, rand_y)
