from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game_is_on=True
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)    
snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")

while game_is_on:
    screen.update() 
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.incscore()
        scoreboard.updatescoreboard()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < (-280) or snake.head.ycor() > 280 or snake.head.ycor() < (-280):
        scoreboard.reset()
        snake.reset()
        
    for segments in snake.snake_part:
            if segments== snake.head:
                pass
            elif snake.head.distance(segments)<10:
                scoreboard.reset()
                snake.reset()
                    
screen.exitonclick()
