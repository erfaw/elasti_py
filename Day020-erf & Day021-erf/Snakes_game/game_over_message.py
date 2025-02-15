from turtle import Turtle
class Game_over_message:
    def __init__(self):
        pass
        
    def make_game_over_message(self):
        msg = Turtle()
        msg.pencolor('white')
        msg.write("GAME OVER !!!", False, "center", ("Arial", 40, "bold"))