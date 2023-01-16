from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"score:{self.score}", align="center")
    def update(self):
        self.write(f"score:{self.score}", align="center" ,font=("Arial", 34, "normal"))
    def addscore(self):
        self.score+=1
        self.clear()
        self.update()
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 34, "normal"))
