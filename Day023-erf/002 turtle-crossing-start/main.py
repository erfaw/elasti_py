import time
from turtle import Screen
from player import Player
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('gray')
screen.tracer(0)
player = Player()
screen.onkey(key="Up", fun= player.move_up)
screen.listen()

cars = CarManager()


game_is_on = True
i = 1
while game_is_on:
    if i % 6 == 0:
        cars.make_car()
        for car in cars.list:
            if car.xcor() < -310:
                cars.reuse_list.append(car)
                cars.list.remove(car)
    for car in cars.list:
        car.fd(MOVE_INCREMENT)
    time.sleep(0.1)
    screen.update()
    i += 1
