# old import : from turtle import Screen, Turtle
# new import, 'Turtle' is no longer used in main.py, and can be deleted
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# to solve the 'caterpillar' effect tracer is disabled
screen.tracer(0)

# new snake object is created from the Snake class, when this is created 'create_snake' is called and the
# segments/squares are being created/drawn
snake = Snake()
# as above, a food object is created
food = Food()
# Scoreboard object is created from the scoreboard class
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Building the snake, it will consist of 3 20x20pixel boxes. The turtle shape will be set to "square" and color white
# one way to do it:
'''
segment_1 = Turtle("square").color("white")

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.goto(-20, 0)

segment_3 = Turtle("square")
segment_3.color("white")
segment_3.goto(-40,0)
'''


# for snake movement I create an empty list, this list will be used in the position function,
# data will be added via append, segments is moved to snake class
# segments = []

# while loop created, for movement, as long as there is 'seg' in the segment list
# variable game_is_on set on True
game_is_on = True
while game_is_on:
    # as the screen tracer alone, only results in a black screen, screen.update is called after the for
    # loop has been run, to show the new squares. it is outside the forloop so the 3 squares have moved
    # before the screen is updated. Hence, no caterpillar motion
    screen.update()
    # Time.sleep, give the game time to update before the for loop runs again
    time.sleep(0.1)
    # for loop only used for test no movement left/right, as long as there is data in the segment list,
    # move 20px forward
    # for seg in segments:
    #    seg.forward(20)
    snake.move()

    # Detect collision with food, .distance from turtle is used to determine the snakes head
    # from the food.
    # I also need to increase the score when the snake collides with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        #scoreboard object called, and tells the score to increase
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
         game_is_on = False
         scoreboard.game_over()
         #scoreboard.reset()
         #snake.reset()

    # Detect collision with tail.
    # if head collides with any segment in the tail
        # Trigger game_over
    # But I also need to make sure it doesn't get triggered at the beginning of the game

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    '''
    # A simpler version for detecting collision, slicing is used:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
'''



screen.exitonclick()
