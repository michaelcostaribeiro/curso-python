import turtle as t
from color_data import colors
from random import choice
import colorgram

t.colormode(255)
test_tuple = colorgram.extract('hirst-painting.jpg', 50)
colors_from_image = []

for i in range(0, len(test_tuple)):
    colors_from_image.append((test_tuple[i].rgb.r ,test_tuple[i].rgb.g ,test_tuple[i].rgb.b))



class Jimmy():
    def __init__(self, name):
        self.name = t.Turtle()
        self.name.fillcolor("white")
        self.name.teleport(-275,-275)
        self.screen_name = t.Screen()
        self.screen_name.setup(600,600)
        self.screen_width = self.screen_name.window_width()
        self.screen_height = self.screen_name.window_height()
        self.stamps = []

    def create_random_color(self):
        return choice(colors)

    def create_stamp(self):
        starting_pencolor = self.name.pencolor()
        starting_fillcolor = self.name.fillcolor()
        starting_shape = self.name.shape()
        self.name.shape('circle')
        random_color = choice(colors_from_image)
        self.name.color(random_color, random_color) # need to be fixed
        self.stamps.append(self.name.stamp())
        self.name.color(starting_pencolor, starting_fillcolor)
        self.name.shape(starting_shape)


    def tp_forward(self):
        self.create_stamp()
        jimmy_x_position = self.name.xcor()
        jimmy_y_position = self.name.ycor()
        if jimmy_x_position < self.screen_width/2 and jimmy_y_position < self.screen_height/2:
            self.name.teleport(self.name.xcor() + 60)
            return True
        elif jimmy_x_position > self.screen_width/2 and jimmy_y_position < self.screen_height/2:
            self.name.teleport(-275, jimmy_y_position+50)
            return True
        else:
            self.name.hideturtle()
            return False