from turtle import Turtle, Screen
import random
my_sc = Screen()
my_sc.setup(width= 800, height=500)
#build 6 turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

current_x = my_sc.window_width()
current_y = -(my_sc.window_height()/2) + 50
def true_height():
    global current_y
    current_y += 50
    return current_y - 50

turtles = [] # list for store turtles
for _ in range(6): # a loop for make, set color, set right position to turtles and store them in 'turtles'
    trtl = Turtle(shape="turtle")
    trtl.penup()
    trtl.color(colors[_])
    trtl.goto(x= -(current_x/2)+40, y=true_height())
    turtles.append(trtl)


my_sc.exitonclick()