import turtle as t
from random import choice,randint

t.colormode(255)
def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

dan = t.Turtle()
dan.pensize(1)
dan.speed('fastest')

def draw_spirograph(size_of_gap):
    for _ in range(round(360 / size_of_gap)):
        dan.color(random_color())
        dan.circle(100)
        dan.setheading(dan.heading() + size_of_gap)

draw_spirograph(2)


t.exitonclick()