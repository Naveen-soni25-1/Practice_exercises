import pygame.font 

class Button:
    """A class to make button."""
    def __init__(self, tr_game, msg):
        """ initialize button attributes and properties"""
        self.screen = tr_game.screen
        self.button_width = 100
        self.button_height = 40
        self.button_color = (0, 233, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 47)

        self.rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.rect.center = self.screen.get_rect().center
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """render the message given on the screen"""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """a function to draw button"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)