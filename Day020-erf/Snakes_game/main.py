from turtle import Turtle, Screen
tim = Turtle()
my_sc = Screen()
my_sc.bgcolor('black')
turtles = []
for turtle_index in range(10): # make the body of snake (3 square)
    new_turtle = Turtle('square')
    new_turtle.penup()
    new_turtle.color('white')
    new_turtle.speed("fastest")
    if not turtle_index == 0:
        new_turtle.goto(
            turtles[turtle_index-1].xcor()-18, 0
        )
    turtles.append(new_turtle)

turtles[0].shape('triangle')
turtles[0].color('orange')
# turtles[0].speed("fastest")

#make turtle move forward
is_game_over = False
tr=''
def h_left():
    if not turtles[0].heading() == 0 :
        turtles[0].setheading(180)
    else: pass
def h_right():
    if not turtles[0].heading() == 180 :
        turtles[0].setheading(0)
    else: pass
def h_up():
    if not turtles[0].heading() == 270 :
        turtles[0].setheading(90)
    else: pass    

def h_down():
    if not turtles[0].heading() == 90 :
        turtles[0].setheading(270)
    else: pass 
my_sc.onkey(fun=h_up, key="w")
my_sc.onkey(fun=h_left, key="a")
my_sc.onkey(fun=h_down, key="s")
my_sc.onkey(fun=h_right, key="d")
my_sc.listen()

# mikhaym ye function callback benevisim ke jaye feli ro bede be ghabli va ghabli goto beshe onja va hamintori ta enteha
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

while not is_game_over:
    first_position_x = turtles[0].xcor()
    first_position_y = turtles[0].ycor()
    turtles[0].fd(10)
    
    call_back_move(
        first_position_x, first_position_y
    )
            

my_sc.exitonclick()
