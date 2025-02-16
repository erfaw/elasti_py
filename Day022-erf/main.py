from screen import my_sc, white_box
from paddle import Paddle

left_paddle = Paddle(position="left")
right_paddle = Paddle(position="right")

my_sc.update()
my_sc.exitonclick()