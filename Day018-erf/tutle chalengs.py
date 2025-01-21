from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
tim.color('blue')

# Draw a Square 
def draw_square():
    """draw a square with tim"""
    tim.forward(100)
    for i in range(3):
        tim.right(90)
        tim.forward(100)

# Draw a dashed line:
def draw_dashed_line(how_many):
    """draw a dashed line with turtle."""
    tim.penup()
    tim.setpos(-300, 0) # change first position of turtle to -100x.
    for _ in range(how_many):
        tim.pendown()
        tim.forward(20)
        tim.penup()
        tim.forward(20)

draw_dashed_line(15)

# baraye inke nemayesh bedim o ba click az safhe kharej beshe :
my_screen = Screen()
my_screen.exitonclick()