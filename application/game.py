import pygame

from application.constants import BLACK
from application.core.collider import collide_and_kill, player_collide
from application.core.entities import Player
from application.core.entities.explosion import Explosion
from application.core.levels.level01 import Level01
from application.groups import all_sprites, enemy_group, bullets_group, enemy_bullet_group


class Game(object):
    def __init__(self, screen, clock):
        self.player = Player()
        all_sprites.add(self.player)

        self.current_level = None

        self.clock = clock
        self.screen = screen

        self.player_group = pygame.sprite.Group()

        self.player_group.add(self.player)

    def setupLevel(self):
        self.current_level = Level01()
        self.current_level.setup()

        all_sprites.add(self.current_level.entities)
        enemy_group.add(self.current_level.entities)

    def run(self):
        running = True

        while running:

            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.handle_bullets()

            self.handle_enemy_bulltets()

            self.screen.fill(BLACK)

            all_sprites.update()

            all_sprites.draw(self.screen)

            pygame.display.flip()

            running = self.player.is_alive()

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


