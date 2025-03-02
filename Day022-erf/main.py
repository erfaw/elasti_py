from screen import my_sc, white_box, DOMAIN_X, DOMAIN_Y
from paddle import Paddle
import time
from ball import Ball

left_paddle = Paddle(position="left")
right_paddle = Paddle(position="right")
ball = Ball()
game_over = False

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
my_sc.listen()

# Right paddle x_cor = 475
# Left paddle x_cor = -480
while game_over == False:
    #tayin reflect baraye divar ha
    if ball.is_near_wall() and ball.is_stop == True:
        ball.reflect_wall()
    # tayin reflect paddle
    elif right_paddle.is_hit_ball(ball.pos()) or left_paddle.is_hit_ball(ball.pos()) :
        ball.reflect_paddle()
    ball.move()

        
    time.sleep(0.1)
    my_sc.update()
    
my_sc.exitonclick()