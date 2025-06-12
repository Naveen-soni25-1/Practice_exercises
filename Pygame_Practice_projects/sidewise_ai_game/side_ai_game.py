import pygame

import sys

from time import sleep

from settings import Settings
from game_stats import GameStats
from rocket import Rocket
from bullet import Bullets 
from alien import Alien

class AlienInvasion:
    """A class to run and manage the side-scrolling alien invasion game."""
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Side-Scrolling Alien Invasion")
        self.clock = pygame.time.Clock()
        self.game_stats = GameStats(self)

        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self.create_fleet()

        # an active flage for alieninvsion game 
        self.game_active = True

    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self.rocket.update()
                self._update_bullets()
                self.update_aliens()
                
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _fire_bullets(self):
        if len(self.bullets) < self.settings.bullet_limit:
            bullet = Bullets(self)
            self.bullets.add(bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen.get_rect().right:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collision() 

    def _check_bullet_alien_collision(self):
        """respond to bullet alien collision"""
        # remove any bullet and alien that collide
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True) # dokill tell pygzme to remove that element(take boolean form )
             # sprite.groupcollide() note collision b/w two group and return dictionary containing these collision element (i.e ket bullet and value alien)
        
        if not self.aliens:
            # destroy existing bullet and call new fleet
            self.bullets.empty()
            self.create_fleet()

    def create_fleet(self):
        """Create a fleet of aliens across right side of screen."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        screen_rect = self.screen.get_rect()

        # Decide how many columns (vertical stack) and rows (horizontal spacing)
        available_vertical_space = screen_rect.height - (2 * alien_height)
        number_of_aliens_y = available_vertical_space // (2 * alien_height)

        available_horizontal_space = screen_rect.width - self.rocket.rect.width - (3 * alien_width)
        number_of_rows = available_horizontal_space // (2 * alien_width)

        for row_number in range(number_of_rows):
            for alien_number in range(number_of_aliens_y):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        alien.y = alien_height + 2 * alien_height * alien_number
        alien.rect.y = alien.y

        alien.x = self.screen.get_width() - alien_width - (2 * alien_width * row_number)
        alien.rect.x = alien.x

        self.aliens.add(alien)


    def _check_fleet_edges(self):
        """Check if any aliens hit the top/bottom and change direction."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Reverse direction."""
        self.settings.fleet_direction *= -1
    
    def update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.rocket, self.aliens):
            self._rocket_hit()
        
        self._check_alien_hit_bottom()
    
    def _rocket_hit(self):
        """rocket collide with alien"""
        if self.game_stats.ship_left > 0 :
            self.game_stats.ship_left - 1

            # destroy existing bullets and alien 
            self.aliens.empty()
            self.bullets.empty()

            # create new fleet and  start game
            self.create_fleet()
            self.rocket.centered_rocket()

            # pause the game so user can see that rocket been hit
            sleep(0.5)
        else:
            self.game_active = False

    def _check_alien_hit_bottom(self):
        """treat same as hitting the ship"""
        for alien in self.aliens.sprites():
            if alien.rect.left <= self.rocket.screen_rect.x:
                self._rocket_hit()
                break

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
