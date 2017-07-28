import pygame

from application.constants import BLACK
from application.core.collider import collide_and_kill, player_collide
from application.core.entities import Player
from application.core.entities.explosion import Explosion
from application.core.levels.level01 import Level01
from application.core.levels.level02 import Level02
from application.core.menu import display_main_menu
from application.groups import all_sprites, enemy_group, bullets_group, enemy_bullet_group, reset_groups


class Game(object):
    def __init__(self, screen, clock):

        self.current_level = None

        self.clock = clock
        self.screen = screen



        self._display_menu = True

    def setupLevel(self):
        self.current_level = Level01()
        self.current_level.setup()

        all_sprites.add(self.current_level.entities)
        enemy_group.add(self.current_level.entities)

    def _reset(self):
        self.player = Player()

        reset_groups()
        all_sprites.add(self.player)

        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

    def run(self):

        running = True

        while running:
            if self._display_menu:
                display_main_menu(self.screen)
                self._reset()
                self.setupLevel()
                self._display_menu = False

            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break

            self.current_level.update(screen=self.screen)

            self.handle_bullets()

            self.handle_enemy_bulltets()

            all_sprites.update()

            all_sprites.draw(self.screen)

            pygame.display.flip()

            self._display_menu = not self.player.is_alive()

    @staticmethod
    def handle_bullets():
        hits = collide_and_kill(bullets_group, enemy_group)
        for hit in hits:
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)

    def handle_enemy_bulltets(self):
        hits = player_collide(self.player, enemy_bullet_group)
        for bullet in hits:
            expl = Explosion(bullet.rect.center, 'lg')
            self.player.player_hit(bullet)
            all_sprites.add(expl)
