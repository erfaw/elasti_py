from turtle import Turtle
import screen
from screen import DOMAIN_X, DOMAIN_Y

MOVING_DISTANCE = 20

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
        self.turtlesize (stretch_len=1, stretch_wid=5)
        
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

    def is_hit_ball(self, ball_pos):
        """check if paddle hit ball, return True, ball_pos must be 'ball.pos()' (a tuple with (x,y) cordinates)"""
        ball_xcor = ball_pos[0]
        ball_ycor = ball_pos[1]
        if self.position == 'right':
            if self.xcor()-21 < ball_xcor <= self.xcor() and self.ycor()-30 < ball_ycor < self.ycor()+30:
                return True
        elif self.position == 'left':
            if (self.xcor() < ball_xcor <= self.xcor()+20 and self.ycor()-30 < ball_ycor < self.ycor()+30 ):
                return True
        else:
            return False
