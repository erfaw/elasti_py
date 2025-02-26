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

while game_over == False:
    #tayin reflect baraye divar ha
    if (ball.ycor() >= DOMAIN_Y-20 or ball.ycor() <= -(DOMAIN_Y-20) ) and ball.is_stop == True:
        ball.reflect_wall()
    # tayin reflect paddle
    elif (left_paddle.xcor() < ball.xcor() <= left_paddle.xcor()+20 and left_paddle.ycor()-30 < ball.ycor() < left_paddle.ycor()+30 ):
        ball.reflect_paddle()
    elif right_paddle.xcor()-21 < ball.xcor() <= right_paddle.xcor() and right_paddle.ycor()-30 < ball.ycor() < right_paddle.ycor()+30 :
        ball.reflect_paddle()
        
    ball.move()

        
    time.sleep(0.1)
    my_sc.update()
    
my_sc.exitonclick()