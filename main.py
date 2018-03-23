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
from os import system
import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN, QUIT, RESIZABLE
)
from map import Map, MAZE_ELEMENTS, MAZE_SIZE

# Configuration
CELL_SIZE_PX = 30

MAZE_ELEMENTS_TILES = {
    'wall': 'img/transp-30.png',
    'exit': 'img/g-orange-transp-30.png',
    'plyr': 'img/player-30.png',
    'void': 'img/blue-white-30.png'
}
BACKGROUND_IMG = 'img/brick-800.png'
UNKNOWN_TILE = 'img/unknown-30.png'
MAP_FILE = '01.map'

MAZE_SIZE_CEL = MAZE_SIZE
GAME_KEYS = [K_UP, K_DOWN, K_RIGHT, K_LEFT]
WINDOW_SIZE_PX = CELL_SIZE_PX * MAZE_SIZE_CEL

def maze_draw():
    """ Take a map string and generate a graphic maze """
    back_tiles = []
    for cell, element in enumerate(MAP_GAME.map_print().replace('\n', '')):
        key = [key for (key, val) in MAZE_ELEMENTS.items() if val == element][0]

        if key in MAZE_ELEMENTS_TILES:
            back_tiles.append(
                pygame.image.load(MAZE_ELEMENTS_TILES[key]).convert_alpha()
            )

        else:
            back_tiles.append(pygame.image.load(UNKNOWN_TILE).convert())

        x = (cell % MAZE_SIZE_CEL) * CELL_SIZE_PX
        y = (cell // MAZE_SIZE_CEL) * CELL_SIZE_PX
        WINDOW.blit(back_tiles[cell], (x, y))

    # Refresh
    pygame.display.flip()

pygame.init()

WINDOW = pygame.display.set_mode(
    (WINDOW_SIZE_PX, WINDOW_SIZE_PX), RESIZABLE
)
BACKGROUND = pygame.image.load(BACKGROUND_IMG).convert()
WINDOW.blit(BACKGROUND, (0, 0))

# Loading map
MAP_GAME = Map(MAP_FILE)

# Draw maze
maze_draw()

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

            # system('clear')
            print("status_message:{}".format(MAP_GAME.status_message))
            # MAP_GAME.map_print()

            # Draw maze
            maze_draw()
