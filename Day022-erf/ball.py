from turtle import Turtle
import random
from screen import DOMAIN_Y
class Ball(Turtle):
    """a ball for pong game that start moving randomlly, inherited from Turtle()"""
    def __init__(self):
        super().__init__()
        self.__prepare_appearance()
        
    def __prepare_appearance(self):
        self.shape('circle')
        self.color('red')
        self.penup()
        self.teleport(
            x=-5,
            y= random.randint
            (-int(DOMAIN_Y),+int(DOMAIN_Y))
            )
