from turtle import Turtle, Screen
import random
my_sc = Screen()
my_sc.bgcolor('black')
my_sc.setup(width=550, height=550)

score = 0

# make the body of snake (4 square)
turtles = []
for turtle_index in range(4): 
    new_turtle = Turtle('square')
    new_turtle.penup()
    new_turtle.color('white')
    new_turtle.speed("fastest")
    if not turtle_index == 0:
        new_turtle.goto(
            turtles[turtle_index-1].xcor()-18, 0
        )
    turtles.append(new_turtle)

# set specific color and shape to head of snake
turtles[0].shape('triangle')
turtles[0].color('orange')

# some variable and function to move turtle
is_game_over = False
def h_left():
    """set heading to """
    if not turtles[0].heading() == 0 :
        turtles[0].setheading(180)
    else: pass
def h_right():
    """set heading to """
    
    if not turtles[0].heading() == 180 :
        turtles[0].setheading(0)
    else: pass
def h_up():
    """set heading to """
    if not turtles[0].heading() == 270 :
        turtles[0].setheading(90)
    else: pass    
def h_down():
    """set heading to """
    if not turtles[0].heading() == 90 :
        turtles[0].setheading(270)
    else: pass 

# adding event listener to some keys (W,A,S,D) to direct turtle
my_sc.onkey(fun=h_up, key="w")
my_sc.onkey(fun=h_left, key="a")
my_sc.onkey(fun=h_down, key="s")
my_sc.onkey(fun=h_right, key="d")
my_sc.listen()

counter_call_back = 1
def call_back_move(x_togo, y_togo):
    """ye callback function hast ke ba estefade az oon position e ghabl az fd(10) ro negah midarim o baad az fd(10) roye turtle[0] pass midim be turtle badi va hminjori ta enteha, ke dar enteha baes avali 10 ta harekat kne va ma ba onkey() ha on avali ro control miknim, baghie az on avali tabaiat miknn zanjire var"""
    global counter_call_back
    if counter_call_back <= len(turtles)-1:
        prev_position_x = turtles[counter_call_back].xcor()
        prev_position_y = turtles[counter_call_back].ycor()
        turtles[counter_call_back].goto(
            x_togo, y_togo
        )
        counter_call_back += 1
        call_back_move(
            prev_position_x, prev_position_y
        )
    else:
        counter_call_back = 1

# add food by random
food = Turtle('circle')
food.penup()
food.color('blue')
food.shapesize(0.7, 0.7)
food.goto(
    random.randint(-250, 250),
    random.randint(-250, 250)
)
food_position = food.pos()


# Loop baraye harekat khodkar be jelo
while not is_game_over:
    first_position_x = turtles[0].xcor()
    first_position_y = turtles[0].ycor()
    turtles[0].fd(10)
    
    call_back_move(
        first_position_x, first_position_y
    )
            

my_sc.exitonclick()
