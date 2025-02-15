from turtle import Screen, Turtle
WIDTH = 1000
HEIGHT = 650

my_sc = Screen()
my_sc.tracer(0)
my_sc.setup(width=WIDTH, height=HEIGHT)
my_sc.bgcolor('black')

mid_line = Turtle()
mid_line.teleport(0, 325)
mid_line.pencolor('white')
mid_line.setheading(270)
mid_line.pensize(5)

while mid_line.ycor() > -325:
    mid_line.fd(10)
    mid_line.penup()
    mid_line.fd(10)
    mid_line.pendown()
    
my_sc.update()
