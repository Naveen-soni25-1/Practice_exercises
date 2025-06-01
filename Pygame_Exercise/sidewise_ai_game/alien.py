import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and get its rect
        self.image = pygame.image.load('images/alien.bmp')  # Use your actual image path
        self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.smoothscale(self.image, (60,40))
        self.rect = self.image.get_rect()

        # Start each new alien at a default position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien up/down based on the fleet direction."""
        self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y

        self.x -= self.settings.fleet_move_speed 
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien hits top or bottom of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0 or self.rect.bottom >= screen_rect.bottom:
            return True
        return False

