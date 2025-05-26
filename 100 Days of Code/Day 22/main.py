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


board = Scoreboard(True)
player_score = Scoreboard(False)
enemy_score = Scoreboard(False)

player_score.render_score('user', 0)
enemy_score.render_score('enemy', 2)

enemy = Enemy()
user = User()
ball = Ball()


while True:
    enemy.auto_move()
    ball.move()
    ball.detect_miss()
    ball.detect_paddle(user)
    ball.detect_paddle(enemy)

screen.exitonclick()