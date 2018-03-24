"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-11
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [_ocp3_ project](https://github.com/freezed/ocp3)
"""

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
MOVE_STATUS = ['bad', 'wall', 'exit', 'collect', 'ok']
MOVE_STATUS_MSG = {
    'bad': "Le déplacement «{}» n'est pas autorisé.",
    'wall': "Le déplacement est stoppé par un mur.",
    'exit': "Vous êtes sortit du labyrinte",
    'collect': "Vous ramassez l'objet «{}»",
    'ok': "Jusqu'ici, tout va bien…"
}

CELL_SIZE_PX = 30   # Size of the tiles, in pixels
MAZE_SIZE_TIL = 15      # Size of a map, in tiles

# Messages
ERR_MAP = "ERR_MAP: «{}»"
MSG_START_GAME = "Welcome in OCP3.\nUse arrow keys to play, any other key to quit."

# Files
BACKGROUND_IMG = 'img/zebra-800.png'
MAP_FILE = '01.map'
UNKNOWN_TILE = 'img/unknown-30.png'


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