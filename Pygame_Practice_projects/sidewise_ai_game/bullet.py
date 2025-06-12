import pygame

from pygame.sprite import Sprite

class Bullets(Sprite):
    """class to create bullets """
    def __init__(self, ai_game):
        """initialize the bullets attributes"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.rocket = ai_game.rocket

        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midright = self.rocket.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """update bullet posiion"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)