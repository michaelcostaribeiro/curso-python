import turtle as t
from color_data import colors
from random import choice,randint

t.colormode(255)
angles = [0,90,180,270]


def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

dan = t.Turtle()
dan.pensize(10)
size_speed = 1

while True:
    dan.pencolor(random_color())
    dan.forward(25)
    dan.speed(size_speed)
    size_speed +=1
    dan.left(choice(angles))


