import pygame

class Board:
    def __init__(self):
        self.board = []  # internal representation of board
        self.black = self.white = 12  # number of red and white pieces
        self.black_king = self.white_king = 0 # number of red and white kings

    def draw_board(self, win):
        # draw the checkerboard
        # use pygame.draw.rect
        pass

    def draw_pieces(self, win):
        # draw the game pieces on the board
        # call draw_board here first?
        pass

    def initialize_board(self):
        # create the initial board
        # could use interior list for each row
        # on board square there is either piece or is empty
        pass

    def get_piece(self, row, col):
        # return piece at current location
        pass

    def move(self, piece, row, col):
        # move pieces on the board - swap location of piece curr to new
        # check if piece is king in new location
        pass