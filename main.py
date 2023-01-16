from turtle import Turtle,Screen
from snake import Snake
from food import Food
import time
from score import Score

screen=Screen()
screen.setup(width=1000,height=700)
screen.bgcolor("black")
screen.tracer(2)

snake=Snake()
food= Food()
scoreboard=Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
gameison=True

while gameison:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #detection of food collision
    if snake.head.distance(food)<15 :
        food.refresh()
        scoreboard.addscore()
        snake.extend()

    #detect collision with wall
    if snake.head.xcor()>480 or snake.head.xcor() < -480 or snake.head.ycor() <-350 or snake.head.ycor()>350:
        gameison=False
        scoreboard.gameover()
    #detect hitting tail
    for segments in snake.segments:
        if segments==snake.head:
            continue
        elif snake.head.distance(segments)<10:
            gameison=False
            scoreboard.gameover()


gameison=False
screen.exitonclick()