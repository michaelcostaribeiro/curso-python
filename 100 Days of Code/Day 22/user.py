from paddle import Paddle
from turtle import Screen

class User(Paddle):
    def __init__(self):
        super().__init__()
        self.teleport(-280,0)
        self.controls = Screen()
        self.up()
        self.controls.onkeypress(self.move_up,'Up')
        self.controls.onkeypress(self.move_down,'Down')
        self.controls.listen()

    def move_up(self):
        self.goto(self.xcor(), self.ycor()+30)
        

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-30)
    
