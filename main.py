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
from maze import Maze
from player import Player
from conf import (
    BACKGRND_FILE, CAPTION, MAZE_FILE, HEAD_SIZE_H, maze_draw,
    MSG_END, MSG_QUIT, set_header, WIN_DIM
)

GAME_KEYS = [K_UP, K_DOWN, K_RIGHT, K_LEFT]
last_message = False  # Do not execute last message loop

# initialize maze and player
game_maze = Maze(MAZE_FILE)
macgyver = Player(game_maze)

if game_maze.status:
    pygame.init()
    pygame.time.Clock().tick(25)
    pygame.display.set_caption(CAPTION)
    WINDOW = pygame.display.set_mode(WIN_DIM)
    WINDOW.blit(pygame.image.load(BACKGRND_FILE).convert(), (0, HEAD_SIZE_H))

# Game loop
while game_maze.status:
    set_header(WINDOW, macgyver.status_message)
    maze_draw(WINDOW, game_maze.maze_print())
    for event in pygame.event.get():
        if event.type == QUIT:
            game_maze.status = False
            last_message = False

        if event.type == KEYDOWN:
            last_message = True  # Execute last_message loop
            if event.key in GAME_KEYS:
                macgyver.move_to(event.key)

            else:
                macgyver.status_message['status'] = MSG_QUIT
                game_maze.status = False

# Allows reading the last_message (won, lost or quit)
while last_message:
    macgyver.status_message['title'] = MSG_END
    set_header(WINDOW, macgyver.status_message)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            last_message = False
