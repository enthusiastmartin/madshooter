import logging

from application.constants import WIDTH
from application.core.entities import Enemy


class Level01(object):
    def __init__(self):
        self._entities = []

    def setup(self):
        max = (WIDTH - 100) // 50

        for idx in range(0,max):
            self._entities.append(Enemy(x=50+idx*50))

    @property
    def entities(self):
        return self._entities
