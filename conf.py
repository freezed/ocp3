"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-11
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [_ocp3_ project](https://github.com/freezed/ocp3)
"""
from math import floor

ELEMENTS = (
    {'symbol': 'n', 'name': 'needle', 'cross': True, 'item': True,
     'tile': 'img/needle.png'},
    {'symbol': 't', 'name': 'tube', 'cross': True, 'item': True,
     'tile': 'img/rod.png'},
    {'symbol': 'e', 'name': 'ether', 'cross': True, 'item': True,
     'tile': 'img/ether.png'},
    {'symbol': 'E', 'name': 'guard', 'cross': False, 'item': False,
     'tile': 'img/guardian.png'},
    {'symbol': ' ', 'name': 'floor', 'cross': True, 'item': False,
     'tile': 'img/floor1.png'},
    {'symbol': '.', 'name': 'wall', 'cross': False, 'item': False,
     'tile': 'img/wall.png'},
    {'symbol': 'X', 'name': 'player', 'cross': False, 'item': False,
     'tile': 'img/macgyver.png'},
    {'symbol': '\n', 'name': 'nlin', 'cross': False, 'item': False,
     'tile': None},
)

CELL_SIZE = 30   # Size of the tiles, in pixels
MAZE_SIZE = 15   # Size of a maze, in tiles
BLACK = (0, 0, 0)
BLUE = (0, 0, 128)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Messages
CAPTION = "OCP3, a maze based on pygame"
ERR_FILE = "Maze filename is not avaiable:  «{}»"
ERR_LINE = "Maze file has wrong lines number:  «{}»"
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
MSG_WINNER = "Congratulations! You asleep the guard."

# Files
MAZE_FILE = '01.maze'
UNKNOWN_FILE = 'img/unknown-30.png'

# Constant calculation
FONT_SIZE = floor(0.9 * CELL_SIZE)
HEAD_SIZE_H = (2 * CELL_SIZE)
WIN_SIZE_W = CELL_SIZE * MAZE_SIZE
WIN_SIZE_H = WIN_SIZE_W + HEAD_SIZE_H
WIN_DIM = (WIN_SIZE_W, WIN_SIZE_H)


# FUNCTION


def elmt_val(kval, ksel, vsel, nline=False):
    """
    Return value(s) from ELEMENTS

    :param str kval: key of the value returned
    :param str ksel: key of the selection criteria
    :param str vsel: value of the selection criteria
    :param bool/int nline: Default False, return value(s) in a generator,
    use a int() to return the `n` value from a list

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
