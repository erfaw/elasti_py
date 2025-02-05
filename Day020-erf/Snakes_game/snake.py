from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0), (-60,0)]
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            new_turtle = self.make_new_turtle()
            new_turtle.goto(position)
            self.turtles.append(new_turtle)
        
    def make_new_turtle(self):
        """make a turtle with white color and fastest speed and shapesize 0.5, 0.5 and return that object"""
        new_turtle = Turtle('square')
        new_turtle.penup()
        new_turtle.color('white')
        # new_turtle.speed("fastest")
        # new_turtle.shapesize(0.5,0.5)
        return new_turtle

    def move(self):
        first_position_x = self.turtles[0].xcor()
        first_position_y = self.turtles[0].ycor()    
        self.turtles[0].fd(MOVE_DISTANCE)
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
                
    def h_left(self):
        """set heading to """
        if not self.head.heading() == 0 :
            self.head.setheading(180) 
        
    def h_right(self):
        """set heading to """
        if not self.head.heading() == 180 :
            self.head.setheading(0)
        
    def h_up(self):
        """set heading to """
        if not self.head.heading() == 270 :
            self.head.setheading(90)
          
    def h_down(self):
        """set heading to """
        if not self.head.heading() == 90 :
            self.head.setheading(270)
        