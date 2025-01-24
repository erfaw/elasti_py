import colorgram, turtle
from turtle import Screen
import random

colors_of_pic = colorgram.extract(r"C:\Users\ErF\Desktop\python\elasti_py\Day018-erf\image.jpg", 30)

colors = [
    (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)
]

tim = turtle.Turtle()
tim.penup()
tim.setpos(-300, -250)
my_screen = Screen()
my_screen.colormode(255)

for _ in range(10):
    for _ in range(10):
        tim.dot( 20 , random.choice(colors) )
        tim.forward(50)
    tim.setpos(
    -300 , tim.ycor() + 50
    )


my_screen.exitonclick()
