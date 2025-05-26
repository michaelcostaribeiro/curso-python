from turtle import Turtle
from random import randrange
from config import MOVE_DISTANCE




class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.shapesize(.5)
        self.refresh()
        
    def refresh(self):
        self.randomX = round(randrange(-280, 280, 20))
        self.randomY = round(randrange(-280, 280, 20))
        self.teleport(self.randomX, self.randomY)
