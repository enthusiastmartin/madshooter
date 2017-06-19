import pygame

from application.constants import WIDTH, HEIGHT
from application.core.assets import enemy_img


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x=WIDTH/2, y = 50):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(enemy_img, (50, 38))
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        pass
