import pygame
from checkers import HEIGHT, WIDTH

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CHECKERS')

def get_pos_of_mouse(pos):
    # returns the row/col mouse is on
    pass

if __name__ == '__main__':
    run = True
    clock = pygame.time.Clock()

    # game loop
    while run:
        clock.tick(FPS) # game runs at same fps on all machines

        # check and handle events within game loop
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

            # mouse movements
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    pygame.quit()