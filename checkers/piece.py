import pygame
from .constants import SQUARE_SIZE, PADDING


class Piece:
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False
        self.x = SQUARE_SIZE * col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * row + SQUARE_SIZE // 2

    def draw_piece(self, win):  # rename to "draw" ?
        # draw the game piece
        # think about how big we want piece relative to the square location
        # circle(surface, color, center, radius)
        # also draw king piece
        radius = SQUARE_SIZE//2 - PADDING
        pygame.draw.circle(win, self.colour, (self.x, self.y), radius)

    def make_king(self):
        # make into king piece
        pass

    def pos(self):
        # calc position based on row and column
        # remember that circle piece in middle of square
        pass

    def move(self, row, col):
        # move the game piece
        pass

    def __repr__(self):  # for debugging, return the colour instead of object code
        return str(self.colour)

