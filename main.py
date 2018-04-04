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
    K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN, QUIT
)
from map import Map
from conf import (
    BACKGRND_FILE, CAPTION, MAP_FILE, HEAD_SIZE_H, maze_draw,
    MSG_END, MSG_QUIT, set_header, WIN_DIM
)

GAME_KEYS = [K_UP, K_DOWN, K_RIGHT, K_LEFT]
last_message = False  # Do not execute last message loop

# Loading map
MAP_GAME = Map(MAP_FILE)

if MAP_GAME.status:
    pygame.init()
    pygame.time.Clock().tick(25)
    pygame.display.set_caption(CAPTION)
    WINDOW = pygame.display.set_mode(WIN_DIM)
    WINDOW.blit(pygame.image.load(BACKGRND_FILE).convert(), (0, HEAD_SIZE_H))

# Game loop
while MAP_GAME.status:
    set_header(WINDOW, MAP_GAME.status_message)
    maze_draw(WINDOW, MAP_GAME.map_print())
    for event in pygame.event.get():
        if event.type == QUIT:
            MAP_GAME.status = False
            last_message = False

        if event.type == KEYDOWN:
            last_message = True  # Execute last_message loop
            if event.key in GAME_KEYS:
                MAP_GAME.move_to(event.key)

            else:
                MAP_GAME.status_message['status'] = MSG_QUIT
                MAP_GAME.status = False

# Allows reading the last_message (won, lost or quit)
while last_message:
    MAP_GAME.status_message['title'] = MSG_END
    set_header(WINDOW, MAP_GAME.status_message)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            last_message = False
