from turtle import Turtle, Screen
import random
my_sc = Screen()
my_sc.setup(width= 500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False

not_catched = True
while not_catched: 
    user_bet = my_sc.textinput(title="Make a bet", prompt=f"which turtle will be first one({" ,".join(colors)})?")
    if user_bet.lower() in colors:
        is_race_on = True
        not_catched = False

#build 6 turtle

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