FONT = ("Courier", 24, "normal")
from turtle import Turtle, Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.penup()
        self.setpos(640, 340)
        self.write(f'Your score: {self.score}', align="right", font=FONT)

    def game_over(self):
        self.setpos(0,0)
        self.write(f'Game over', align="right", font=FONT)





