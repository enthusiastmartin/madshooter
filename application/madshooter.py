import random

import pygame

from application.constants import WIDTH, HEIGHT, BLACK, APPLICATION_TITLE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(APPLICATION_TITLE)
clock = pygame.time.Clock()

from application.core.collider import collide_and_kill

# Groups
from application.groups import bullets_group, enemy_group, all_sprites

from application.core.entities.explosion import Explosion

# Player
from application.core.entities import Player
player = Player()
all_sprites.add(player)

# Load first Level
from application.core.levels.level01 import Level01
level = Level01()
level.setup()

all_sprites.add(level.entities)

enemy_group.add(level.entities)

# Main
running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    hits = collide_and_kill(bullets_group, enemy_group)

    for hit in hits:
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)

    screen.fill(BLACK)

    all_sprites.update()

    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
