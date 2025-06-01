class GameStats:
    """a class to manage game stats"""
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        """reset the game stats"""
        self.ship_left = self.settings.ship_limit