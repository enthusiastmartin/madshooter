import pygame

from application.constants import BLACK
from application.core.assets import laser_green_img


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser_green_img
        self.image.set_colorkey(BLACK) # TODO: check this

        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = x
        self.rect.bottom = y

        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy

        if self.rect.bottom <= 0:
            self.kill()
