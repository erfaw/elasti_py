from turtle import Turtle
import random

class Food:
    def __init__(self):
        self.make_food()
        self.move_random_place()
        
    def make_food(self):
        """make a food object, move it to a random place, return object"""
        self.food = Turtle('circle')
        self.food.penup()
        self.food.color('blue')
        self.food.speed("fastest")
        
    def move_random_place(self):
        self.food.teleport(
            random.randint(-250, 250),
            random.randint(-250, 250)
        )
        
    def is_ate(self, head):
        head_x = head.xcor()
        head_y = head.ycor()
        if self.food.xcor()-18 <= head_x <= self.food.xcor()+18 and self.food.ycor()-18 <= head_y <= self.food.ycor()+18:
            return True
        else: 
            return False
        