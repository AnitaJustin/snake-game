from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
class Snake:
    def __init__(self):
        self.segments=[]
        self.createsnake()
        self.head=self.segments[0]

    def addsegment(self, position):
        snakei = Turtle(shape="square")
        snakei.penup()
        snakei.color("white")
        snakei.goto(position)
        self.segments.append(snakei)

    def createsnake(self):
        for position in STARTING_POSITIONS:
            self.addsegment(position)

    def extend(self):
        self.addsegment(self.segments[-1].position())


    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segnum - 1].xcor()
            new_y = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() !=90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() !=0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() !=180:
            self.head.setheading(0)