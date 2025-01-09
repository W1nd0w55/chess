import pygame, controls, elements, pieces
pygame.init()

def main():
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Chess')
    board = elements.Board(screen)
    p = pieces.place_all(screen)
    clock = pygame.time.Clock()
    fps = 60
    while 1:
        screen.fill((0, 0, 0))
        board.render()
        pieces.render_all(p)
        controls.events(p)
        pygame.display.update()
        clock.tick(fps)

if __name__ == '__main__': main()
