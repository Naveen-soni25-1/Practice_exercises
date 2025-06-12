import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ A class to manage bullet"""
    def __init__(self,tr_game):
        super().__init__()
        self.screen = tr_game.screen 
        self.screen_rect  = self.screen.get_rect()

        self.bullet_color = (255, 255, 255)
        self.bullet_width = 15
        self.bullet_height = 3
        self.rect = pygame.Rect(0, 0 , self.bullet_width, self.bullet_height)
        self.rect.midright = tr_game.ship.rect.midright
        self.x = float(self.rect.x)

    def update_bullet(self):
        """ update bullet position."""
        self.x += 4
        self.rect.x = self.x

    def draw_bullet(self):
        """draw bullet on screen"""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)