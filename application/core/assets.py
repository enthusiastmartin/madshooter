from os import path

import pygame

from application.config import img_dir
from application.constants import BLACK
from application.core.spritesheet import SpriteSheet

ship_sheet_img = path.join(img_dir+"/ships", 'ships_saucer.png')
ship_sheet = SpriteSheet(ship_sheet_img)

player_img = pygame.image.load(path.join(img_dir, 'player.png')).convert()
enemy_img = pygame.image.load(path.join(img_dir, 'enemy.png')).convert()

laser_green_img = pygame.image.load(path.join(img_dir,'laserGreen.png')).convert()

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    ## resize the explosion
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)

    ## player explosion
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)

