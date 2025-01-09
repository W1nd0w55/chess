import pygame, pieces
pygame.init()

def events(p):
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT: exit()
        elif i.type == pygame.MOUSEBUTTONDOWN: pieces.move(p)
