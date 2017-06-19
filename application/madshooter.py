import pygame

from application.constants import WIDTH, HEIGHT, BLACK, APPLICATION_TITLE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(APPLICATION_TITLE)
clock = pygame.time.Clock()

# Groups
bullets_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Player
from application.core.entities import Player
player = Player()
all_sprites.add(player)

# Load first Level
from application.core.levels.level01 import Level01
level = Level01()
level.setup()

all_sprites.add(level.entities)

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

    screen.fill(BLACK)

    all_sprites.update()

    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
