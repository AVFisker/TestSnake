from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # Food shape set to circle
        self.shape("circle")
        # penup to remove lines
        self.penup()
        # shapesize is by default 20px, the food is going to be 10px
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # color of the food
        self.color("blue")
        # speed is fastest, so I don't have to see animations
        self.speed("fastest")
        # refresh method called
        self.refresh()

    def refresh(self):
        # random module is used to generate food random in the screen area,
        # not to close to the wall, hence the -20 px.
        # refresh in a new location, when touched by snake
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

