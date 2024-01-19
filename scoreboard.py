from turtle import Turtle
#Instead of harcoding fonts in the code, constants are used.
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

# New superclass scoreboard, inherits from Turtle. Score starts at 0, white color, text is shown at
# center top. The 'turtle' is hidden, and not drawing lines
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # to make sure the scores are not being written on top of each other,
    # the old score needs to be removed
    '''
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
'''

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # When the snake hits a wall, game over function is used
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER MAN, GAME OVER", align=ALIGNMENT, font=FONT)

    # method to keep score, when snake collides with food, the score needs to increase by 1
    def increase_score(self):
        self.score += 1
        #self.clear()
        self.update_scoreboard()
