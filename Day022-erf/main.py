from screen import my_sc
from paddle import Paddle

left_paddle = Paddle("left")
right_paddle = Paddle("right")

my_sc.update()
my_sc.exitonclick()