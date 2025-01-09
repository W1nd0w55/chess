import pygame, pieces
pygame.init()

def events(p):
    # Check events
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
        elif i.type == pygame.MOUSEBUTTONDOWN: pieces.move(p)
