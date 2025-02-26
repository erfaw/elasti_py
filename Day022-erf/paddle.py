from turtle import Turtle
import screen
from screen import DOMAIN_X, DOMAIN_Y

MOVING_DISTANCE = 30

class Paddle(Turtle):
    """make a paddle for pong game, catch a arg: position , which helps move paddle to right side"""
    def __init__(self, position):
        super().__init__()
        self.position = position.lower()
        self.make_paddle()
        
    def make_paddle(self):
        self.color('white')
        self.penup()
        self.shape('square')
        self.turtlesize(stretch_len=0.7, stretch_wid=3)
        
        # teleport to right side by argument 'position'
        if self.position == "left":
            self.teleport(
                -(screen.DOMAIN_X) + 20 ,
                0
            )
        elif self.position == "right":
            self.teleport(
               - (-(screen.DOMAIN_X) + 25),
                0
            )
        else:
            raise ValueError("incorrect side, only 'right' and 'left' ")
        
    def move_up(self):
        if not self.ycor() >= DOMAIN_Y-54:
            self.sety(self.ycor()+MOVING_DISTANCE)
    def move_down(self):
        if not self.ycor() <= -(DOMAIN_Y-54):
            self.sety(self.ycor()-MOVING_DISTANCE)
