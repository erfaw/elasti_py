from turtle import Turtle
from screen import DOMAIN_X, DOMAIN_Y
NUMBER_SIZE = 60
FONT = "Arial"
class Scoreboard:
    def __init__(self):
        self.right = Turtle()
        self.left = Turtle()
        self.make_scoreboard()
    
    def make_scoreboard(self):
        """making scoreboard style and first initialized"""
        # prepare right
        self.right.hideturtle()
        self.right.color('white')
        self.right.teleport(70,DOMAIN_Y-120)
        self.right.write(0,False, 'center', (FONT, NUMBER_SIZE, "bold"))

        # prepare left
        self.left.hideturtle()
        self.left.color('white')
        self.left.teleport(70,DOMAIN_Y-120)
        self.left.write(0,False, 'center', (FONT, NUMBER_SIZE, "bold"))
