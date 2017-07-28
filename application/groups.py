import pygame

bullets_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


def reset_groups():
    for b in bullets_group:
        b.kill()

    for e in enemy_bullet_group:
        e.kill()

    for e in enemy_group:
        e.kill()

    for a in all_sprites:
        a.kill()
