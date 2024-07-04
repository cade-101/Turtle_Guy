from turtle import Screen
from car import Car
from scoreboard import Scoreboard
from turtle_guy import Guy
import time
import random

SPAWN_PERCENT = 20
MOVE_SPEED = 0.1
car_list = []


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


turtle_guy = Guy()
scoreboard = Scoreboard()
screen.onkey(key='Up', fun=turtle_guy.go_up)
screen.onkey(key='Down', fun=turtle_guy.go_down)
screen.onkey(key='Left', fun=turtle_guy.go_left)
screen.onkey(key='Right', fun=turtle_guy.go_right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(MOVE_SPEED)
    if random.randrange(0, 100) < SPAWN_PERCENT:
        car = Car(xcor=280, ycor=random.randrange(-270, 280))
        car_list.append(car)
    for car in car_list:
        car.move_car()
    #detect collision with car
        if turtle_guy.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()
    #detect collision with upper wall
        if turtle_guy.ycor() > 290:
            turtle_guy.level_up()
            scoreboard.level_up()
            SPAWN_PERCENT += 3
            MOVE_SPEED *= 0.9









screen.exitonclick()