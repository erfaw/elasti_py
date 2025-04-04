import time
from turtle import Screen
from player import Player, FINISH_LINE_Y, STARTING_POSITION
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

TIME_SLEEP = 0.1
game_is_on = True
i = 1
while game_is_on:
    if player.ycor() > FINISH_LINE_Y:
        player.teleport(STARTING_POSITION[0],STARTING_POSITION[1])
        TIME_SLEEP *= 0.9
    for car in cars.list:
        if car.distance(player) <= 45 and car.ycor()-14 <= player.ycor() <= car.ycor()+14:
            game_is_on = False
            break
    if i % 6 == 0:
        cars.make_car()
        for car in cars.list:
            if car.xcor() < -310:
                cars.reuse_list.append(car)
                cars.list.remove(car)
    for car in cars.list:
        car.fd(MOVE_INCREMENT)
    time.sleep(TIME_SLEEP)
    screen.update()
    i += 1

screen.exitonclick()