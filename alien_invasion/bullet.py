import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    Class to manage bullets fired from ship
    """
    def __init__(self, game):
        """
        Create bullet at ship's current location
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.colour = self.settings.bullet_colour

        # Create bullet rect and set to correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        # Store bullet y-position as decimal
        self.y = float(self.rect.y)

    def update(self):
        """
        Move bullet vertically upwards
        """
        self.y -= self.settings.bullet_speed    # Update position of bullet
        self.rect.y = self.y                    # Update rect position

    def draw_bullet(self):
        """
        Draws bullet to the screen
        """
        pygame.draw.rect(self.screen, self.colour, self.rect)