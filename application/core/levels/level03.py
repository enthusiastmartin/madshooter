import pygame

from os import path
import time

from application.config import img_dir
from application.constants import WIDTH, HEIGHT
from application.core.entities import Enemy
from application.core.levels.baselevel import BaseLevel
from application.groups import add_enemy


class Level03(BaseLevel):
    def __init__(self):
        self._background_img = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
        self._background = pygame.transform.rotate(self._background_img, 90)
        self._background = pygame.transform.scale(self._background, (WIDTH, HEIGHT))

        self._w, self._h = self._background.get_size()

        self._x = self._y = 0
        self._x1 = 0
        self._y1 = -self._h

        self._level_time = 20 * 1000  # milliseconds

    def setup(self):
        self._enemies = []
        self._enemies.append({'time': 1000, 'enemy': Enemy(x=150, y=0)})
        self._enemies.append({'time': 6500, 'enemy': Enemy(x=450, y=0)})

        self._start_time = time.time() * 1000.0

    def update(self, screen=None):

        # Update background
        if screen:
            self._update_background(screen)

        # now = pygame.time.get_ticks()
        now = time.time() * 1000.0
        diff = now - self._start_time

        now = diff

        if now > self._level_time:
            pass

        if len(self._enemies) > 0:
            if self._enemies[0]['time'] <= now:
                add_enemy(self._enemies[0]['enemy'])
                del self._enemies[0]

    def _update_background(self, screen):
        screen.blit(self._background, self._background.get_rect())
        self._y1 += 1
        self._y += 1
        screen.blit(self._background, (self._x, self._y))
        screen.blit(self._background, (self._x1, self._y1))
        if self._y > self._h:
            self._y = -self._h
        if self._y1 > self._h:
            self._y1 = -self._h
