"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-11
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [_ocp3_ project](https://github.com/freezed/ocp3)
"""
from math import floor
import pygame

ELEMENTS = (
    {
        'symbol': 'n', 'name': 'needle', 'cross': True,
        'ressurect': False, 'collect': True, 'tile': 'img/3-30.png'
    },
    {
        'symbol': 't', 'name': 'tube', 'cross': True,
        'ressurect': False, 'collect': True, 'tile': 'img/1-30.png'
    },
    {
        'symbol': 'e', 'name': 'ether', 'cross': True,
        'ressurect': False, 'collect': True, 'tile': 'img/2-30.png'
    },
    {
        'symbol': 'E', 'name': 'exit', 'cross': False,
        'ressurect': False, 'collect': False, 'tile': 'img/g-30.png'
    },
    {
        'symbol': ' ', 'name': 'void', 'cross': True,
        'ressurect': True, 'collect': False, 'tile': 'img/void-30.png'
    },
    {
        'symbol': '.', 'name': 'wall', 'cross': False,
        'ressurect': False, 'collect': False, 'tile': 'img/wall-30.png'
    },
    {
        'symbol': 'X', 'name': 'player', 'cross': False,
        'ressurect': False, 'collect': False, 'tile': 'img/player-30.png'
    },
    {
        'symbol': '\n', 'name': 'nlin', 'cross': False,
        'ressurect': False, 'collect': False, 'tile': False
    },
)

CELL_SIZE = 30   # Size of the tiles, in pixels
MAZE_SIZE = 15   # Size of a map, in tiles
BLACK = (0, 0, 0)
BLUE = (0, 0, 128)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Messages
CAPTION = "OCP3, a maze based on pygame"
ERR_FILE = "Map filename is not avaiable:  «{}»"
ERR_LINE = "Map file has wrong lines number:  «{}»"
HEAD_MESSAGES = {
    'title': "Welcome in OCP3.",
    'status': "Use arrow keys to play, any other key to quit.",
    'items': "Items: {}/{}",
}
MSG_COLLECT = "You pick «{}»"
MSG_END = "End of game, press a key to quit."
MSG_LOSER = "You lose! You were missing: {}."
MSG_OK = "…"
MSG_QUIT = "You decide to quit the game"
MSG_WALL = "That's a wall!"
MSG_WINNER = "Cogratulations! You asleep the guard."

# Files
BACKGRND_FILE = 'img/back-800.png'
MAP_FILE = '01.map'
UNKNOWN_FILE = 'img/unknown-30.png'

# Constant calculation
FONT_SIZE = floor(0.9 * CELL_SIZE)
HEAD_SIZE_H = (2 * CELL_SIZE)
WIN_SIZE_W = CELL_SIZE * MAZE_SIZE
WIN_SIZE_H = WIN_SIZE_W + HEAD_SIZE_H
WIN_DIM = (WIN_SIZE_W, WIN_SIZE_H)


# FUNCTIONS


def elmt_val(kval, ksel, vsel, nline=False):
    """
    Return value(s) from ELEMENTS

    :param str kval: key of the value returned
    :param str ksel: key of the selection criteria
    :param str vsel: value of the selection criteria
    :param bool/int nline: Default False, return value(s) in a list,
    use a int() to return the `n` value from the list

    """
    try:
        if nline is False:
            return (element[kval] for element in ELEMENTS
                    if element[ksel] == vsel)
        else:
            return [element[kval] for element in ELEMENTS
                    if element[ksel] == vsel][nline]
    except IndexError:
        return False


def maze_draw(surface, map_string):
    """
    Take a map string and generate a graphic maze

    :param obj surface: a pygame surface object
    :param str map_string: map modelized in a string
    """
    back_tiles = []
    for cell, element in enumerate(map_string):
        img = elmt_val('tile', 'symbol', element, 0)

        if img is False:
            back_tiles.append(pygame.image.load(UNKNOWN_FILE).convert())
        else:
            back_tiles.append(pygame.image.load(img).convert_alpha())

        x = (cell % MAZE_SIZE) * CELL_SIZE
        y = (cell // MAZE_SIZE) * CELL_SIZE + HEAD_SIZE_H
        surface.blit(back_tiles[cell], (x, y))

    # Refresh
    pygame.display.flip()


def set_header(surface, messages):
    """
    Set the header message on the window

    :param obj surface: surface surfaceect
    :param list/str messages: list of messages per place
    """
    pygame.draw.rect(surface, BLACK, (0, 0, WIN_SIZE_W, HEAD_SIZE_H))

    FONT = pygame.font.Font(None, FONT_SIZE)

    h_title = FONT.render(messages['title'], True, BLUE, WHITE)
    h_status = FONT.render(messages['status'], True, WHITE, BLACK)
    h_items = FONT.render(messages['items'], True, GREEN, BLACK)

    h_items_pos = h_items.get_rect(topright=(WIN_SIZE_W, 0))

    surface.blit(h_title, (0, 0))
    surface.blit(h_status, (0, CELL_SIZE))
    surface.blit(h_items, h_items_pos)
