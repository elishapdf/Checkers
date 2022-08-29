import pygame
from checkers.constants import HEIGHT, WIDTH, SQUARE_SIZE,BLUE,RED
from checkers.board import Board
from checkers.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CHECKERS')

# def get_pos_of_mouse(pos):
#     # returns the row/col mouse is on

#     row = round((pos[1]*SQUARE_SIZE/8)/800)
#     col = round((pos[0]*SQUARE_SIZE/8)/800)

#     return (row,col)
#     pass


def play(pos):
    pass

if __name__ == '__main__':
    run = True
    clock = pygame.time.Clock()
    board = Board()
    game = Game(WIN)

    # game loop
    board.draw(WIN)
    pygame.display.update()
    while run:
        clock.tick(FPS) # game runs at same fps on all machines

        # check and handle events within game loop
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

            # mouse movements
            if event.type == pygame.MOUSEBUTTONDOWN:
                # pygame.display.update()
                pos = pygame.mouse.get_pos()
                game.play(pos,board,WIN)
                                
                
        
        # Board()
        # board.draw(WIN)
        pygame.display.update()

    pygame.quit()