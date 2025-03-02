from turtle import Turtle
from screen import DOMAIN_X, DOMAIN_Y
NUMBER_SIZE = 60
FONT = "Arial"
class Scoreboard:
    def __init__(self):
        self.right_score = Turtle()
        self.left_score = Turtle()
        self.make_scoreboard()
    
    def make_scoreboard(self):
        """making scoreboard style and first initialized"""
        self.right_score.hideturtle()
        # self.left_score.hideturtle()
        self.right_score.color('white')
        self.right_score.teleport(70,DOMAIN_Y-120)
        self.right_score.write(0,False, 'center', (FONT, NUMBER_SIZE, "bold"))
