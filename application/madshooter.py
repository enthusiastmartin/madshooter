import pygame

from application.constants import WIDTH, HEIGHT, APPLICATION_TITLE

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(APPLICATION_TITLE)
clock = pygame.time.Clock()

from application.game import Game

game = Game(screen, clock)
game.setupLevel()

game.run()

pygame.quit()
