import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pendientes = []
from random import randint
import math
class Ball(pygame.sprite.Sprite):
    def __init__(self,angulo = 0.625):
        self.abajo = None
        self.arriba = None
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = 512
        self.rect.centery = 300
        self.x = 512
        self.y = 300
        self.speed = 30
        self.direccion_or = angulo
        self.direccion = angulo
        self.angulo = 2 * math.pi * self.direccion

    def actualizarAngulo(self):
        self.angulo = 2 * math.pi * self.direccion

    def reset(self):
        self.rect.centerx = 512
        self.rect.centery = 300
        self.x = 512
        self.y = 300
        self.speed = 4
        self.direccion = self.direccion_or
        self.angulo = 2 * math.pi * self.direccion

    def move(self):
        self.y += int(self.speed * math.cos(self.angulo))
        self.x += int(self.speed * math.sin(self.angulo))
        self.rect.x = self.x
        self.rect.y = self.y
        if(self.y >= 600  and (self.arriba == None or self.arriba == True)):
            if (self.direccion > 0.75 and self.direccion < 1):
                self.change_direction(change=True)
            else:
                self.change_direction()
            self.abajo = True
            self.arriba = False
        elif(self.y <= 0 and (self.abajo == None or self.abajo == True)):
            if(self.direccion > 0.25 and self.direccion < 0.5):
                self.change_direction(change = True)
            else:
                self.change_direction()
            self.abajo = False
            self.arriba = True


    def change_direction(self,change = False):
        if(change):
            self.direccion -= 0.25
        else:
            self.direccion += 0.25
        self.direccion = self.direccion % 1
        self.actualizarAngulo()

    def colision(self,paddle):
        if((paddle.buscado == None or paddle.buscado) and paddle.x + 5 > self.x and paddle.x - self.speed < self.x
                and paddle.y + 50 > self.y and paddle.y - 50 < self.y):
            self.speed += 1
            paddle.buscado = False
            if((self.direccion > 0 and self.direccion < 0.25) or (self.direccion > 0.5 and self.direccion < 0.75)):
                self.change_direction(change=True)
            else:
                self.change_direction()
            return True
        return False
