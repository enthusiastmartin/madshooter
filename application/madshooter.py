import pygame

## assets folder
from os import path

img_dir = path.join(path.dirname(__file__), 'assets')

"""
Constants
"""
WIDTH = 480
HEIGHT = 600
BLACK = (0, 0, 0)

"""
PLAYER
"""


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

    def update(self):
        pass


"""
MAIN
"""
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mad Shooter")
running = True

player_img = pygame.image.load(path.join(img_dir, 'player.png')).convert()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

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
