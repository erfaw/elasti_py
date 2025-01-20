from turtle import Turtle, Screen

arshia = Turtle()
arshia.shape('turtle')
arshia.color('blue')

# Draw a Square 
arshia.forward(100)
for i in range(3):
    arshia.right(90)
    arshia.forward(100)


# baraye inke nemayesh bedim o ba click az safhe kharej beshe :
my_screen = Screen()
my_screen.exitonclick()