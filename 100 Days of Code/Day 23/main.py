import turtle as t
import time
from scoreboard import Scoreboard
from car import Car
from random import randint
from player import Player

screen = t.Screen()
screen.setup(600,600)
screen.tracer(0)

scoreboard = Scoreboard()
car_array = [Car(),Car(),Car()]

game_over = True

current_difficulty = 0.175

player = Player()

while game_over:
    random_number = randint(1,5-scoreboard.current_level)
    if random_number == 1:
        car_array.append(Car())
    for car in car_array:
        car.move()
        if car.car_crash(player):
            game_over = False
            scoreboard.render_game_over()
    time.sleep(current_difficulty)
    screen.update()


    if player.ycor()>300:
        player.teleport(0,-280)
        current_difficulty *= .85
        scoreboard.current_level += 1
        scoreboard.render_level()



screen.exitonclick()
