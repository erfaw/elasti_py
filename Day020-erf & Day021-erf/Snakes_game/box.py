from turtle import Turtle
class Box:
    def __init__(self, screen_width, screen_height):
        self.box = self.make_box(
            screen_width,
            screen_height
            )
        self.wide_cor
        
    def make_box(self, sc_width, sc_height):
        """based on width and height of turtle screen make a white box for game"""
        right_w = sc_width/2 -20
        right_h = sc_height/2 -20
        self.wide_cor = self.box_position(right_w, right_h)
        box = Turtle()
        box.penup()
        box.teleport(-right_w, right_h)
        box.hideturtle()
        box.pendown()
        box.pensize(7)
        box.pencolor('white')
        box.goto(right_w, right_h)
        box.goto(right_w, -right_h)
        box.goto(-right_w, -right_h)
        box.goto(-right_w, right_h)
        return box
    
    def box_position(self, x,y):
        """return a tuple (x,y) for domain of white box has been made. x for width and y for height (whole width would be 2x and whole height woould be 2y)"""
        return (x , y)