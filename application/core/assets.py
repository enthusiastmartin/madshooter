from os import path

import pygame

from application.config import img_dir

player_img = pygame.image.load(path.join(img_dir, 'player.png')).convert()
enemy_img = pygame.image.load(path.join(img_dir, 'enemy.png')).convert()
