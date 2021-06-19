from turtle import Turtle, write
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("highscore.txt") as file:
            score=int(file.read())
            self.highscore=score
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.write(f"score:{self.score}  High score: {self.highscore}",move=False,align="center",font=("Arial",24,"normal"))
    def incscore(self):
        self.score+=1 
        self.updatescoreboard()
    def updatescoreboard(self):    
        self.clear()  
        self.write(f"score:{self.score}   High score: {self.highscore}",move=False,align="center",font=("Arial",24,"normal"))
    def reset(self):
        if self.score>self.highscore:
            with open("highscore.txt",mode="w") as file:
                file.write(f"{self.score}")
                self.highscore=self.score
        self.score=0    
        self.updatescoreboard()     
    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER.",align="center",font=("Arial",24,"normal"))

         
