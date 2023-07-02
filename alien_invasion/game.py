import pygame
import sys

from settings import Settings
from ship import Ship

class Game:
    """
    Driver class
    """
    SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_wdith, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run(self):
        """
        Main game loop
        """
        running = True
        while running:
            self._check_events()
            self._update_screen()

        
    def _check_events(self):
        """
        Private function to respond to keypresses and mouse events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # Call to sys.exit() closes script immediately

    def _update_screen(self):
        """
        Private function to update images on screen and flip to new screen
        """
        # Redraw screen 
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()

        # Display most recently drawn screen
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()

