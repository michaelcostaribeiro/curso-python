from config import MOVE_DISTANCE
import scoreboard as score
import snake as s
from turtle import Screen
import food as f
import time


screen = Screen()
snake = s.Snake()
screen.setup(s.SCREEN_X,s.SCREEN_Y)
screen.bgcolor('black')
screen.title('Snake Game')


screen.onkey(snake.move_up,'Up')
screen.onkey(snake.move_left,'Left')
screen.onkey(snake.move_down,'Down')
screen.onkey(snake.move_right,'Right')
screen.listen()
screen.tracer(0)

game_over = False
food = f.Food()
scoreboard = score.Scoreboard()

while not game_over:
    screen.update()
    time.sleep(.1)


    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.body.append(s.SnakeBlock())
        scoreboard.refresh_score()
    
    
    if s.wall_check(snake.head):
        game_over = s.wall_check(snake.head)
    if s.body_check(snake.body):
        game_over = s.body_check(snake.body)

    
    


screen.exitonclick()
