import pygame

from application.constants import WIDTH, HEIGHT, BLACK, APPLICATION_TITLE

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

from application.core.entities import *

pygame.display.set_caption(APPLICATION_TITLE)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

enemy = Enemy()

all_sprites.add(enemy)

running = True

while running:
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
