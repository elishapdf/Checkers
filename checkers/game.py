import pygame
from checkers.constants import SQUARE_SIZE,BLUE,RED

class Game:
    def __init__(self,win):
        self.win = win

    def get_pos_of_mouse(self,pos):
    # returns the row/col mouse is on

        row = round((pos[1]*SQUARE_SIZE/8)/800)
        col = round((pos[0]*SQUARE_SIZE/8)/800)

        return (row,col)


    def get_valid_move(self,row,col,board,direction):
        while row >= 0:
            if board.board[row][col] != 0  and (board.board[row][col]).colour == (0,0,0):
                row -=1
                if direction == "right":
                    col+=1
                else:
                    col-=1

            elif board.board[row][col] == 0:
                return (row,col)

            else:
                if board.board[row][col] != 0  and (board.board[row][col]).colour == (255,0,0):
                    break


        return (-1,-1)


        pass
        



    def play(self, pos, board, WIN):

        # getting the row and col of clicked square
        pos = self.get_pos_of_mouse(pos)
        piece = board.board[pos[0]][pos[1]]
        if piece !=0 and piece != -1:
            right_diag_square = (-1,-1)
            left_diag_square = (-1,-1)
            # checking which squares will have two diagonal squares
            if pos[1] < 7:
                right_diag_square = self.get_valid_move(pos[0]-1,pos[1]+1,board,"right")
                if right_diag_square != (-1,-1):
                    board.highlight_squares(WIN,right_diag_square[0],right_diag_square[1],BLUE)
                # right_diag_square = (pos[0]-1,pos[1]+1)
                # if board.board[right_diag_square[0]][right_diag_square[1]] == 0:
                #     board.highlight_squares(WIN,right_diag_square[0],right_diag_square[1],BLUE)
                # else:
                #     right_diag_square = (-1,-1)
            if pos[1] > 0:
                left_diag_square = self.get_valid_move(pos[0]-1,pos[1]-1,board,"left")
                if left_diag_square != (-1,-1):
                    board.highlight_squares(WIN,left_diag_square[0],left_diag_square[1],BLUE)
                # left_diag_square = (pos[0]-1,pos[1]-1)
                # if board.board[left_diag_square[0]][left_diag_square[1]] == 0:
                #     board.highlight_squares(WIN,left_diag_square[0],left_diag_square[1],BLUE)
                # else:
                #     left_diag_square = (-1,-1)
            
            pygame.display.update()

            if pos[1] < 7 or pos[1] > 0:
                run1 = True
                while run1:
                    for event1 in pygame.event.get():
                        if event1.type == pygame.MOUSEBUTTONDOWN:
                            pos1 = pygame.mouse.get_pos()
                            pos1 = self.get_pos_of_mouse(pos1)
                            
                            if pos[1] < 7 or pos[1] > 0:
                                # if user moves to right
                                if pos1 == right_diag_square:
                                    board.remove_circle(WIN,right_diag_square[1],right_diag_square[0])
                                    board.remove_circle(WIN,left_diag_square[1],left_diag_square[0])
                                    board.remove_circle(WIN,pos[1],pos[0])
                                    pygame.display.update()
                                    board.move(pos[0],pos[1],right_diag_square[0],right_diag_square[1],RED,WIN)
                                    pygame.display.update()
                                    
                                elif pos1 == left_diag_square:
                                    #if user moves to left
                                    board.remove_circle(WIN,left_diag_square[1],left_diag_square[0])
                                    board.remove_circle(WIN,right_diag_square[1],right_diag_square[0])
                                    board.remove_circle(WIN,pos[1],pos[0])
                                    pygame.display.update()
                                    board.move(pos[0],pos[1],left_diag_square[0],left_diag_square[1],RED,WIN)
                                    pygame.display.update()

                                else:
                                    #user chooses another piece
                                    board.remove_circle(WIN,left_diag_square[1],left_diag_square[0])
                                    board.remove_circle(WIN,right_diag_square[1],right_diag_square[0])
                                    pygame.display.update()
                            run1 = False 



