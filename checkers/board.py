import pygame
from .constants import BLACK, WHITE, GREY, ROWS, COLS, SQUARE_SIZE,RED
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []  # internal representation of board
        self.black_piece = self.white_piece = 12  # number of red and white pieces
        self.black_king = self.white_king = 0  # number of red and white kings
        self.initialize_board()

    def draw_empty_board(self, win):
        # draw the checkerboard
        # use pygame.draw.rect
        win.fill(GREY)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                # rect(surface, color, rect), rect = x, y , height, width, (x,y) = top-left corner coord
                pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw(self, win):
        # draw the game pieces on the board
        # call draw_board here first?
        self.draw_empty_board(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0 and piece != -1:
                    piece.draw_piece(win)


    def initialize_board(self):  # could change to add -1 to self.board
        # create the initial board
        # could use interior list for each row
        # on board square there is either piece or is empty
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row % 2 == ((col + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLACK))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(-1)
            
    def get_piece(self, row, col):
        # return piece at current location
        pass

    def move(self, piece, row, col):
        # move pieces on the board - swap location of piece curr to new
        # check if piece is king in new location
        pass

    def highlight_squares(self,win,row,col,colour):
        if row != -1 and col != -1:
            piece = Piece(row,col,colour)
            piece.draw_piece(win)
        

    def remove_circle(self,win,row,col):
        if row != -1 and col != -1:
            # if self.board[row][col] == 0:
            pygame.draw.rect(win, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        

    def move(self, row, col, new_row, new_col, colour,win):
        # move the game piece
        # pygame.draw.rect(win, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        self.board[row][col] = 0
        self.board[new_row][new_col] = Piece(new_row,new_col,colour)
        piece = self.board[new_row][new_col]
        piece.draw_piece(win)
        
