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
from conf import BACKGROUND_IMG, CAPTION, MAP_FILE, HEADER_HEIGHT, maze_draw, MSG_END, MSG_QUIT, set_header, WIN_DIM

# Constant calculation
GAME_KEYS = [K_UP, K_DOWN, K_RIGHT, K_LEFT]

pygame.init()
WINDOW = pygame.display.set_mode(WIN_DIM, RESIZABLE)
pygame.display.set_caption(CAPTION)
WINDOW.blit(pygame.image.load(BACKGROUND_IMG).convert(), (0, HEADER_HEIGHT))

# Loading map
MAP_GAME = Map(MAP_FILE)

# Header messaging
set_header(WINDOW, MAP_GAME.status_message)

# Draw maze
maze_draw(WINDOW, MAP_GAME.map_print().replace('\n', ''))

pygame.time.Clock().tick(25)
# Game loop
last_wait = True
while MAP_GAME.status:
    for event in pygame.event.get():
        if event.type == QUIT:
            MAP_GAME.status = False
            last_wait = False

        if event.type == KEYDOWN:
            if event.key in GAME_KEYS:
                MAP_GAME.move_to(event.key)

            else:
                MAP_GAME.status_message['status'] = MSG_QUIT
                MAP_GAME.status = False

            set_header(WINDOW, MAP_GAME.status_message)
            # Draw maze
            maze_draw(WINDOW, MAP_GAME.map_print().replace('\n', ''))

MAP_GAME.status_message['title'] = MSG_END
set_header(WINDOW, MAP_GAME.status_message)
pygame.display.flip()

while last_wait:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            last_wait = False
