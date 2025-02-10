from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
my_sc = Screen()
my_sc.bgcolor('black')
my_sc.setup(width=600, height=600)
my_sc.title("my Snake game")
my_sc.tracer(0)

snake = Snake() 
food = Food()
scoreboard = Scoreboard()

# Prepare a box 
box = Turtle()
box.penup()
box.teleport(-280, 280)
box.hideturtle()
box.pendown()
box.color('white')
box.pensize(10)
box.pencolor('white')
box.goto(280, 280)
box.goto(280, -280)
box.goto(-280, -280)
box.goto(-280, 280)

# adding event listener to some keys (W,A,S,D) to direct turtle
my_sc.onkey(fun=snake.h_up, key="w")
my_sc.onkey(fun=snake.h_left, key="a")
my_sc.onkey(fun=snake.h_down, key="s")
my_sc.onkey(fun=snake.h_right, key="d")
my_sc.listen()

# Loop baraye harekat khodkar be jelo
is_game_over = False
while not is_game_over:
    my_sc.update()
    time.sleep(0.15)
    snake.move()
    if food.is_ate(head= snake.head):
        scoreboard.score +=1
        scoreboard.update()
        snake.growth()
        food.move_random_place()
    else: 
        continue 
        # if not -295 <= snake.head.xcor() <= 287 or not -285 <= snake.head.ycor() <= 280 :
        #     is_game_over = True
        #     for sq in snake.turtles:
        #         sq.color('red')
        #         my_sc.update()

        # else: continue
    
my_sc.exitonclick()
