import sys

import pygame

from target import Target
from bullet import Bullet
from ship import Ship 
from button import Button 

class TargetGame:
    """a class to manage game resources"""
    def __init__(self):
        """initialize the game and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("Target Practice")
        self.bg_color = (0, 0, 0)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)
        self.clock = pygame.time.Clock()
        self.missed_bullets = 0

        self.play_button = Button(self, "play")

        self.game_active = False 

    def run_game(self):
        """start the main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.target.update()

            self.update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """check for keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mouse_click()

    def _check_keydown_events(self, events):
        """respond to keypresses."""
        if events.key == pygame.K_UP:
            self.ship.move_up = True
        elif events.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif events.key == pygame.K_SPACE:
            self._fire_bullet ()
        elif events.key == pygame.K_q:
            sys.exit()
        
    def _check_keyup_events(self, events):
        """respond to key releases."""
        if events.key == pygame.K_UP:
            self.ship.move_up = False
        elif events.key == pygame.K_DOWN:
            self.ship.move_down = False

    def _check_mouse_click(self):
        """check mouse button clicked"""
        mouse_pos = pygame.mouse.get_pos()
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.game_active = True
            self.missed_bullets = 0
            self.ship.reset_ship()
            
            pygame.mouse.set_visible(False)
            self.bullets.empty()

        
    def _fire_bullet(self):
        """create a new bullets and add it to the bullets group."""
        if len(self.bullets) < 3:
            new_bullets = Bullet(self)
            self.bullets.add(new_bullets)
    
    def _update_bullets(self):
        """ a healping method to update bullets """
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            bullet.update_bullet()
        
        for bullet in self.bullets.copy():
            if bullet.rect.x > 1200:
                self.bullets.remove(bullet)
                self.missed_bullets += 1
        
        if self.missed_bullets == 3:
            self.game_active = False
            pygame.mouse.set_visible(True)
        
    def update_screen(self):
        """update images on the screen and flip to new screen."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.target.draw_target()
        self.target._check_edge()

        if self.game_active:
            self._update_bullets()
        
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # make a game insatnce and run the game.
    target_game = TargetGame()
    target_game.run_game()