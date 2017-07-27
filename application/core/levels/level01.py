
from application.constants import WIDTH, BLACK
from application.core.entities import Enemy
from application.core.levels.baselevel import BaseLevel


class Level01(BaseLevel):
    def __init__(self):

        self._enemies = []

    def setup(self):
        super()
        max = (WIDTH - 100) // 50

        for idx in range(0,max):
            self._enemies.append(Enemy(x=50+idx*50))

    def update(self, screen=None):
        if screen:
            screen.fill(BLACK)

    @property
    def entities(self):
        return self._enemies
