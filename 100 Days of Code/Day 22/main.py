from turtle import Screen
from scoreboard import Scoreboard
from user import User
from enemy import Enemy
from ball import Ball
import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

board = Scoreboard(True)
player_score = Scoreboard(False)
enemy_score = Scoreboard(False)

player_score.render_score('user', player_score.score)
enemy_score.render_score('enemy', enemy_score.score)

enemy = Enemy()
user = User()
ball = Ball()


while True:
    screen.update()
    time.sleep(0.05)
    enemy.auto_move(enemy.direction)
    ball.move()
    point = ball.detect_miss()
    if point == 'user_point':
        player_score.score += 1
        player_score.render_score('user', player_score.score)
    if point == 'enemy_point':
        enemy_score.score += 1
        enemy_score.render_score('enemy', enemy_score.score)
    ball.detect_paddle(user)
    ball.detect_paddle(enemy)

screen.exitonclick()