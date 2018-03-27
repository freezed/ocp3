"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-11
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [_ocp3_ project](https://github.com/freezed/ocp3)
"""
import pygame
import math

# CONFIGURATION
ELEMENT_LIST = [
    {'symbol': 'n', 'name': 'needle', 'cross': True, 'ressurect': False, 'collect': True, 'tile': 'img/3-blue-transp-30.png'},
    {'symbol': 't', 'name': 'tube', 'cross': True, 'ressurect': False, 'collect': True, 'tile': 'img/1-blue-transp-30.png'},
    {'symbol': 'e', 'name': 'ether', 'cross': True, 'ressurect': False, 'collect': True, 'tile': 'img/2-blue-transp-30.png'},
    {'symbol': 'E', 'name': 'exit', 'cross': False, 'ressurect': False, 'collect': False, 'tile': 'img/g-orange-transp-30.png'},
    {'symbol': ' ', 'name': 'void', 'cross': True, 'ressurect': True, 'collect': False, 'tile': 'img/blue-white-30.png'},
    {'symbol': '.', 'name': 'wall', 'cross': False, 'ressurect': False, 'collect': False, 'tile': 'img/transp-30.png'},
    {'symbol': 'X', 'name': 'player', 'cross': False, 'ressurect': False, 'collect': False, 'tile': 'img/player-30.png'},
    {'symbol': '\n', 'name': 'nlin', 'cross': False, 'ressurect': False, 'collect': False, 'tile': False},
]

# Possible returns of a move, keep the «ok» at the end
MOVE_STATUS = ['looser', 'wall', 'winner', 'collect', 'ok']
MOVE_STATUS_MSG = {
    'looser': "Vous vous êtes fait assommé! Pour endormir le garde, il manqait: {}.\nPerdu!",
    'wall': "Le déplacement est stoppé par un mur.",
    'winner': "Gagné! Vous avez endormis le garde avec votre seringue.",
    'collect': "Vous ramassez l'objet «{}»",
    'ok': "Jusqu'ici, tout va bien…"
}

CELL_SIZE_PX = 30   # Size of the tiles, in pixels
MAZE_SIZE_TIL = 15      # Size of a map, in tiles
FONT_SIZE = math.floor(0.9 * CELL_SIZE_PX)
BLACK = (0, 0, 0)
BLUE = (0, 0, 128)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Messages
CAPTION = "OCP3, a pygame maze"
ERR_MAP = "ERR_MAP: «{}»"
HEADER_MESSAGES = {
    'title': "Welcome in OCP3.",
    'status': "Use arrow keys to play, any other key to quit.",
    'items': "Items: {}/{}",
}
MSG_END = "End of game, press a key to quit."
MSG_QUIT = "You decide to quit the game"

# Files
BACKGROUND_IMG = 'img/zebra-800.png'
MAP_FILE = '01.map'
UNKNOWN_TILE = 'img/unknown-30.png'

# Constant calculation
HEADER_HEIGHT = (2 * CELL_SIZE_PX)
WINDOW_SIZE_PX_W = CELL_SIZE_PX * MAZE_SIZE_TIL
WINDOW_SIZE_PX_H = WINDOW_SIZE_PX_W + HEADER_HEIGHT
WIN_DIM = (WINDOW_SIZE_PX_W, WINDOW_SIZE_PX_H)


# FUNCTIONS


def elmt_val(kval, ksel, vsel, nline=False):
    """
    Return value(s) from ELEMENT_LIST

    :param str kval: key of the value returned
    :param str ksel: key of the selection criteria
    :param str vsel: value of the selection criteria
    :param bool/int nline: Default False, return value(s) in a list,
    use a int() to return the `n` value from the list

    :return str/bool/…:
    """
    try:
        if nline is False:
            return (element[kval] for element in ELEMENT_LIST if element[ksel] == vsel)
        else:
            return [element[kval] for element in ELEMENT_LIST if element[ksel] == vsel][nline]
    except IndexError:
        return False


def maze_draw(WINDOW, map_string):
    """ Take a map string and generate a graphic maze """
    back_tiles = []
    for cell, element in enumerate(map_string):
        img = elmt_val('tile', 'symbol', element, 0)

        if img is False:
            back_tiles.append(pygame.image.load(UNKNOWN_TILE).convert())
        else:
            back_tiles.append(pygame.image.load(img).convert_alpha())

        x = (cell % MAZE_SIZE_TIL) * CELL_SIZE_PX
        y = (cell // MAZE_SIZE_TIL) * CELL_SIZE_PX + HEADER_HEIGHT
        WINDOW.blit(back_tiles[cell], (x, y))

    # Refresh
    pygame.display.flip()


def set_header(WINDOW, messages):
    """
    Set the header message on the window

    :param obj WINDOWS: display object
    :param list/str messages: list of messages per place
    """
    pygame.draw.rect(WINDOW, BLACK, (0, 0, WINDOW_SIZE_PX_W, HEADER_HEIGHT))

    FONT = pygame.font.Font(None, FONT_SIZE)

    h_title = FONT.render(str(messages['title']), True, BLUE, WHITE)
    h_status = FONT.render(str(messages['status']), True, WHITE, BLACK)
    h_items = FONT.render(str(messages['items']), True, GREEN, BLACK)

    h_items_pos = h_items.get_rect(topright=(WINDOW_SIZE_PX_W, 0))

    WINDOW.blit(h_title, (0, 0))
    WINDOW.blit(h_status, (0, CELL_SIZE_PX))
    WINDOW.blit(h_items, h_items_pos)
