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
from gui import GraphUI
from conf import MAZE_FILE, MSG_END, MSG_QUIT

GAME_KEYS = [K_UP, K_DOWN, K_RIGHT, K_LEFT]
last_message = False  # Do not execute last message loop

# initialize maze with file
game_maze = Maze(MAZE_FILE)

# Running graphic user interface & initialize player
if game_maze.status:
    macgyver = Player(game_maze)
    gui = GraphUI()

# Game loop
while game_maze.status:
    gui.set_header(macgyver.status_message)
    gui.draw(game_maze)
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
    gui.set_header(macgyver.status_message)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            last_message = False
