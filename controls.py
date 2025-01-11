import pygame, pieces
pygame.init()

def events(screen, p):
    # Check events
    for i in pygame.event.get():
        if i.type == pygame.QUIT or (i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE): exit()
        elif i.type == pygame.MOUSEBUTTONDOWN: pieces.move(screen, p)
