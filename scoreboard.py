from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.write(f"score:{self.score}",move=False,align="center",font=("Arial",24,"normal"))
    def incscore(self):
        self.score+=1 
        self.clear()  
        self.write(f"score:{self.score}",move=False,align="center",font=("Arial",24,"normal"))
    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER.",align="center",font=("Arial",24,"normal"))

         