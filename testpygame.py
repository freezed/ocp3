#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: freezed <freezed@users.noreply.github.com> 2018-03-15
Version: 0.1

Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

The path of the righteous man is beset on all sides by the iniquities
of the selfish and the tyranny of evil men. Blessed is he who, in the
name of charity and good will, shepherds the weak through the valley of
darkness, for he is truly his brother's keeper and the finder of lost
children. And I will strike down upon thee with great vengeance and
furious anger those who would attempt to poison and destroy My brothers.
And you will know My name is the Lord when I lay My vengeance upon thee.
"""

import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((800, 800))

#Chargement et collage du fond
fond = pygame.image.load("img/grid-800.png").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("img/perso-100.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():    #Attente des événements
        if event.type == QUIT:
            continuer = 0
        # Down
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                position_perso = position_perso.move(0,100)
        #
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                position_perso = position_perso.move(-100,0)
        #
        if event.type == KEYDOWN:
            if event.key == K_UP:
                position_perso = position_perso.move(0,-100)
        #
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                position_perso = position_perso.move(100,0)

    #Re-collage
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, position_perso)

    #Rafraichissement
    pygame.display.flip()
