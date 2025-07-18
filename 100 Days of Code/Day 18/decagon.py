from turtle import Turtle, Screen
from color_data import colors
from random import choice


def create_random_color():
    return choice(colors)

timmy = Turtle()
screen = Screen()

for i in range(3,11):
    radius = 360/i
    timmy.color(create_random_color())
    for j in range(0,i):
        timmy.forward(90)
        timmy.right(radius)

screen.exitonclick()