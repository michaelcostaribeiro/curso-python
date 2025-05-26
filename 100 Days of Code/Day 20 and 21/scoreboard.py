from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 20, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.ht()
        self.color('white')
        self.goto(0,260)
        self.score = 0
        self.write(f'Score: {self.score}',False ,ALIGN,FONT)

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.goto(0,260)
        self.write(f'Score: {self.score}',False, ALIGN,FONT)
        