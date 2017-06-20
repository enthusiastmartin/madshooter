import pygame


def add_bullet(bullet):
    from application.madshooter import all_sprites, bullets_group
    all_sprites.add(bullet)
    bullets_group.add(bullet)


def collide_and_kill( group1, group2 ):
    return pygame.sprite.groupcollide(group1, group2, True, True)