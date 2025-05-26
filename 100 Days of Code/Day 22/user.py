from paddle import Paddle
from turtle import Screen

class User(Paddle):
    def __init__(self):
        super().__init__()
        self.teleport(-280,0)
        self.controls = Screen()
        self.up()
        self.controls.onkey(self.move_up,'Up')
        self.controls.onkey(self.move_down,'Down')
        self.controls.listen()

    def move_down(self):
        if self.ycor()>-260:
            self.goto(-280,self.ycor()-20)

    def move_up(self):
        if self.ycor()<260:
            self.goto(-280,self.ycor()+20)

