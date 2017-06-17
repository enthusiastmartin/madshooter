import pygame

from application.constants import WIDTH, HEIGHT
from application.core.assets import player_img


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(player_img, (50, 38))

        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

        self.speedx = 0

    def update(self):
        keystate = pygame.key.get_pressed()

        self.speedx = 0
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 5

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.x += self.speedx
