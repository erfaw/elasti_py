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
        self.food.shapesize(0.8, 0.8)

        self.food.speed("fastest")
        
    def move_random_place(self):
        self.food.teleport(
            random.randint(-250, 250),
            random.randint(-250, 250)
        )
        
    def xcor(self):
        return self.food.xcor()
    def ycor(self):
        return self.food.xcor()