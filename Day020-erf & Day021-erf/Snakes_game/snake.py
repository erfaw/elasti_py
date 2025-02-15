from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0), (-60,0)]
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
        self.is_hit = self.is_hit_tail()

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
        self.is_hit = self.is_hit_tail()
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
        
    def growth(self):
        growth_snake = self.make_new_turtle()
        growth_snake.teleport(
            self.turtles[len(self.turtles)-1].xcor(),
            self.turtles[len(self.turtles)-1].ycor()
        )
        self.turtles.append(
            growth_snake
        )
        
    def change_body_color(self, color):
        for sq in self.turtles:
            sq.color(color)
            
    def is_hit_wall(self, wide_cor):
        """arg: wide_cor, 'wide_cor' bayad ye tuple bashe ke doamin_x va domain_y white box ro dakhelesh dre. tuple = (domain_x , domain_y)"""
        domain_x = wide_cor[0]-5 
        domain_y = wide_cor[1]-5
        if not -domain_x <= self.head.xcor() <= domain_x or not -domain_y <= self.head.ycor() <= domain_y :
            return True
        else: 
            return False

    def is_hit_tail(self):
        for sq in self.turtles:
            if sq == self.turtles[0]:
                continue
            sq_x = sq.pos()[0]
            sq_y = sq.pos()[1]
            head_x = self.head.pos()[0]
            head_y = self.head.pos()[1]
            
            # if self.head.pos() == sq.pos():
            if sq_x-10 <= head_x <= sq_x+10 and sq_y-10 <= head_y <= sq_y+10 :
                return True
            else: 
                continue
        return False