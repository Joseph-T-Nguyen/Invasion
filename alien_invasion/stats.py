class Stats:
    """
    Statistics for the invasion game
    """
    def __init__(self, game):
        """
        Initialise statistics
        """
        self.settings = game.settings
        self.reset_stats()
        self.game_active = True
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
