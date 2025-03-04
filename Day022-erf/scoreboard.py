from turtle import Turtle
from screen import DOMAIN_X, DOMAIN_Y
NUMBER_SIZE = 60
FONT = "Arial"
class Scoreboard:
    def __init__(self):
        self.right = Turtle()
        self.left = Turtle()
        self.right_score = 0
        self.left_score = 0
        self.make_scoreboard()
    
    def make_scoreboard(self):
        """making scoreboard style and first initialized"""
        # prepare right
        self.right.hideturtle()
        self.right.color('white')
        self.right.teleport(70,DOMAIN_Y-120)
        self.right.write(
            self.right_score,
            False,
            'center',
            (FONT, NUMBER_SIZE, "bold")
            )

        # prepare left
        self.left.hideturtle()
        self.left.color('white')
        self.left.teleport(-75,DOMAIN_Y-120)
        self.left.write(
            self.left_score,
            False,
            'center',
            (FONT, NUMBER_SIZE, "bold")
            )

    def score_for_right(self):
        """give score to right and update it in screen"""
        self.right_score += 1
        self.right.clear()
        self.right.write(
        self.right_score,
        False,
        'center',
        (FONT, NUMBER_SIZE, "bold")
        )

    def score_for_left(self):
        """give score to left and update it in screen"""
        self.left_score += 1
        self.left.clear()
        self.left.write(
        self.left_score,
        False,
        'center',
        (FONT, NUMBER_SIZE, "bold")
        )
