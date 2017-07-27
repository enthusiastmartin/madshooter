import pygame
from os import path

from application.config import img_dir
from application.constants import WIDTH, HEIGHT
from application.core.levels.baselevel import BaseLevel


class Level02(BaseLevel):
    def __init__(self):
        self._background_img = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()

        self._background = pygame.transform.scale(self._background_img, (WIDTH, HEIGHT))

        self._w, self._h = self._background.get_size()

        self._x = self._y = 0
        self._x1 = 0
        self._y1 = -self._h

    def setup(self):
        pass

    def update(self, screen=None):
        screen.blit(self._background, self._background.get_rect())

        self._y1 += 1
        self._y += 1
        screen.blit(self._background, (self._x, self._y))
        screen.blit(self._background, (self._x1, self._y1))
        if self._y > self._h:
            self._y = -self._h
        if self._y1 > self._h:
            self._y1 = -self._h
