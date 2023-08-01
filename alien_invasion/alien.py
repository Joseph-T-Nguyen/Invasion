import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    Class to represent a single alien in the fleet
    """
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load alien image and set rect attribute
        # self.image = pygame.image.load("alien_invasion/images/alien.png")
        self.image = pygame.image.load("images/alien.png")  
        self.rect = self.image.get_rect()

        # Start new alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's horizontal position
        self.x = float(self.rect.x)
    
    def update(self):
        """
        Move alien to right or left
        """
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """
        Returns True if the alien is at the edge of the screen
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    

