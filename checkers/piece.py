import pygame


class Piece:

    def __init__(self, colour, row, col):
        self.colour = colour
        self.row = row
        self.col = col
        self.king = False
        self.x = 0
        self.y = 0

    def draw_piece(self, win):
        # draw the game piece
        # think about how big we want piece relative to the square location
        # also draw king piece
        pass

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
        return str(self.color)
