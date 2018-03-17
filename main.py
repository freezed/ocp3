#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-03-17
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/
"""
import pygame
from map import Map
from pygame.locals import KEYDOWN, K_ESCAPE, QUIT, K_DOWN, K_LEFT, K_UP, K_RIGHT

pygame.init()
screen = pygame.display.set_mode((100, 100))
# Variables
MAP_FILE = '01.map'

# Class
MAP_GAME = Map(MAP_FILE)
print(MAP_GAME.status)
print(MAP_GAME.status_message)

# Loading map
MAP_GAME.map_print()

# Event loop
game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_on = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_on = False

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                print('down')

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                print('left')

        if event.type == KEYDOWN:
            if event.key == K_UP:
                print('up')

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                print('right')
