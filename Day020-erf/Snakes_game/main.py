from turtle import Turtle, Screen
import random, time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from box import Box
from game_over_message import Game_over_message
my_sc = Screen()
my_sc.bgcolor('black')
my_sc.setup(width=600, height=600)
my_sc.title("my Snake game")
my_sc.tracer(0)

snake = Snake() 
food = Food()
scoreboard = Scoreboard()
box = Box(
    screen_width= my_sc.window_width() ,
    screen_height= my_sc.window_height()
)
game_over_message = Game_over_message()

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
    if food.is_ate(head= snake.head):
        scoreboard.score +=1
        scoreboard.update()
        snake.growth()
        food.move_random_place()
    elif snake.is_hit_wall(wide_cor= box.wide_cor) :
        is_game_over = True
        snake.change_body_color(color= 'red')
        my_sc.update()
    elif snake.is_hit_tail():
        is_game_over = True
        snake.change_body_color(color= 'red')
        my_sc.update()
    else: continue
    game_over_message.make_game_over_message()
my_sc.exitonclick()
