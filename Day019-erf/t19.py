from turtle import Turtle, Screen

arsh = Turtle()
my_sc = Screen()

def move_forward():
    arsh.forward(20)
    
def move_backward():
    arsh.backward(20)
    
def turn_left():
    arsh.left(10)
    
def turn_right():
    arsh.right(10)
    
def clear_drawing():
    arsh.clear()
    arsh.penup()
    arsh.home()
    arsh.pendown()

my_sc.onkey(move_forward, "w")
my_sc.onkey(move_backward, "s")
my_sc.onkey(turn_left, "a")
my_sc.onkey(turn_right, "d")
my_sc.onkey(clear_drawing, "c")
my_sc.listen()
my_sc.exitonclick()