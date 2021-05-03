from turtle import Turtle
import time
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP,DOWN,LEFT,RIGHT=90,270,180,0
class Snake:
    def __init__(self):
        self.snake_part=[]
        self.create_snake()
        self.head=self.snake_part[0]
        self.move()
    def  create_snake(self):
        for i in STARTING_POSITION:
            self.inc_size(i)
    def inc_size(self,position):
            new_part=Turtle(shape="square")
            new_part.penup()
            new_part.color("white")
            new_part.goto(position)
            self.snake_part.append(new_part)  
    def extend(self):
        self.inc_size(self.snake_part[-1].position())        
    def move(self):
            for segnum in range(len(self.snake_part)-1,0,-1):
                newx=self.snake_part[segnum-1].xcor()
                newy=self.snake_part[segnum-1].ycor()
                self.snake_part[segnum].goto(newx,newy)
            self.head.forward(MOVE_DISTANCE) 
    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)            
    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)    
    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)        