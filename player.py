from turtle import Turtle, Screen

STARTING_POSITION = (0, -380)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def player_move(self):
        self.forward(MOVE_DISTANCE)


