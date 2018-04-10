"""
Author: freezed <freezed@users.noreply.github.com> 2018-04-04
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [_ocp3_ project](https://github.com/freezed/ocp3)
"""
from conf import (
    elmt_val, MSG_COLLECT, MSG_LOSER, MSG_OK, MSG_WALL, MSG_WINNER,
    HEAD_MESSAGES
)
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT


class Player:
    """
    Managing the player movement
    """

    def __init__(self, maze):
        """
        Creates a player in the given maze

        :param obj maze: Maze object
        """
        self.maze = maze
        self.position = maze.string.find(
            elmt_val('symbol', 'name', 'player', 0)
        )
        # Element under player, default 'floor'
        self.ground = elmt_val('symbol', 'name', 'floor', 0)

        # Colleted items
        self.stock = []
        self.stock_num = 0

        # Contextual messages to display on each turn
        self.status_message = {}
        self.status_message['title'] = HEAD_MESSAGES['title']
        self.status_message['status'] = HEAD_MESSAGES['status']
        self.status_message['items'] = HEAD_MESSAGES['items'].format(
            self.stock_num, maze.MAX_ITEMS
        )

    def key_event(self, pressed_key):
        """
        Sets value of the new position and passes it to `move_to()`

        :param int pressed_key: direction (pygame const)
        """
        if pressed_key == K_UP:
            self.move_to(self.position - self.maze.COL_NB)

        elif pressed_key == K_DOWN:
            self.move_to(self.position + self.maze.COL_NB)

        elif pressed_key == K_RIGHT:
            self.move_to(self.position + 1)

        elif pressed_key == K_LEFT:
            self.move_to(self.position - 1)

        # ++Add other treatment for key events here (help, menu, etc.)++

    def move_to(self, next_position):
        """
        Next position treatment

        For each movement, it checks the next symbol on the maze and
        apply the corresponding rule:
        - set the new position
        - updates messages
        - collect item (if any)
        - set symbol of the leaved position
        - stop the game (win or lose)

        :param int next_position: index in self.maze.string
        """
        # in the string range
        if next_position in self.maze.RANGE:
            next_symbol = self.maze.string[next_position]

            # 'floor' element
            if next_symbol == elmt_val('symbol', 'name', 'floor', 0):
                self.position = next_position
                self.status_message['status'] = MSG_OK

            # 'item' element
            elif next_symbol in elmt_val('symbol', 'item', True):
                self.position = next_position
                self.stock.append(
                    elmt_val('name', 'symbol', next_symbol, 0)
                )
                self.stock_num += 1
                self.status_message['status'] = MSG_COLLECT.format(
                    elmt_val('name', 'symbol', next_symbol, 0)
                )
                self.status_message['items'] \
                    = HEAD_MESSAGES['items'].format(
                        self.stock_num, self.maze.MAX_ITEMS
                    )

            # 'guard' element
            elif next_symbol == elmt_val('symbol', 'name', 'guard', 0):
                self.maze.status = False

                # all 'item' are collected : player wins
                if sorted(self.stock) == sorted(
                        elmt_val('name', 'item', True)):
                    self.status_message['status'] = MSG_WINNER

                # player lose
                else:
                    missed_item_flist = ', '.join((item for item in elmt_val(
                        'name', 'item', True
                        ) if item not in self.stock))
                    self.status_message['status'] = MSG_LOSER.format(
                        missed_item_flist
                    )

            # for all other element (wall or nline)
            else:
                self.status_message['status'] = MSG_WALL

        # out the string range
        else:
            self.status_message['status'] = MSG_WALL

        # Replaces player symbol on the maze by 'ground' value
        self.maze.string = self.maze.string.replace(
            elmt_val('symbol', 'name', 'player', 0), self.ground
        )

        # Sets the player's new position
        self.maze.set_symbol(
            elmt_val('symbol', 'name', 'player', 0), self.position
        )
