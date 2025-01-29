from turtle import Turtle, Screen
tim = Turtle()
my_sc = Screen()
my_sc.bgcolor('black')
turtles = []
for turtle_index in range(3): # make the body of snake (3 square)
    new_turtle = Turtle('square')
    new_turtle.penup()
    new_turtle.color('white')
    if not turtle_index == 0:
        new_turtle.goto(
            turtles[turtle_index-1].xcor()-18, 0
        )
    turtles.append(new_turtle)

turtles[0].shape('triangle')
turtles[0].color('orange')

#make turtle move forward
is_game_over = False
tr=''
def h_left():
    tr.setheading(180)
def h_right():
    tr.setheading(0)
def h_up():
    tr.setheading(90)
def h_down():
    tr.setheading(270)  
my_sc.onkey(fun=h_up, key="w")
my_sc.onkey(fun=h_left, key="a")
my_sc.onkey(fun=h_down, key="s")
my_sc.onkey(fun=h_right, key="d")
my_sc.listen()
position = ''
while not is_game_over:
    position = turtles[0].pos()
    turtles[0].fd(3)
    for turtle in turtles:
        turtle.goto(position)

        



my_sc.exitonclick()
