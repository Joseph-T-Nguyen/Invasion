import pygame
import sys

from settings import Settings
from ship import Ship
from bullet import Bullet

class Game:
    """
    Driver class
    """
    SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_wdith, self.settings.screen_height))
        ### Fullscreen game. TODO Implement "QUIT" button, as pygame offers no default way to quit game while in fullscreen (no red 'x' button)
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run(self):
        """
        Main game loop
        """
        running = True
        while running:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """
        Private function to respond to keypresses and mouse events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # Call to sys.exit() closes script immediately

            # Check key press/release events
            elif event.type == pygame.KEYDOWN:  
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP: 
                self._check_keyup_events(event)   

    def _check_keydown_events(self, event):
        """
        Private function to check key presses and respond
        """   
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:   # Quit the game on press of 'Q' key
            sys.exit()  
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """
        Private function to check key releases and respond
        """ 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False   

    def _fire_bullet(self):
        """
        Create new bullet and add to bullet group
        """  
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))
    
    def _update_bullets(self):
        """
        Update bullet positions and removes bullets off the screen
        """
        # Update bullet positions
        self.bullets.update()
        
        # Get rid of bullets that are off the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """
        Private function to update images on screen and flip to new screen
        """
        # Redraw screen 
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()

        # Draw bullets fired
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Display most recently drawn screen
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()

