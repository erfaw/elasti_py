from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.__prepare()

    def __prepare(self):
        self.penup()
        self.shape('turtle')
        self.teleport(STARTING_POSITION[0], STARTING_POSITION[1])
        self.setheading(90)

    def move_up(self):
        self.fd(MOVE_DISTANCE)

