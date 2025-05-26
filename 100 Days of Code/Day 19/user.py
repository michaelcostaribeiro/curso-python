from color_data import colors
from turtle import Turtle, Screen

class User:
    def __init__(self, turtle_name):
        self.turtle_name = Turtle()
        self.screen = Screen()
        self.screen.onkeypress(self.move_up,'Up')
        self.screen.onkeypress(self.move_left,'Left')
        self.screen.onkeypress(self.move_down,'Down')
        self.screen.onkeypress(self.move_right,'Right')
        self.screen.onkey(self.clear,'c')
        self.screen.onkey(self.semi_circle,'z')
        self.screen.onkey(self.semi_circle_counterclockwise,'x')
        self.screen.listen()


    def move_up(self):
        self.move(90)

    def move_left(self):
        self.move(180)

    def move_down(self):
        self.move(270)

    def move_right(self):
        self.move(0)

    def semi_circle(self):
        self.turtle_name.circle(90, 180)

    def semi_circle_counterclockwise(self):
        self.turtle_name.circle(90, -180)
        

    def clear(self):
        self.turtle_name.teleport(0,0)
        self.turtle_name.clear()

    def move(self, direction):
        self.turtle_name.setheading(direction)
        self.turtle_name.forward(30)

