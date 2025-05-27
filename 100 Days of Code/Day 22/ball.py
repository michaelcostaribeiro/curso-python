from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.up()
        self.shape('circle')
        self.left(60)
        self.speed('fast')
        self.shapesize(.75)
        self.window = Screen()
        self.WINDOW_HEIGHT = self.window.window_height()/2
        self.WINDOW_WIDTH = self.window.window_width()/2

    def move(self):
        if self.ycor()> self.WINDOW_HEIGHT-5 or self.ycor()< self.WINDOW_HEIGHT*-1+5:
            self.setheading(self.heading()-90)
            self.forward(20)   
        self.forward(20)
    
    def detect_paddle(self, paddle):
        if self.distance(paddle)<50 and self.xcor() > 260:
            self.setheading(self.heading()-120)
        elif self.distance(paddle)<50 and self.xcor() < -260:
            self.setheading(self.heading()-120)
    
    def detect_miss(self):
        if self.xcor() > 360:
            self.home()
            self.setheading(180)
            return 'user_point'
        if self.xcor() < -360:
            self.home()
            self.setheading(0)
            return 'enemy_point'
        
