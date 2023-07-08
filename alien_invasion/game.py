import pygame
import sys
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from stats import Stats
from button import Button

class Game:
    """
    Driver class
    """
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_wdith, self.settings.screen_height))
        ### Fullscreen game. TODO Implement "QUIT" button, as pygame offers no default way to quit game while in fullscreen (no red 'x' button)
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")
        self.stats = Stats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Make the Play button
        self.play_button = Button(self, "Play")

    def run(self):
        """
        Main game loop
        """
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)   

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
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        """
        Responds to bullets hitting aliens
        """
        # Remove any bullets that have collided
            # Set first Boolean to False to make the bullet travel through entire screen
            # Set second Bollean to True always, otherwise bullets do not delete alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # Repopulate aliens
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """
        Create the fleet of aliens
        """
        alien_width, alien_height = Alien(self).rect.size
        space_available_x = self.settings.screen_wdith - (2*alien_width)
        number_aliens = space_available_x // (2*alien_width)

        # Determine number of rows of aliens that fit on screen
        ship_height = self.ship.rect.height
        space_available_y = self.settings.screen_height - (3*alien_height) - ship_height
        number_rows = space_available_y // (2 * alien_height)

        # Create full fleet of aliens
        for row in range(number_rows):
            for num in range(number_aliens):
                self._create_alien(num, row)

    def _create_alien(self, num, row):
        """
        Creates an alien and places it in the row
        """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2*alien_width*num
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2*alien_height*row
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """
        Responds appropriate if any aliens have reached an edge
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """
        Drops the entire fleet down and changes the fleet direction
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 # Change direction

    def _update_aliens(self):
        """
        Check if fleet is at edge and then update positions of all aliens in fleet
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting bottom of screen
        self._check_aliens_bottom()

    def _ship_hit(self):
        """
        Responds to ship being hit by alien
        """
        if self.stats.ships_left > 0: 
            self.stats.ships_left -= 1
        
            # Get rid of remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and center the ship
            self._create_fleet()
            self.ship.centre_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """
        Check if any aliens have reached the bottom of the screen
        """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()    # Treat same as ship being hit
                break

    def _check_play_button(self, mouse_pos):
        """
        Start a new game when player clicks play
        """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True

            # Get rid of aliens and bullets, and create new fleet
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.centre_ship()

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

        # Draw aliens
        self.aliens.draw(self.screen)

        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Display most recently drawn screen
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()

