from screen import my_sc, white_box, DOMAIN_X, DOMAIN_Y
from paddle import Paddle
import time
from ball import Ball

left_paddle = Paddle(position="left")
right_paddle = Paddle(position="right")
ball = Ball()

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

while True:
    if ball.is_stop == True:
        ball.reflect_wall()
        ball.is_stop = False
    else:
        print("else")
        ball.move()

        
    time.sleep(0.1)
    my_sc.update()
    
my_sc.exitonclick()