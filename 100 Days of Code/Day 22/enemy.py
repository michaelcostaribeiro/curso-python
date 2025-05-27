from paddle import Paddle

class Enemy(Paddle):
    def __init__(self):
        super().__init__()
        self.teleport(280,0)
        self.speed(1.1)
        self.up()
        self.direction = 'up'

    def move_up(self):
        self.goto(self.xcor(), self.ycor()+30)
        

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-30)
    
    def auto_move(self, direction):
        if direction == 'up':
            self.move_up()
            if self.ycor()>260:
                self.direction = 'down'
        elif direction == 'down':
            self.move_down()
            if self.ycor()<-260:
                self.direction = 'up'
