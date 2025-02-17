import pygame
pygame.init()

class Board:
    def __init__(self, screen):
        # Board initialization
        self.screen = screen
        self.image = pygame.image.load('./images/board.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.center = self.screen_rect.center

    def render(self):
        # Board rendering
        self.screen.blit(self.image, self.rect)
