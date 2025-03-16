from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.list = []
        self.reuse_list = []

    def make_car(self):
        if self.reuse_list == []:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_len=2 , stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.seth(180)
            new_car.teleport(
                300,
                random.randint(-250, 250)
                )
            self.list.append(new_car)
        else:
            self.list.append(
                self.reuse_list[0]
            )
            self.list[-1].teleport(
                300,
                random.randint(-250, 250)
                )
            self.reuse_list.remove(
                self.reuse_list[0]
            )
