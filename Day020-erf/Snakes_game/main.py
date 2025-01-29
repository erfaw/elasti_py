from turtle import Turtle, Screen
tim = Turtle()
my_sc = Screen()
my_sc.bgcolor('black')
turtles = []
for turtle_index in range(3): # make the body of snake (3 square)
    new_turtle = Turtle('square')
    new_turtle.penup()
    new_turtle.color('white')
    if not turtle_index == 0:
        new_turtle.goto(
            turtles[turtle_index-1].xcor()-18, 0
        )
    turtles.append(new_turtle)

turtles[0].shape('triangle')
turtles[0].color('orange')

#make turtle move forward
is_game_over = False
def move():
    for turtle in turtles:
        turtle.fd(25)
while not is_game_over:
    for turtle in turtles:
        turtle.fd(3)



my_sc.exitonclick()
