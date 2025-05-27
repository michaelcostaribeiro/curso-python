from turtle import Turtle

FONT = ('Courier', 16, 'bold')
ALIGN = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.ht()
        self.color('black')
        self.current_level = 1
        self.render_level()
        
    def render_level(self):
        self.clear()
        self.goto(-230,270)
        self.write(f'Level: {self.current_level}',False,  ALIGN, FONT)
    
    def render_game_over(self):
        self.home()
        self.write('GAME OVER',False,  ALIGN, FONT)
