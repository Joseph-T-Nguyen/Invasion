import pygame

class Ship:
    def __init__(self, game):
        """
        Initialise ship and set starting position

        Ship image taken at: https://www.flaticon.com/free-icon/rocket_293581
                 Image Size: 64px by 64px
        """
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load ship image and get rect
        self.image = pygame.image.load("alien_invasion/images/ship.png") # alien_invasion/... required for vscode.
        # self.image = pygame.image.load("images/ship.png") ### TODO VSCode reads file path from one file above. Uncomment for final version
        self.rect = self.image.get_rect()

        # Start new ship at bottom centre of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Ship horizontal position value
        self.x = float(self.rect.x)

        # Boolean flags for ship movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Updates ship position based on the boolean movement flags. 
        Only move within screen boundaries.
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self): 
        """
        Draw ship at current location
        """
        self.screen.blit(self.image, self.rect)