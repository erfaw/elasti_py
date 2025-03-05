from turtle import Screen, Turtle
WIDTH = 1000
HEIGHT = 650
DOMAIN_X = WIDTH/2
DOMAIN_Y = HEIGHT/2

class Sc:
    def __init__(self):
        self.my_sc = Screen()
        self.root_window = self.my_sc.getcanvas().winfo_toplevel()
        self.mid_line = Turtle()
        self.white_box = Turtle()
        self.details = Turtle()
        self.delay_notif = Turtle()
        self.__prepare_()
        self.window_size_lock()
        self.my_sc.update()


    def __prepare_(self):
        # my_sc
        self.my_sc.tracer(0)
        self.my_sc.setup(width=WIDTH, height=HEIGHT+50)
        self.my_sc.bgcolor('black')
        # mid_line
        self.mid_line.teleport(-5, 325)
        self.mid_line.hideturtle()
        self.mid_line.pencolor('white')
        self.mid_line.setheading(270)
        self.mid_line.pensize(5)
        while self.mid_line.ycor() > -325:
            self.mid_line.fd(10)
            self.mid_line.penup()
            self.mid_line.fd(10)
            self.mid_line.pendown()
        # white_box
        self.white_box.hideturtle()
        self.white_box.pencolor('white')
        self.white_box.pensize(3)
        self.white_box.teleport(
            -DOMAIN_X,+DOMAIN_Y
        )
        self.white_box.goto(
            +DOMAIN_X, +DOMAIN_Y
        )
        self.white_box.goto(
            +DOMAIN_X, -DOMAIN_Y
        )
        self.white_box.goto(
            -DOMAIN_X, -DOMAIN_Y
        )
        self.white_box.goto(
            -DOMAIN_X, +DOMAIN_Y
        )
        # details
        self.details.hideturtle()
        self.details.pencolor('white')
        self.details.teleport(-DOMAIN_X+10, DOMAIN_Y)
        self.details.write(
            "Up=W    Down=S",
            False,
            "left",
            ("Arial", 12, "bold")
            )
        self.details.teleport(-(-DOMAIN_X+10), DOMAIN_Y)
        self.details.write(
            "Up=↑    Down=↓",
            False,
            "right",
            ("Arial", 12, "bold")
        )
        # delay_notif
        self.delay_notif.hideturtle()
        self.delay_notif.teleport(-15,0)
        self.delay_notif.pencolor('white')

    def window_size_lock(self):
        self.root_window.resizable(False, False)

    def window_size_unlock(self):
        self.root_window.resizable(True, True)

