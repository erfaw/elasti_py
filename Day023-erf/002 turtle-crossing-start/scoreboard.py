from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.level = 1
        self.__prepare_writer()

    def __prepare_writer(self):
        self.writer = Turtle()
        self.writer.penup()
        self.writer.hideturtle()
        self.writer.teleport(-295, 255)
        self.writer.write(f"Level: {self.level}", False, "left", FONT)

    def update_level(self):
        self.level += 1
        self.writer.clear()
        self.writer.write(f"Level: {self.level}", False, "left", FONT)

    def game_over(self):
        self.writer.teleport(-100,0)
        self.writer.write("Game Over!!", False, "left", FONT)