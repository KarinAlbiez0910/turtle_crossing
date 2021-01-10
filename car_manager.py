from turtle import Turtle, Screen
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.starting_move_distance = 5
        self.move_increment = 10

    def build_car(self):
        random_num = random.randint(1,6)
        if random_num == 1:
            car = Turtle()
            car.shape('square')
            self.x_value = 780
            self.random_y = random.randint(-360, 360)
            self.random_color = random.choice(COLORS)
            car.penup()
            car.setpos(self.x_value, self.random_y)
            car.setheading(180)
            car.color(self.random_color)
            car.shapesize(stretch_len=2, stretch_wid=1)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.starting_move_distance)


        screen.update()















