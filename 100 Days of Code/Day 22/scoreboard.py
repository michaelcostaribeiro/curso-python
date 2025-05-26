from turtle import Turtle

FONT = ('Courier', 50, 'bold')
ALIGN = 'center'

class Scoreboard(Turtle):
    def __init__(self, draw_line):
        super().__init__()
        self.ht()
        self.speed(100)
        self.color('white')
        self.teleport(0,-300)
        self.pensize(5)
        if draw_line == True:
            self.draw_dotted_line(18)
    
    def draw_dotted_line(self, number_of_lines):
        self.setheading(90)
        for i in range(0, number_of_lines):
            self.pd()
            self.forward(20)
            self.pu()
            self.forward(20)
    
    def render_score(self, player, player_score):
        if player == 'user':
            self.clear()
            self.teleport(-70,200)
            self.write(player_score, False, ALIGN, FONT)
        elif player == 'enemy':
            self.clear()
            self.teleport(70,200)
            self.write(player_score, False, ALIGN, FONT)