#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-03-17
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

Main file for [_ocp3_ project](https://github.com/freezed/ocp3)
See [README](https://github.com/freezed/ocp3/blob/master/README.md) for
details
"""
import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN, QUIT, RESIZABLE
)
from map import Map
from conf import BACKGROUND_IMG, CELL_SIZE_PX, elmt_val, MAP_FILE, maze_draw, MAZE_SIZE_TIL

# MAIN SCRIPT
GAME_KEYS = [K_UP, K_DOWN, K_RIGHT, K_LEFT]
WINDOW_SIZE_PX = CELL_SIZE_PX * MAZE_SIZE_TIL

pygame.init()

WINDOW = pygame.display.set_mode(
    (WINDOW_SIZE_PX, WINDOW_SIZE_PX + CELL_SIZE_PX), RESIZABLE
)
BACKGROUND = pygame.image.load(BACKGROUND_IMG).convert()
WINDOW.blit(BACKGROUND, (0, CELL_SIZE_PX))

# Loading map
MAP_GAME = Map(MAP_FILE)

# Draw maze
maze_draw(WINDOW, MAP_GAME.map_print().replace('\n', ''))

# system('clear')
print(MAP_GAME.status_message)
# MAP_GAME.map_print()

# Game loop
while MAP_GAME.status:
    for event in pygame.event.get():
        if event.type == QUIT:
            MAP_GAME.status = False

        if event.type == KEYDOWN:
            if event.key in GAME_KEYS:
                MAP_GAME.move_to(event.key)

            else:
                MAP_GAME.status = False

            print("status_message:{}".format(MAP_GAME.status_message))

            # Draw maze
            maze_draw(WINDOW, MAP_GAME.map_print().replace('\n', ''))
