from screen import my_sc,details, white_box, DOMAIN_X, DOMAIN_Y
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

left_paddle = Paddle(position="left")
right_paddle = Paddle(position="right")
ball = Ball()
scoreboard = Scoreboard()
round_over = False
game_over = False
enter_pressed = False
escape_pressed = False

def on_enter_pressed():
    global enter_pressed
    if not round_over:
        enter_pressed = True
def on_escape_pressed():
    global escape_pressed
    if not round_over:
        escape_pressed = True
# add event listeners
my_sc.onkey(
    left_paddle.move_up
    ,'w')
my_sc.onkey(
    left_paddle.move_down
    ,'s')
my_sc.onkey(
    right_paddle.move_up
    ,'Up')
my_sc.onkey(
    right_paddle.move_down
    ,'Down')
my_sc.onkey(
    on_enter_pressed
    ,'Return') # 'enter' key on keyboard
my_sc.onkey(
    on_escape_pressed
    ,'Escape') # 'enter' key on keyboard
my_sc.listen()

def game_round():
    my_sc.update()
    round_over = False
    ball.first_place()
    while not round_over:
        #tayin reflect baraye divar ha
        if ball.is_near_wall() and ball.is_stop == True:
            ball.reflect_wall()
        # tayin reflect paddle
        elif right_paddle.is_hit_ball(ball.pos()) or left_paddle.is_hit_ball(ball.pos()) :
            ball.reflect_paddle()
        # tayin game over va scoring
        elif not left_paddle.xcor() <= ball.xcor() <= right_paddle.xcor():
            if ball.xcor() < left_paddle.xcor() and ball.is_stop:
                print('score for right')
                scoreboard.score_for_right()
                round_over = True
                
            elif ball.xcor() > right_paddle.xcor() and ball.is_stop:
                print('score for left')
                scoreboard.score_for_left()
                round_over = True
            
        ball.move()
        time.sleep(0.1)
        my_sc.update()

my_sc.update()
while not game_over:
    if enter_pressed:
        game_round()
        enter_pressed = False
    elif escape_pressed:
        game_over = True
    else: 
        pass
    time.sleep(0.1)
    my_sc.update()
