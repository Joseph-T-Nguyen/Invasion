import pygame
import sys

class Game:
    """
    Driver class
    """
    SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))
        pygame.display.set_caption("Alien Invasion")

    def run(self):
        """
        Main game loop
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # sys.exit()  # TODO Which to use?
        
            # Display most recently drawn screen
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()

