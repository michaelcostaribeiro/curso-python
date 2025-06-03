from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 20, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.ht()
        self.color('white')
        self.goto(-120,260)
        self.score = 0
        self.highest_score = self.get_highest_score()
        self.write(f'Score: {self.score}',False ,ALIGN,FONT)
        self.goto(120,260)
        self.write(f'Highest score: {self.highest_score}',False ,ALIGN,FONT)

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.goto(-120,260)
        self.write(f'Score: {self.score}',False, ALIGN,FONT)
        if self.score > self.highest_score:
            self.update_highest_score(self.score)
            self.highest_score = self.get_highest_score()
        self.goto(120,260)
        self.write(f'Highest score: {self.highest_score}',False ,ALIGN,FONT)


    def get_highest_score(self):
        with open ('highest_score.txt', 'r+') as file:
            return int(file.read().split()[-1])
    
    def update_highest_score(self, number):
        current_number = self.get_highest_score()
        if number > current_number:
            with open('highest_score.txt', 'w') as file:
                file.write(f'highest_score is {number}')
