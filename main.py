from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

CAR_SPEED = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
score = Scoreboard()

"""User input"""
screen.onkey(player.move, "Up")

game_on = True
while game_on:
    time.sleep(CAR_SPEED)
    screen.update()

    car.car_generate()
    car.move_cars()

    """Checking the collision between cars and the player"""
    for cars in car.all_cars:
        if player.distance(cars) < 27:
            score.game_over()
            game_on = False

    """Checking whether the player crossed the finishing line"""
    if player.ycor() > 280:
        score.level_up()
        player.refresh()
        CAR_SPEED *= 0.7

screen.exitonclick()
