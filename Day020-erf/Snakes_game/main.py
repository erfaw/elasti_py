from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
my_sc = Screen()
my_sc.bgcolor('black')
my_sc.setup(width=600, height=600)
my_sc.title("my Snake game")
my_sc.tracer(0)
score = 0

snake = Snake() 
food = Food()

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
    time.sleep(0.1)
    snake.move()
    # ye if , baraye check kardan food_position ba position sare snake, age bod score += 1 va ye food jadid 
    if food.food.xcor()-18 <= snake.turtles[0].xcor() <= food.food.xcor()+18 and food.food.ycor()-18 <= snake.turtles[0].ycor() <= food.food.ycor()+18 :
        score +=1
        snake.growth()
        print(score)
        food.move_random_place()
    else: 
        continue
    
my_sc.exitonclick()
