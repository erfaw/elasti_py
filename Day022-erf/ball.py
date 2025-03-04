from turtle import Turtle
import random
from screen import DOMAIN_Y, DOMAIN_X

MOVE_DISTANCE = 20 
class Ball(Turtle):
    """a ball for pong game that start moving randomlly, inherited from Turtle()"""
    def __init__(self):
        super().__init__()
        self.__prepare_appearance()
        self.is_stop = False
        
    def __prepare_appearance(self):
        self.shape('circle')
        self.color('red')
        self.speed('fastest')
        self.penup()
        self.first_place()
    
    def first_place(self):
        """set the place for first of round"""
        self.setheading(random.randint(135, 225)) 
        self.teleport(
            x=-5,
            y= random.randint
            (-int(DOMAIN_Y-80),+int(DOMAIN_Y-80))
            )

    def move(self):
        if -DOMAIN_X < self.xcor() < DOMAIN_X and -DOMAIN_Y < self.ycor() < DOMAIN_Y:
            # self.is_stop = False
            self.fd(MOVE_DISTANCE)
        else: 
            self.is_stop = True
        
    def reflect_paddle(self): #besyar kasif neveshte shde
        """must change heading to a number that would be reflect of hiting paddle"""
        if 0 < self.heading() < 90:
            reflect_heading = 180 - self.heading() 
        elif 90 < self.heading() < 180:
            reflect_heading = abs(self.heading() - 180)
        elif 180 < self.heading() < 270:
            teta = (
                self.heading() - 180
            )
            reflect_heading =self.heading() + 180- 2*teta
        elif 270 < self.heading() < 360:
            reflect_heading = 180 + abs(self.heading() - 360)           
        else:
            reflect_heading = self.heading()+180
        
        self.setheading(reflect_heading)
        self.fd(MOVE_DISTANCE)
        self.is_stop = False
        
    def reflect_wall(self): #besyar kasif neveshte shde
        """must change heading to a number that would be reflect of hiting wall"""
        if 0 < self.heading() < 90:
            teta = 90 - self.heading()
            reflect_heading = self.heading() + 180 + teta + teta
        elif 90 < self.heading() < 180:
            teta = self.heading() - 90
            x = abs(180 - 2*(teta))
            reflect_heading = self.heading() + x
        elif 180 < self.heading() < 270:
            teta = 270 - self.heading()
            x = 180 - 2*teta
            reflect_heading =self.heading() - x 
        elif 270 < self.heading() < 360:
            teta = self.heading() - 270
            reflect_heading = self.heading() - 180 - 2*teta          
        else:
            pass
        
        self.setheading(reflect_heading)
        self.fd(MOVE_DISTANCE)
        self.is_stop = False

    def is_near_wall(self):
        """return True if ball is near wall"""
        if self.ycor() >= DOMAIN_Y-20 or self.ycor() <= -(DOMAIN_Y-20):
            return True
        else:
            return False
        