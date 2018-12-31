import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
class Paddle(pygame.sprite.Sprite):
    def __init__(self, player_number):

        ### Creating the paddle ###

        pygame.sprite.Sprite.__init__(self)

        self.player_number = player_number
        self.image = pygame.Surface([10, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.speed = 8
        self.buscado = None

        ### Establishing the location of each paddle ##

        if self.player_number == 1:
            self.rect.centerx = 0
            self.rect.centerx += 50
        elif self.player_number == 2:
            self.rect.centerx = 1024
            self.rect.centerx -= 50
        self.rect.centery = 300
        self.x = self.rect.centerx
        self.y = self.rect.centery

    def move(self,movimiento):

        if self.player_number == 1:
            if (movimiento == 1) and (self.rect.y > 5):
                self.rect.y -= self.speed
                self.y -= self.speed
            elif (movimiento == 0) and (self.rect.bottom < 600 - 5):
                self.rect.y += self.speed
                self.y += self.speed

        if self.player_number == 2:
            if (movimiento == 1) and (self.rect.y > 5):
                self.rect.y -= self.speed
            elif (movimiento == 0) and (self.rect.bottom < 600 - 5):
                self.rect.y += self.speed
