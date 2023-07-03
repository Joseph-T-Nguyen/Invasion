class Settings:
    """
    Class to store all settings for the game
    """
    def __init__(self):
        """
        Initialises game settings:
            - screen settings
            - ship settings
            - bullet settings
        """
        self._init_screen_settings()
        self._init_ship_settings()
        self._init_bullet_settings()

    def _init_screen_settings(self):
        """
        Initalises screen settings
        """
        self.screen_wdith = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230) # Light gray background colour

    def _init_ship_settings(self):
        """
        Initialises ship settings
        """
        self.ship_speed = 1.5   

    def _init_bullet_settings(self):
        """
        Initalises bullet settings
        """
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)   # Dark gray bullets
        self.bullets_allowed = 3            # Limit ammo on screen