import pygame
import sys

from settings import Settings

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

    def run(self):
        """
        Main game loop
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
            # Redraw screen 
            self.screen.fill(self.settings.bg_colour)

            # Display most recently drawn screen
            pygame.display.flip()
        
        # Once we break out of the loop, stop the game
        pygame.quit()
        # sys.exit()  # TODO Which to use?

if __name__ == "__main__":
    game = Game()
    game.run()

