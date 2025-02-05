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

    def move(self):
        first_position_x = self.turtles[0].xcor()
        first_position_y = self.turtles[0].ycor()    
        self.turtles[0].fd(10)
        raw_prev_position = 0
        for snake_body in range(len(self.turtles)) :
            if snake_body == 0 : 
                pass
            else: 
                raw_prev_position = self.turtles[snake_body].position()
                self.turtles[snake_body].teleport(
                    first_position_x, first_position_y
                )
                first_position_x = raw_prev_position[0]
                first_position_y = raw_prev_position[1]