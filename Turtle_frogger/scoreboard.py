from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.color("yellow")
        self.update_scoreboard()
        
        
    def level_up(self):
        self.level += 1
        self.update_scoreboard()
            
    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", align="left", font=FONT)
    
class Road(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-300, 280)
        self.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        