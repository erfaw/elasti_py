from turtle import Turtle, Screen
tim = Turtle()
my_sc = Screen()
my_sc.bgcolor('black')
turtles = []
for turtle_index in range(3): # make the body of snake (3 square)
    new_turtle = Turtle('square')
    new_turtle.penup()
    new_turtle.color('white')
    # new_turtle.speed("slow")
    if not turtle_index == 0:
        new_turtle.goto(
            turtles[turtle_index-1].xcor()-20, 0
        )
    turtles.append(new_turtle)

# turtles[0].shape('triangle')
# turtles[0].color('orange')

#make turtle move forward
is_game_over = False
tr=''
def h_left():
    turtles[0].setheading(180)
def h_right():
    turtles[0].setheading(0)
def h_up():
    turtles[0].setheading(90)

def h_down():
    turtles[0].setheading(270)  
my_sc.onkey(fun=h_up, key="w")
my_sc.onkey(fun=h_left, key="a")
my_sc.onkey(fun=h_down, key="s")
my_sc.onkey(fun=h_right, key="d")
my_sc.listen()

while not is_game_over:
    i=2
    turtles[0].fd(10)

    for tr in turtles:
        tr.fd(10)

            

def new_method():
    pass



my_sc.exitonclick()
