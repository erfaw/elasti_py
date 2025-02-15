from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.make_paddle()
        
    def make_paddle(self):
        self.color('white')
        self.shape('square')
        self.turtlesize(stretch_len=0.7, stretch_wid=3)