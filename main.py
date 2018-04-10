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
last_message = False  # do not execute last message loop

# initialize maze with file
GAME_MAZE = Maze(MAZE_FILE)

# running graphic user interface & initialize player
if GAME_MAZE.status:
    MACGYVER = Player(GAME_MAZE)
    GUI = GraphUI()
    GUI.draw(GAME_MAZE, MACGYVER.status_message)

# game loop
while GAME_MAZE.status:
    for event in pygame.event.get():
        if event.type == QUIT:
            GAME_MAZE.status = False
            last_message = False

        if event.type == KEYDOWN:
            last_message = True  # executes last_message loop
            if event.key in GAME_KEYS:
                MACGYVER.key_event(event.key)
                GUI.set_header(MACGYVER.status_message)
                GUI.update(MACGYVER)

            else:
                MACGYVER.status_message['status'] = MSG_QUIT
                GAME_MAZE.status = False


# displays the last_message (won, lost or quit)
while last_message:
    MACGYVER.status_message['title'] = MSG_END
    GUI.set_header(MACGYVER.status_message)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            last_message = False
