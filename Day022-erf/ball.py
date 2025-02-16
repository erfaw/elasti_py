from turtle import Turtle
import random
from screen import DOMAIN_Y

MOVE_DISTANCE = 30 
class Ball(Turtle):
    """a ball for pong game that start moving randomlly, inherited from Turtle()"""
    def __init__(self):
        super().__init__()
        self.__prepare_appearance()
        
    def __prepare_appearance(self):
        self.shape('circle')
        self.color('red')
        self.penup()
        self.setheading(random.randint(135, 225)) #random for first move toward left side.
        self.teleport(
            x=-5,
            y= random.randint
            (-int(DOMAIN_Y-80),+int(DOMAIN_Y-80))
            )

    def move(self):
        self.fd(MOVE_DISTANCE)