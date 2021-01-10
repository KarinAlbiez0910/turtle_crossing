import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.player_move)
car_manager = CarManager()
score_board = Scoreboard()



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    if player.ycor() > 380:
        player.setpos(STARTING_POSITION)
        score_board.score = score_board.score + 1
        score_board.update_score()
        car_manager.starting_move_distance = car_manager.starting_move_distance + car_manager.move_increment

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score_board.game_over()
    car_manager.build_car()
    car_manager.move_cars()





screen.exitonclick()







