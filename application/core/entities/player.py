import pygame

from application.constants import WIDTH, HEIGHT
from application.core.assets import player_img
from application.core.entities.bullet import Bullet

from application.core.collider import add_bullet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(player_img, (50, 38))

        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

        self.speedx = 0

        now = pygame.time.get_ticks()
        self.last_shot = now
        self.shot_delay= 250

    def update(self):
        keystate = pygame.key.get_pressed()

        self.speedx = 0
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 5

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.x += self.speedx

        if keystate[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shot_delay:
            self.last_shot = now

            bullet = Bullet(self.rect.centerx, self.rect.top)

            add_bullet(bullet)
