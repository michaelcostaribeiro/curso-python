from config import MOVE_DISTANCE
import turtle as t

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

SCREEN_X = 600
SCREEN_Y = 600

class Snake():
    def __init__(self):
        self.body = [SnakeBlock(),SnakeBlock(),SnakeBlock()]
        self.head = self.body[0].block
        self.body[0].block.color('white')
    
    def move(self):
        for i in range(len(self.body)-1, 0, -1):  
            new_x_cor = self.body[i-1].block.xcor()
            new_y_cor = self.body[i-1].block.ycor()
            self.body[i].block.goto(new_x_cor, new_y_cor)
            if self.body[i].block.pencolor() == 'black':
                self.body[i].block.color('white')
        self.head.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


class SnakeBlock():
    def __init__(self):
        self.block = t.Turtle('square')
        self.block.color('black')
        self.block.turtlesize(1,1)
        self.block.up()
    
def wall_check(snake_head):
    if snake_head.pos()[0] >= SCREEN_X/2 or snake_head.pos()[0] <= SCREEN_X/2*-1:
        return True
    elif snake_head.pos()[1] >= SCREEN_Y/2 or snake_head.pos()[1] <= SCREEN_Y/2*-1:
        return True
    else:
        return False

def body_check(snake_body):
    for i in range(1,len(snake_body)):
        if snake_body[0].block.pos() == snake_body[i].block.pos():
            return True
    return False


