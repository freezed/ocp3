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
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN, QUIT
from map import Map

pygame.init()
SCREEN = pygame.display.set_mode((100, 100))

MAP_FILE = '01.map'
GAME_KEYS = [K_UP, K_DOWN, K_RIGHT, K_LEFT]

# Loading map
MAP_GAME = Map(MAP_FILE)

system('clear')
print(MAP_GAME.status_message)
MAP_GAME.map_print()

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

            system('clear')
            print("status_message:{}".format(MAP_GAME.status_message))
            MAP_GAME.map_print()