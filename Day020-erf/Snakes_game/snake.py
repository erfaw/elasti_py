from turtle import Turtle

class Snake():
    def make_new_turtle(self):
        """make a turtle with white color and fastest speed and shapesize 0.5, 0.5 and return that object"""
        new_turtle = Turtle('square')
        new_turtle.penup()
        new_turtle.color('white')
        new_turtle.speed("fastest")
        new_turtle.shapesize(0.5,0.5)
        return new_turtle
    
    def __init__(self):
        self.turtles = []
        for turtle_index in range(4): 
            new_turtle = self.make_new_turtle()
            if not turtle_index == 0:
                new_turtle.goto(
                    self.turtles[turtle_index-1].xcor()-18, 0
                )
            self.turtles.append(new_turtle)
            # set specific color and shape to head of snake
            self.turtles[0].shape('triangle')
            self.turtles[0].color('orange')
