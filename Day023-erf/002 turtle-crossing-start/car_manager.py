from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.make_car()

    def make_car(self):
        new_car = Turtle()
        new_car.shape('square')
        new_car.shapesize(stretch_len=2 , stretch_wid=1)
        new_car.color(random.choice(COLORS))
