"""
Author: freezed <freezed@users.noreply.github.com> 2018-04-04
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [_ocp3_ project](https://github.com/freezed/ocp3)
"""
from conf import elmt_val, MSG_COLLECT, MSG_LOSER, MSG_OK, MSG_WALL, MSG_WINNER, HEAD_MESSAGES
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT


class Player:
    """
    Managing the player movement
    """

    def __init__(self, maze):
        """ Constructor """
        self.maze = maze
        self.position = maze.string.find(elmt_val('symbol', 'name', 'player', 0))
        # Element under player, default 'void'
        self.ground = elmt_val('symbol', 'name', 'void', 0)

        self.stock = []
        self.stock_num = 0

        self.status_message = {}
        self.status_message['title'] = HEAD_MESSAGES['title']
        self.status_message['status'] = HEAD_MESSAGES['status']
        self.status_message['items'] = HEAD_MESSAGES['items'].format(
            self.stock_num, maze.MAX_ITEMS
        )

    def move_to(self, pressed_key):
        """
        Move the player on the maze

        :param str pressed_key: direction (pygame const)
        """
        # Replace player symbol on the maze by 'ground'
        self.maze.string = self.maze.string.replace(
            elmt_val('symbol', 'name', 'player', 0), self.ground
        )

        if pressed_key == K_UP:
            self.next_pos(self.position - self.maze.COL_NB)

        elif pressed_key == K_DOWN:
            self.next_pos(self.position + self.maze.COL_NB)

        elif pressed_key == K_RIGHT:
            self.next_pos(self.position + 1)

        elif pressed_key == K_LEFT:
            self.next_pos(self.position - 1)

    def next_pos(self, next_position):
        """
        Next position treatment

        For each movement, it checks the next symbol on the maze and apply the corresponding rule:
        - set the new position
        - updates messages
        - collect item (if any)
        - set symbol of the leaved position
        - stop the game (win or lose)

        :param int next_position: index in self.maze.string
        """
        # is in the string range
        if next_position in self.maze.RANGE:
            next_symbol = self.maze.string[next_position]

            # is a 'void' element
            if next_symbol == elmt_val('symbol', 'name', 'void', 0):
                self.position = next_position
                self.status_message['status'] = MSG_OK

            # is a 'item' element
            elif next_symbol in elmt_val('symbol', 'item', True):
                self.position = next_position
                self.ground = elmt_val('symbol', 'name', 'void', 0)
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

            # is an 'exit' element (aka the guard)
            elif next_symbol == elmt_val('symbol', 'name', 'exit', 0):
                self.maze.status = False

                # all 'item' are collected : player wins
                if sorted(self.stock) == sorted(elmt_val('name', 'item', True)):
                    self.status_message['status'] = MSG_WINNER

                # player lose
                else:
                    missed_item_flist = ', '.join((item for item in elmt_val(
                        'name', 'item', True
                        ) if item not in self.stock))
                    self.status_message['status'] = MSG_LOSER.format(
                        missed_item_flist
                    )

            # is all other element (wall or nline)
            else:
                self.status_message['status'] = MSG_WALL

        else:
            self.status_message['status'] = MSG_WALL

        # Sets the player's new position
        self.maze.set_symbol(elmt_val('symbol', 'name', 'player', 0), self.position)
