import sys, time,math
from random import randint
from PyPong.paddle import Paddle
from PyPong.ball import Ball
SCORE_GANAR = 1
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 600
### Paddle Stuff ###

PADDLE_SPEED = 10

UP1 = False
DOWN1 = False
NO_MOVEMENT1 = True
UP2 = False
DOWN2 = False
NO_MOVEMENT2 = True

### Ball Stuff ###

UPLEFT = 0
DOWNLEFT = 1
UPRIGHT = 2
DOWNRIGHT = 3
player1_win = False
player2_win = False

### colors ###
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
main_surface = None
surface_rect = None

def run(player,angulo):
    global main_surface
    global surface_rect
    global UP1
    global DOWN1
    global NO_MOVEMENT1
    global UP2
    global DOWN2
    global NO_MOVEMENT2
    global player1_win
    global player2_win
    respuestas = 0
    start = time.time()
    paddle1 = Paddle(1)
    paddle2 = Paddle(2)
    ball = Ball(angulo=angulo)

    player1_score = 0
    player2_score = 0
    abajo = None
    arriba = None
    counter = 0
    respuestas = 0
    while True:

        if ( (paddle2.buscado ==None or paddle2.buscado) and ball.rect.x > WINDOW_WIDTH - 60):
            # esto porque jugador 2 no esta activado
            if (ball.direccion > 0 and ball.direccion < 0.25):
                ball.change_direction(change=True)
            else:
                ball.change_direction()
            #ball.speed += 1
            paddle1.buscado = True
            paddle2.buscado = False

        elif (ball.rect.x < 0):
            ball.reset()

        ball.move()
        # calcular si se mueve
        paddle1.move(player.movimiento([paddle1.y/600.0,ball.x/1024.0,ball.y/600.0,ball.direccion]))
        if(ball.colision(paddle1)):
            player.agregarDistancia(abs(ball.y - paddle1.y))
            player.agregarRespuesta()
            respuestas += 1
            paddle2.buscado = True

        if( ball.colision(paddle2)):
            paddle1.buscado = True

        if ball.rect.x > WINDOW_WIDTH:
            player1_score += 1
        elif ball.rect.x < 0:
            player.agregarDistancia(abs(ball.y - paddle1.y))
            player2_score += 1

        if player1_score == 5:
            player1_win = True
            break
        elif player2_score == SCORE_GANAR:
            player2_win = True
            break
        if respuestas == 2:
            break

        counter += 1
    return respuestas



