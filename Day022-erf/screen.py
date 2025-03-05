from turtle import Screen, Turtle
# it's so important to set widht and height from here.
WIDTH = 1000
HEIGHT = 650
DOMAIN_X = WIDTH/2
DOMAIN_Y = HEIGHT/2
my_sc = Screen()
my_sc.tracer(0)
my_sc.setup(width=WIDTH, height=HEIGHT+50)
my_sc.bgcolor('black')

# baraye jelogiri az change size window e bazi , toplevel ro dakhele ye variable mirizim o baad method 'resizable()' ro call  miknim va width o height ro False gharar midim.
root_window = my_sc.getcanvas().winfo_toplevel()
root_window.resizable(False, False)

mid_line = Turtle()
mid_line.teleport(-5, 325)
mid_line.hideturtle()
mid_line.pencolor('white')
mid_line.setheading(270)
mid_line.pensize(5)

while mid_line.ycor() > -325:
    mid_line.fd(10)
    mid_line.penup()
    mid_line.fd(10)
    mid_line.pendown()
    
white_box = Turtle()
white_box.hideturtle()
white_box.pencolor('white')
white_box.pensize(3)
white_box.teleport(
    -DOMAIN_X,+DOMAIN_Y
)
white_box.goto(
    +DOMAIN_X, +DOMAIN_Y
)
white_box.goto(
    +DOMAIN_X, -DOMAIN_Y
)
white_box.goto(
    -DOMAIN_X, -DOMAIN_Y
)
white_box.goto(
    -DOMAIN_X, +DOMAIN_Y
)
my_sc.update()

details = Turtle()
# details.penup()
details.hideturtle()
details.pencolor('white')
details.teleport(-DOMAIN_X+10, DOMAIN_Y)

details.write(
    "Up=W    Down=S",
    False,
    "left",
    ("Arial", 12, "bold")
    )
my_sc.update()