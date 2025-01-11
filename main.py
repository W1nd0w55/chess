import pygame, controls, elements, pieces
from settings import *
pygame.init()

def main():
    # Game settings
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption(NAME)
    board = elements.Board(screen)
    p = pieces.place_all(screen)
    clock = pygame.time.Clock()
    # Main loop
    while True:
        screen.fill(BLACK)
        board.render()
        pieces.render_all(p)
        controls.events(screen, p)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__': main()
