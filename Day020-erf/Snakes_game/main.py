from turtle import Turtle, Screen
import random
import time
my_sc = Screen()
my_sc.bgcolor('black')
my_sc.setup(width=600, height=600)
my_sc.title("my Snake game")
my_sc.tracer(0)
score = 0

# make the body of snake (4 square)
turtles = []
def make_new_turtle():
    """make a turtle with white color and fastest speed and shapesize 0.5, 0.5 and return that object"""
    new_turtle = Turtle('square')
    new_turtle.penup()
    new_turtle.color('white')
    new_turtle.speed("fastest")
    new_turtle.shapesize(0.5,0.5)
    return new_turtle
    
for turtle_index in range(4): 
    new_turtle = make_new_turtle()

    if not turtle_index == 0:
        new_turtle.goto(
            turtles[turtle_index-1].xcor()-18, 0
        )
    turtles.append(new_turtle)


# set specific color and shape to head of snake
turtles[0].shape('triangle')
# turtles[0].shapesize(0.4,0.4)
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
def make_food():
    """make a food object, move it to a random place, return object"""
    food = Turtle('circle')
    food.penup()
    food.color('blue')
    food.shapesize(0.8, 0.8)
    food.teleport(
        random.randint(-250, 250),
        random.randint(-250, 250)
    )
    food.speed("fastest")
    
    return food

food_pos = make_food()

# Loop baraye harekat khodkar be jelo
my_sc.update()
while not is_game_over:
    # my_sc.tracer(1)
    first_position_x = turtles[0].xcor()
    first_position_y = turtles[0].ycor()
    my_sc.update()
    time.sleep(0.1)
    turtles[0].fd(10)
    
    # ye if , baraye check kardan food_position ba position sare snake, age bod score += 1 va ye food jadid 
    if food_pos.xcor()-5 <= turtles[0].xcor() <= food_pos.xcor()+5 and food_pos.ycor()-5 <= turtles[1].ycor() <= food_pos.ycor()+5 :
        

        score +=1
        growth_snake = make_new_turtle()
        growth_snake.teleport(
            turtles[len(turtles)-1].xcor(),
            turtles[len(turtles)-1].ycor()
        )
        

        turtles.append(
            growth_snake
        )
        food_pos.hideturtle()
        food_pos = make_food()
        

    raw_prev_position = 0
    for snake_body in range(len(turtles)) :
        if snake_body == 0 : 
            pass
        else: 
            

            raw_prev_position = turtles[snake_body].position()
            turtles[snake_body].teleport(
                first_position_x, first_position_y
            )
            

            first_position_x = raw_prev_position[0]
            first_position_y = raw_prev_position[1]
    
my_sc.exitonclick()
