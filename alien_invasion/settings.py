class Settings:
    """
    Class to store all settings for the game
    """
    def __init__(self):
        self.screen_wdith = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230) # Light gray background colour

        # Ship settings
        self.ship_speed = 0.5