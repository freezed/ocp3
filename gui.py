"""
Author: freezed <freezed@users.noreply.github.com> 2018-04-04
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [_ocp3_ project](https://github.com/freezed/ocp3)
"""
import pygame
from conf import (
    BLACK, BLUE, CAPTION, CELL_SIZE, elmt_val, FONT_SIZE, GREEN,
    HEAD_SIZE_H, MAZE_SIZE, UNKNOWN_FILE, WIN_DIM, WIN_SIZE_W, WHITE
)


class GraphUI:
    """ Manages graphic display with pygame """

    def __init__(self):
        """
        Starts pygames magic:
        - `surface`  object
        - `font` object
        - the display clock
        """
        pygame.init()
        pygame.time.Clock().tick(25)
        pygame.display.set_caption(CAPTION)
        self.SURFACE = pygame.display.set_mode(WIN_DIM)
        self.FONT = pygame.font.Font(None, FONT_SIZE)

    def blit(self, img_file, position):
        """
        Blit an image on display

        :param str img_file:
        :param tuple position: coordinates in pixels on x/y
        """
        self.SURFACE.blit(
            pygame.image.load(img_file).convert_alpha(), position
        )

    def draw(self, maze, messages):
        """
        Take a maze string and generate a graphic maze

        :param obj maze: a Maze object
        :param list/str messages: list of messages for header
        """
        for cell, element in enumerate(maze.string.replace('\n', '')):
            img = elmt_val('tile', 'symbol', element, 0)
            x = (cell % MAZE_SIZE) * CELL_SIZE
            y = (cell // MAZE_SIZE) * CELL_SIZE + HEAD_SIZE_H

            if img is False:
                self.blit(UNKNOWN_FILE, (x, y))
            else:
                self.blit(img, (x, y))

        self.set_header(messages)

        # Refresh
        pygame.display.flip()

    def set_header(self, messages):
        """
        Set the header message on the window

        :param obj surface: surface object
        :param list/str messages: list of messages per emplacement
        """
        pygame.draw.rect(self.SURFACE, BLACK, (0, 0, WIN_SIZE_W, HEAD_SIZE_H))

        h_title = self.FONT.render(messages['title'], True, BLUE, WHITE)
        h_status = self.FONT.render(messages['status'], True, WHITE, BLACK)
        h_items = self.FONT.render(messages['items'], True, GREEN, BLACK)

        h_items_pos = h_items.get_rect(topright=(WIN_SIZE_W, 0))

        self.SURFACE.blit(h_title, (0, 0))
        self.SURFACE.blit(h_status, (0, CELL_SIZE))
        self.SURFACE.blit(h_items, h_items_pos)

    def update(self, player):
        """
        Updates GUI after a move

        :param obj player: a Player object
        """
        changed_tiles = [
            (
                elmt_val('tile', 'symbol', player.ground, 0),
                player.old_position
            ),
            (
                elmt_val('tile', 'name', 'player', 0),
                player.current_position
            ),
        ]

        [self.blit(tile[0], self.coord_from_index(tile[1]))
            for num, tile in enumerate(changed_tiles) if None not in tile]

        # Refresh
        pygame.display.flip()

    @staticmethod
    def coord_from_index(idx):
        """
        Gets 2 dimensions coordinates

        Converts a string index (the position in the maze.string: beware
        of EOL) to 2 dimensions coordinates (necessary for positionning
        objects in pygame)

        :param int index: string index
        """

        x = (idx % (MAZE_SIZE + 1)) * CELL_SIZE
        y = (idx // (MAZE_SIZE + 1)) * CELL_SIZE + HEAD_SIZE_H
        return (x, y)
