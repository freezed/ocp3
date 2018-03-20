#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: freezed <freezed@users.noreply.github.com> 2018-03-15
Version: 0.1

Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [_ocp3_ project](https://github.com/freezed/ocp3)
"""

import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN, QUIT, RESIZABLE
)

MAZE_SIZE_CEL = 15
CELL_SIZE_PX = 50
BACK_TILE_IMG = 'img/blue-transp-50.png'
PLAYER_TILE_IMG = 'img/player-50.png'
WINDOW_SIZE_PX = CELL_SIZE_PX * MAZE_SIZE_CEL

pygame.init()

WINDOW = pygame.display.set_mode(
    (WINDOW_SIZE_PX, WINDOW_SIZE_PX),
    RESIZABLE
)

GRID = range(MAZE_SIZE_CEL ** 2)
back_tiles = []
for cell in GRID:
    back_tiles.append(pygame.image.load(BACK_TILE_IMG).convert())
    x = (cell % MAZE_SIZE_CEL) * CELL_SIZE_PX
    y = (cell // MAZE_SIZE_CEL) * CELL_SIZE_PX
    WINDOW.blit(back_tiles[cell], (x, y))

PLAYER = pygame.image.load(PLAYER_TILE_IMG).convert_alpha()
player_pos = PLAYER.get_rect()

# Player position
WINDOW.blit(PLAYER, player_pos)

# Refresh
pygame.display.flip()

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                player_pos = player_pos.move(0, CELL_SIZE_PX)

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player_pos = player_pos.move(-CELL_SIZE_PX, 0)

        if event.type == KEYDOWN:
            if event.key == K_UP:
                player_pos = player_pos.move(0, -CELL_SIZE_PX)

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player_pos = player_pos.move(CELL_SIZE_PX, 0)

    # New player position
    # WINDOW.blit(back_tiles, (0,0))
    WINDOW.blit(PLAYER, player_pos)

    # Refresh
    pygame.display.flip()
