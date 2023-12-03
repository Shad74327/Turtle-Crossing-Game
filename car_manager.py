import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []

    """Randomly generating cars along the y-axis"""
    def car_generate(self):
        occurrence = random.randint(1, 6)
        if occurrence == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    """Cars moving from right to left"""
    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE)



