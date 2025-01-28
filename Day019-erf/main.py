from turtle import Turtle, Screen
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

trtl_1 = Turtle(shape="turtle")
trtl_1.goto(x= -(current_x/2)+40, y=true_height())
trtl_2 = Turtle(shape="turtle")
trtl_2.goto(x= -(current_x/2)+40, y=true_height())
trtl_3 = Turtle(shape="turtle")
trtl_3.goto(x= -(current_x/2)+40, y=true_height())
trtl_4 = Turtle(shape="turtle")
trtl_4.goto(x= -(current_x/2)+40, y=true_height())
trtl_5 = Turtle(shape="turtle")
trtl_5.goto(x= -(current_x/2)+40, y=true_height())
trtl_6 = Turtle(shape="turtle")
trtl_6.goto(x= -(current_x/2)+40, y=true_height())
# set colors

# Move them to left side , lined.


my_sc.exitonclick()