import pygame


class Rocket:
    """a class to draw rocket on screen"""
    def __init__(self, ai_game):
        """initialize the game settings"""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load image of ship
        self.image = pygame.image.load("images/ship.bmp")
        self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.smoothscale(self.image, (60, 30))
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft 

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.moving_up = False
        self.moving_down = False 
    
    def update(self):
        """a class to update rocket position"""
        if self.moving_up and self.rect.top >= self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        self.rect.y = self.y

    def centered_rocket(self):
        """centerd th ship"""
        self.rect.midleft  = self.screen_rect.midleft
        self.x = float(self.rect.x)  
    
    def blitme(self):
        """draw rocket on screen"""
        self.screen.blit(self.image, self.rect)