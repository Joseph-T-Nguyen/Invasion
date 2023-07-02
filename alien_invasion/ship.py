import pygame

class Ship:
    def __init__(self, game):
        """
        Initialise ship and set starting position

        Ship image taken at: https://www.flaticon.com/free-icon/rocket_293581
        Size: 64px by 64px
        """
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load ship image and get rect
        self.image = pygame.image.load("alien_invasion/images/ship.png") # alien_invasion/... required for vscode.
        # self.image = pygame.image.load("images/ship.png") ### TODO VSCode reads file path from one file above. Uncomment for final version
        self.rect = self.image.get_rect()

        # Start new ship at bottom centre of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self): 
        """
        Draw ship at current location
        """
        self.screen.blit(self.image, self.rect)