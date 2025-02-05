from turtle import Turtle, Screen
import random
import time
from snake import Snake
my_sc = Screen()
my_sc.bgcolor('black')
my_sc.setup(width=600, height=600)
my_sc.title("my Snake game")
my_sc.tracer(0)
score = 0

snake = Snake() 

# adding event listener to some keys (W,A,S,D) to direct turtle
my_sc.onkey(fun=snake.h_up, key="w")
my_sc.onkey(fun=snake.h_left, key="a")
my_sc.onkey(fun=snake.h_down, key="s")
my_sc.onkey(fun=snake.h_right, key="d")
my_sc.listen()

# add food by random
# def make_food():
#     """make a food object, move it to a random place, return object"""
#     food = Turtle('circle')
#     food.penup()
#     food.color('blue')
#     food.shapesize(0.8, 0.8)
#     food.teleport(
#         random.randint(-250, 250),
#         random.randint(-250, 250)
#     )
#     food.speed("fastest")
    
#     return food

# food_pos = make_food()

# Loop baraye harekat khodkar be jelo
is_game_over = False
while not is_game_over:
    my_sc.update()
    time.sleep(0.1)
    snake.move()
    
    # ye if , baraye check kardan food_position ba position sare snake, age bod score += 1 va ye food jadid 
    # if food_pos.xcor()-5 <= turtles[0].xcor() <= food_pos.xcor()+5 and food_pos.ycor()-5 <= turtles[1].ycor() <= food_pos.ycor()+5 :
        

    #     score +=1
    #     growth_snake = make_new_turtle()
    #     growth_snake.teleport(
    #         turtles[len(turtles)-1].xcor(),
    #         turtles[len(turtles)-1].ycor()
    #     )
        

    #     turtles.append(
    #         growth_snake
    #     )
    #     food_pos.hideturtle()
    #     food_pos = make_food()
    
my_sc.exitonclick()
