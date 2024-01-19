from turtle import Turtle
# another way is using a for loop and tuples, starting positions are the same coordinates
# old tuple was in lower case, now it is being used as a constant, Uppercase letters
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # def xxx is methods created in the class
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # The for loop runs through the starting_positions list/tuple
        # and creates a segment for each set of coordinates in the list/tuple
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        # new snake square
        new_segment = Turtle("square")
        # square color
        new_segment.color("white")
        # Stop drawing lines
        new_segment.penup()
        # each segment gets a new set of coordinates
        new_segment.goto(position)
        # segments list for movement data
        self.segments.append(new_segment)


    def reset(self):
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # add a new segment to the snake after food collision
        self.add_segment(self.segments[-1].position())


    def move(self):
        # for loop for movement, start with the last input in the segments list.
        # use len() to take the length of the list, -1
        # to get the last input
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # we want the seg num to goto the second to last segments position
            # x and y coordinates are being saved in new_x and new_y variables
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # the variables tell the segments.goto where to go next
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
