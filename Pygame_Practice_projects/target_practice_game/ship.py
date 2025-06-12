import pygame

class Ship:
    """A class to manage ship"""
    def __init__(self, target):
        """initialize the ship sttributes"""
        self.screen = target.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.image = pygame.transform.smoothscale(self.image, (70, 50))
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.move_up = False
        self.move_down = False 

    def update(self):
        """update the ship position"""
        if self.move_up and self.rect.top > 0:
            self.rect.y -= 4
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 4
    def reset_ship(self):
        """reset the ship on the screen"""
        self.rect.midleft = self.screen_rect.midleft
    
    def blitme(self):
        """draw ship on screen"""
        self.screen.blit(self.image, self.rect)