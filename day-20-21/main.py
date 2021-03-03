"""
    SNAKE GAME
"""

import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# screen setup
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game")
screen.tracer(0)

# snake and Food
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# arrow keys listener
screen.listen()

screen.onkey(fun=snake.turn_west, key="Left")
screen.onkey(fun=snake.turn_north, key="Up")
screen.onkey(fun=snake.turn_east, key="Right")
screen.onkey(fun=snake.turn_south, key="Down")

# moving the snake
game_is_on = True

# todo: make difficulty levels => user enters any number from 1 to 10, and according to this it will give a difficulty

# difficulty_level = screen.numinput(title="Difficulty Levels", prompt="Choose level of difficulties from 1 to 10: ")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.snake_head.distance(food) <= 15:
        food.refresh()
        scoreboard.up()
        snake.extend()

    # Detect collision with wall
    if snake.snake_head.xcor() > 280 \
            or snake.snake_head.xcor() < -290 \
            or snake.snake_head.ycor() > 290 \
            or snake.snake_head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.snake_head:
        #     pass
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
