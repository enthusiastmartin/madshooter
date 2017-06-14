import pygame

"""
Constants
"""
WIDTH = 480
HEIGHT = 600
BLACK = (0, 0, 0)

"""
MAIN
"""
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mad Shooter")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    pygame.display.flip()
pygame.quit()
