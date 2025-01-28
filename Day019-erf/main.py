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

turtles = []
for _ in range(6):
    trtl = Turtle(shape="turtle")
    trtl.color(colors[_])
    turtles.append(trtl)

my_sc.exitonclick()