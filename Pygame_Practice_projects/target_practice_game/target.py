import pygame

class Target:
    """A class to manage the target."""

    def __init__(self, tr_game):
        """initialize the target and set its starting position."""
        self.screen = tr_game.screen
        self.target_color = (255, 0, 0)
        self.target_height = 100
        self.target_width = 10
        self.rect = pygame.Rect(1190, 300, self.target_width, self.target_height)
        self.y = float(self.rect.y)
        self.direction = 1

    def update(self):
        """update the target position continously"""
        self.y += 2 * self.direction
        self.rect.y = self.y
    
    def _check_edge(self):
        """check if trget has hit the edge of the screen"""
        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_rect().bottom:
            self.direction *= -1
            

    def draw_target(self):
        """draw target on screen"""
        pygame.draw.rect(self.screen, self.target_color, self.rect)