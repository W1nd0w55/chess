import pygame, random
pygame.init()

class Piece:
    def __init__(
    self,
    screen,
    piece: str,
    color: str,
    file: int,
    rank: int
    ):
        self.screen = screen
        self.image = pygame.image.load(f'./images/{color}_{piece}.png')
        self.file = file
        self.rank = rank
        self.rect = self.image.get_rect()

    def render(self):
        # Set piece position
        self.rect.right = self.file * 75
        self.rect.bottom = 600
        for _ in range(1, self.rank): self.rect.bottom -= 75
        # Render the piece
        self.screen.blit(self.image, self.rect)

def place_all(screen):
    return [
        # White Pawns
        Piece(screen, 'pawn', 'white', 1, 2),
        Piece(screen, 'pawn', 'white', 2, 2),
        Piece(screen, 'pawn', 'white', 3, 2),
        Piece(screen, 'pawn', 'white', 4, 2),
        Piece(screen, 'pawn', 'white', 5, 2),
        Piece(screen, 'pawn', 'white', 6, 2),
        Piece(screen, 'pawn', 'white', 7, 2),
        Piece(screen, 'pawn', 'white', 8, 2),

        # White Knights
        Piece(screen, 'knight', 'white', 2, 1),
        Piece(screen, 'knight', 'white', 7, 1),

        # White Bishops
        Piece(screen, 'bishop', 'white', 3, 1),
        Piece(screen, 'bishop', 'white', 6, 1),

        # White Rooks
        Piece(screen, 'rook', 'white', 1, 1),
        Piece(screen, 'rook', 'white', 8, 1),

        # White Family
        Piece(screen, 'queen', 'white', 4, 1),
        Piece(screen, 'king', 'white', 5, 1),

        # Black Pawns
        Piece(screen, 'pawn', 'black', 1, 7),
        Piece(screen, 'pawn', 'black', 2, 7),
        Piece(screen, 'pawn', 'black', 3, 7),
        Piece(screen, 'pawn', 'black', 4, 7),
        Piece(screen, 'pawn', 'black', 5, 7),
        Piece(screen, 'pawn', 'black', 6, 7),
        Piece(screen, 'pawn', 'black', 7, 7),
        Piece(screen, 'pawn', 'black', 8, 7),

        # Black Knights
        Piece(screen, 'knight', 'black', 2, 8),
        Piece(screen, 'knight', 'black', 7, 8),

        # Black Bishops
        Piece(screen, 'bishop', 'black', 3, 8),
        Piece(screen, 'bishop', 'black', 6, 8),

        # Black Rooks
        Piece(screen, 'rook', 'black', 1, 8),
        Piece(screen, 'rook', 'black', 8, 8),

        # Black Family
        Piece(screen, 'queen', 'black', 4, 8),
        Piece(screen, 'king', 'black', 5, 8),
    ]

def render_all(pieces):
    for i in pieces:
        # Render the piece
        i.render()

def move(pieces):
    mouse_pos = pygame.mouse.get_pos()
    for i in pieces:
        if i.rect.collidepoint(mouse_pos):
            i.rank = random.randint(1, 8)
            i.file = random.randint(1, 8)
