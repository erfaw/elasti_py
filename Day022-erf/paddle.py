from turtle import Turtle
import screen
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position.lower()
        self.make_paddle()
        
    def make_paddle(self):
        self.color('white')
        self.shape('square')
        self.turtlesize(stretch_len=0.7, stretch_wid=3)
        
        if self.position == "left":
            self.teleport(
                -(screen.WIDTH/2) + 20 ,
                0
            )
        elif self.position == "right":
            self.teleport(
               - (-(screen.WIDTH/2) + 25),
                0
            )
        else:
            raise ValueError("incorrect side, only 'right' and 'left' ")