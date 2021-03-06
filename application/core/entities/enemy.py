from random import randint, seed

import pygame

from application.constants import WIDTH, HEIGHT
from application.core.assets import enemy_img, ship_sheet
from application.core.collider import add_bullet, add_enemy_bullet
from application.core.entities.bullet import Bullet


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x=WIDTH/2, y = 50):
        pygame.sprite.Sprite.__init__(self)

        self.image = ship_sheet.image_at((0,0,16,40))
        self.image = pygame.transform.scale(self.image, (38,50))

        #self.image = pygame.transform.scale(enemy_img, (50, 38))
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = x
        self.rect.bottom = y

        self.attack_speed = 1

        self.update_tick = pygame.time.get_ticks()
        self.last_shot = self.update_tick
        self.shot_delay= 1250

        seed(self.rect.centerx)

    def update(self):
        self.update_tick = pygame.time.get_ticks()
        self.rect.bottom += self.attack_speed

        # NOTE: this random shoot only until there is time to implement something better

        if randint(0,50) == 6:
            self.shoot()

    def shoot(self):
        #now = pygame.time.get_ticks()
        if self.update_tick - self.last_shot > self.shot_delay:
            self.last_shot = self.update_tick

            bullet = Bullet(self.rect.centerx, self.rect.bottom, 10)

            add_enemy_bullet(bullet)
