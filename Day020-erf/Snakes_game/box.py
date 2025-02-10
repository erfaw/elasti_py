from turtle import Turtle
class Box:
    def __init__(self, screen_width, screen_height):
        self.box = self.make_box(
            screen_width,
            screen_height
            )
        
    def make_box(self, sc_width, sc_height):
        """based on width and height of turtle screen make a white box for game"""
        right_w = sc_width/2 -40
        right_h = sc_height/2 -40
        box = Turtle()
        box.penup()
        box.teleport(-right_w, right_h)
        box.hideturtle()
        box.pendown()
        box.pensize(10)
        box.pencolor('white')
        box.goto(right_w, right_h)
        box.goto(right_w, -right_h)
        box.goto(-right_w, -right_h)
        box.goto(-right_w, right_h)
        return box