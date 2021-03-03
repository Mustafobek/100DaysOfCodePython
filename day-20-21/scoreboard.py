import turtle as t

ALIGN = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def up(self):
        self.score += 1
        # print(self.score)
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game over", move=False, align=ALIGN, font=FONT)
