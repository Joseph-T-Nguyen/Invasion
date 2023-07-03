import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    Class to represent a single alien in the fleet
    """
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        # Load alien image and set rect attribute
        self.image = pygame.image.load("alien_invasion/images/alien.png")
        # self.image = pygame.image.load("images/alien.png")   ### TODO: Change to this before final version
        self.rect = self.image.get_rect()

        # Start new alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's horizontal position
        self.x = float(self.rect.x)

