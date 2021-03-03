import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[i - 1].xcor()
            y_cor = self.segments[i - 1].ycor()
            self.segments[i].goto(x_cor, y_cor)
        self.snake_head.forward(MOVE_DISTANCE)

    def turn_north(self):
        # checking if user tries to turn the snake to back with on move
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def turn_south(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def turn_east(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def turn_west(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def add_segment(self, position):
        snake_segment = t.Turtle(shape="square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        # adds a new segment to the snake
        self.add_segment(self.segments[-1].position())
