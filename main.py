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
import math
from pygame.locals import (
    K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN, QUIT, RESIZABLE
)
from map import Map
from conf import BACKGROUND_IMG, BLACK, BLUE, CAPTION, CELL_SIZE_PX, elmt_val, GREEN, MAP_FILE, maze_draw, MAZE_SIZE_TIL, WHITE

# Constant calculation
GAME_KEYS = [K_UP, K_DOWN, K_RIGHT, K_LEFT]
WINDOW_SIZE_PX_H = CELL_SIZE_PX * MAZE_SIZE_TIL
WINDOW_SIZE_PX_V = WINDOW_SIZE_PX_H + (2 * CELL_SIZE_PX)
WIN_DIM = (WINDOW_SIZE_PX_H, WINDOW_SIZE_PX_V)
FONT_SIZE = math.floor(0.9 * CELL_SIZE_PX)

pygame.init()
WINDOW = pygame.display.set_mode(WIN_DIM, RESIZABLE)
pygame.display.set_caption(CAPTION)
WINDOW.blit(pygame.image.load(BACKGROUND_IMG).convert(), (0, (2 * CELL_SIZE_PX)))

# Loading map
MAP_GAME = Map(MAP_FILE)

# Header messaging
h_msg = MAP_GAME.status_message.splitlines()
FONT = pygame.font.Font(None, FONT_SIZE)
h1_txt = FONT.render(h_msg[0], True, WHITE, BLACK)
h2_txt = FONT.render(h_msg[1], True, WHITE, BLACK)
WINDOW.blit(h1_txt, (0, 0))
WINDOW.blit(h2_txt, (0, CELL_SIZE_PX))

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
