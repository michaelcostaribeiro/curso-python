import turtle as t
from color_data import colors
from random import choice, randint
from name_data import name_pool

players = []

class Runner:
    def __init__(self,name):
        self.name = t.Turtle()
        self.nickname = name
        self.name.shape('turtle')
        self.name.color(choice(colors))
        self.name.speed('fast')
    
    def run(self):
        self.name.forward(randint(0,20))

class Race:
    def __init__(self, number_of_runners):
        self.screen = t.Screen()
        RedTurtle(self.screen)
        self.generate_players(number_of_runners)
        self.position_turtles()
        self.run()
        self.screen.exitonclick()


    def generate_players(self, number_of_runners):
        for i in range(0,number_of_runners):
            players.append(Runner(choice(name_pool)))
    
    def position_turtles(self):
        self.position_changer = self.screen.window_height()/len(players)
        self.current_position = self.screen.window_height()/2 - (self.position_changer/2)
        for i in range(0,len(players)):
            players[i].name.teleport(self.screen.window_width()/2*-1+20,self.current_position)
            self.current_position -= self.position_changer
    
    def run(self):
        finished = False
        while not finished:
            for i in range(0, len(players)):
                players[i].run()
                if(players[i].name.xcor()>self.screen.window_width()/2-70):
                    print(f'{players[i].nickname} has won!')
                    finished = True
                    break

class RedTurtle:
    def __init__(self, screen):
        self.red = t.Turtle('turtle')
        self.red.color('red')
        self.red.teleport(screen.window_width()/2-70, screen.window_height()/2*-1-50)
        self.red.setheading(90)
        self.red.forward(screen.window_height()+100)