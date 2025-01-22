from turtle import Turtle, Screen
import random

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
def draw_dashed_line(degree):
    """draw a dashed line with turtle."""
    tim.penup()
    tim.setpos(-300, 0) # change first position of turtle to -100x.
    for _ in range(degree):
        tim.pendown()
        tim.forward(20)
        tim.penup()
        tim.forward(20)
# draw_dashed_line(15)

# draw triangle, square, pentagon, ..., decagon with a side common
colors = ['red', 'green', 'blue', 'orange', 'black', 'purple', 'DarkRed', 'yellow', 'grey']
def draw_by_number_side():
    for number_side in range(3,11): # 3 for triangle, 4 for square etc. 
        tim.setpos(0,0)
        tim.pencolor(
            colors[number_side-3] # get right index 
        )
        for _ in range(number_side): # drawing based on how many sides the shape has
            tim.forward(100)
            tim.right(360/number_side)
# draw_by_number_side()

# Draw a random walk 
def draw_random_walk(degree):
    tim.pensize(5)
    for _ in range(degree):
        tim.pencolor(
            random.choice(colors)
        )
        for _ in range(random.randint(1,4)):
            tim.left(90)
        tim.forward(25)
# draw_random_walk(50)

def draw_spirograph(degree):
    tim.pensize(3)
    tim.speed("fastest")
    for _ in range(int(360/degree)):
        # tim.pencolor(random.choice(colors))
        tim.pencolor(random.random(),random.random(),random.random())
        tim.circle(100)
        tim.left(degree)

draw_spirograph(7)
    
# baraye inke nemayesh bedim o ba click az safhe kharej beshe :
my_screen = Screen()
my_screen.exitonclick()