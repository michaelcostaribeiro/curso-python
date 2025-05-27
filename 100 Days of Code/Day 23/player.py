from turtle import Turtle, Screen

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.controls = Screen()
        self.controls.listen()
        self.controls.onkey(self.move_up,'Up')
        self.setheading(90)
        self.shape('turtle')
        self.up()
        self.teleport(0,-280)

    def move_up(self):
        self.forward(20)
