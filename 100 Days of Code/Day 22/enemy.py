from paddle import Paddle

class Enemy(Paddle):
    def __init__(self):
        super().__init__()
        self.teleport(280,0)
        self.speed(1.1)
        self.up()
    
    def auto_move(self):
        if self.pos() == (280,0):
            self.goto(self.xcor(), 271)
        elif self.ycor()>270:
            self.goto(self.xcor(),-271)
        if self.ycor()<-270:
            self.goto(self.xcor(),271)