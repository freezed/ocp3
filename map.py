"""
Author: freezed <freezed@users.noreply.github.com> 2018-03-17
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [_ocp3_ project](https://github.com/freezed/ocp3)
"""
import os
import random
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT
from conf import elmt_val, ERR_MAP, MOVE_STATUS_MSG, MSG_START_GAME, MAZE_SIZE_TIL


class Map:
    """
    Provides a usable map from a text file
    Checks the map compatibility
    Moves the player to it
    """

    def __init__(self, map_file):
        """
        Initialise map

        The Map object has given attributes:

        :var int status: move status (what append after a move command)
        :var str status_message: feedback message for player
        :var lst map_in_a_list: splited map in a list
        :var str _map_in_a_string: map string
        :var str _element_under_player: Element under player
        :var int _player_position: Player index in _map_in_a_string

        :param map_file: map filename
        :rtype map: str()
        :return: None
        """
        # Chargement du fichier carte choisi
        if os.path.isfile(map_file) is True:
            with open(map_file, "r") as map_data:

                # translate to a splited lines string list
                map_in_a_list = map_data.read().splitlines()

            # map line number
            if len(map_in_a_list) == MAZE_SIZE_TIL:
                self._COLUM = MAZE_SIZE_TIL + 1
                self._LINES = MAZE_SIZE_TIL
                self._MAXIM = (self._COLUM * self._LINES) - 1
                # Add map checking here

                # Constructing square map
                map_in_a_list = [self.check_line(line) for line in map_in_a_list]
                self._map_in_a_string = '\n'.join(map_in_a_list)

                # Player's initial position
                self._player_position = self._map_in_a_string.find(
                    elmt_val('symbol', 'name', 'player', 0)
                )

                # Element under player at start
                self._element_under_player = elmt_val('symbol', 'name', 'void', 0)

                # Place collectables on the map
                for symbol_to_place in elmt_val('symbol', 'collect', True):
                    position = random.choice([idx for (idx, value) in enumerate(self._map_in_a_string) if value == elmt_val('symbol', 'name', 'void', 0)])
                    self.place_element(symbol_to_place, pos=position)

                self.status = True
                self.status_message = MSG_START_GAME
                self.collected_items = []

            else:
                self.status = False
                self.status_message = ERR_MAP.format("maplines: " + str(len(map_in_a_list)))

        # Erreur de chargement du fichier
        else:
            self.status = False
            self.status_message = ERR_MAP.format(':'.join(["mapfile", map_file]))

    def map_print(self):
        """ Affiche la carte avec la position de jeu courante """
        # print(self._map_in_a_string)
        return self._map_in_a_string

    def move_to(self, pressed_key):
        """
        Deplace le plyr sur la carte

        :param str pressed_key: mouvement souhaite
        :return int: une cle de la constante MOVE_STATUS
        """
        # supprime le plyr de son emplacement actuel et on replace
        # l'elements «dessous»
        self._map_in_a_string = self._map_in_a_string.replace(
            elmt_val('symbol', 'name', 'player', 0),
            self._element_under_player
        )

        # Recupere la position suivante
        if pressed_key == K_UP:
            next_position = self._player_position - self._COLUM

        elif pressed_key == K_DOWN:
            next_position = self._player_position + self._COLUM

        elif pressed_key == K_RIGHT:
            next_position = self._player_position + 1

        elif pressed_key == K_LEFT:
            next_position = self._player_position - 1

        self._element_under_player = elmt_val('symbol', 'name', 'void', 0)

        # Traitement en fonction de la case du prochain pas
        if next_position >= 0 and next_position <= self._MAXIM:
            next_char = self._map_in_a_string[next_position]

            if next_char == elmt_val('symbol', 'name', 'void', 0):
                self._player_position = next_position
                self.status_message = MOVE_STATUS_MSG['ok']

            elif next_char in elmt_val('symbol', 'collect', True):
                self._player_position = next_position
                self.status_message = MOVE_STATUS_MSG['collect'].format(elmt_val('name', 'symbol', next_char, 0))
                self._element_under_player = elmt_val('symbol', 'name', 'void', 0)
                self.collected_items.append(elmt_val('name', 'symbol', next_char, 0))

            elif next_char == elmt_val('symbol', 'name', 'exit', 0):
                self._player_position = next_position
                self.status = False
                self.status_message = MOVE_STATUS_MSG['exit']

            else:  # wall, door or nline
                self.status_message = MOVE_STATUS_MSG['wall']
        else:
            self.status_message = MOVE_STATUS_MSG['wall']

        # place le plyr sur sa nouvelle position
        self.place_element(elmt_val('symbol', 'name', 'player', 0))
        # Debug
        self.status_message += "|"+str(self.collected_items)

    def place_element(self, element, **kwargs):
        """
        Place l'element sur la carte.

        La position est celle de l'attribut self._player_position au
        moment de l'appel.

        Utilise pour place le plyrt et remettre les portes.

        :param str element: element a placer sur la carte
        """
        # FIXME cannot find a way to define default value to the
        # method's arguments with class attributes
        if 'pos' in kwargs:
            pos = kwargs['pos']
        else:
            pos = self._player_position

        if 'txt' in kwargs:
            txt = kwargs['txt']
        else:
            txt = self._map_in_a_string

        self._map_in_a_string = txt[:pos] + element + txt[pos + 1:]

    @staticmethod
    def check_line(line):
        """
        Checks if a line has a good length, fill it if it's too small,
        truncate if it's too long
        """
        differance = MAZE_SIZE_TIL - len(str(line))
        if differance < 0:
            return line[:MAZE_SIZE_TIL]
        elif differance > 0:
            return line + (differance * elmt_val('symbol', 'name', 'void', 0))
        else:
            return line
