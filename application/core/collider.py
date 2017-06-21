import pygame

from application.groups import all_sprites, bullets_group


def add_bullet(bullet):
    all_sprites.add(bullet)
    bullets_group.add(bullet)


def collide_and_kill( group1, group2 ):
    return pygame.sprite.groupcollide(group1, group2, True, True)