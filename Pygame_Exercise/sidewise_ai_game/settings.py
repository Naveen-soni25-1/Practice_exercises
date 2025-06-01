class Settings:
    """a class to maintain game settings"""
    def __init__(self):
        """initializing the setting attributes"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # ship settings
        self.ship_speed = 4
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 15
        self.bullet_height  = 3
        self.bullet_color = (60, 195, 255) 
        self.bullet_speed = 4
        self.bullet_limit = 3

        # alien settings
        self.alien_speed = 1.0
        self.fleet_move_speed = .17
        self.fleet_direction = 1 
        