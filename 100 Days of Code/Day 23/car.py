from turtle import Turtle
from random import choice, randint
from color_data import colors

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.color(choice(colors))
        self.shape('square')
        self.shapesize(1,2,1)
        self.goto(350, randint(-250, 250))
    
    def move(self):
        self.goto(self.xcor()-10, self.ycor())
    
    def car_crash(self, player):
        if self.distance(player)<20 :
            return True
        else:
            return False
