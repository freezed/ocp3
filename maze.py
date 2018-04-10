"""
Author: freezed <freezed@users.noreply.github.com> 2018-03-17
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [_ocp3_ project](https://github.com/freezed/ocp3)
"""
import os
import random
from conf import elmt_val, ERR_FILE, ERR_LINE, MAZE_SIZE


class Maze:
    """
    Provides a usable maze from a text file
    Checks the maze compatibility
    Moves the player to it
    """

    def __init__(self, filename):
        """
        Initialise maze

        The Maze object has given attributes:

        :var bool status: False = End of game (file error, end of game or quit)
        :var str ground: Element under player
        :var int position: Player index in string
        :var int COL_NB: column number of the maze
        :var int RANGE: string range

        :param filename: maze filename
        """
        # Loading maze file
        if os.path.isfile(filename) is False:
            self.status = False
            print(ERR_FILE.format(filename))

        else:
            with open(filename, "r") as maze_data:
                splited_maze = maze_data.read().splitlines()

            if self.check_file(splited_maze):

                # Builds a square maze (end-line spaces are missing in file)
                self.string = '\n'.join(
                    (self.check_line(line) for line in splited_maze)
                )

                # Place randomly 'item' on the maze
                for symbol_to_place in elmt_val('symbol', 'item', True):
                    position = random.choice(
                        [idx for (idx, value) in enumerate(self.string)
                         if value == elmt_val('symbol', 'name', 'floor', 0)]
                    )

                    self.set_symbol(symbol_to_place, position)

                self.MAX_ITEMS = sum(
                    1 for _ in elmt_val('name', 'item', True)
                )
                self.COL_NB = MAZE_SIZE + 1  # List starts to zero
                self.RANGE = range(self.COL_NB * MAZE_SIZE - 1)  # last EOL
                self.status = True

            else:
                self.status = False

    @staticmethod
    def check_file(splited_maze):
        """
        Checks the maze conformity before starting the game

        :param list/str splited_maze: Maze splited in a list (line = index)
        """
        if len(splited_maze) != MAZE_SIZE:
            print(ERR_LINE.format(len(splited_maze)))
            return False

        # ++Add other checks here: elements inside, exit possible, etc++
        else:
            return True

    @staticmethod
    def check_line(line):
        """
        Checks if a line has a good length (configured in MAZE_SIZE const).
        Fill it if it's too small, truncate if it's too long.
        """
        differance = MAZE_SIZE - len(str(line))
        if differance < 0:
            return line[:MAZE_SIZE]
        elif differance > 0:
            return line + (differance * elmt_val('symbol', 'name', 'floor', 0))
        else:
            return line

    def set_symbol(self, symbol, pos):
        """
        Set a symbol on the maze

        Used for 'player' and 'floor' after collecting items

        :param str symbol: the symbol to set
        :param str pos: index in the string
        """
        txt = self.string
        self.string = txt[:pos] + symbol + txt[pos + 1:]
