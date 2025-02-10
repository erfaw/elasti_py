from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.my_board = self.make_scoreboard()
    
    def make_scoreboard(self): 
        new_board = Turtle()
        new_board.penup()
        new_board.teleport(0,280)
        new_board.hideturtle()
        new_board.color("white")
        new_board.pendown()
        new_board.write(f"Score: {self.score}", False, "center", ("Arial", 14, "normal"))
        return new_board
    
    def update(self):
        self.my_board.clear()
        self.my_board.write(f"Score: {self.score}", False, "center", ("Arial", 14, "normal"))
