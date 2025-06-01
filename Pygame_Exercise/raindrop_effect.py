import pygame
from random import randint
from pygame.sprite import Sprite

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Smooth Rain")
screen_rect = screen.get_rect()

# Group to hold all raindrop sprites
raindrops = pygame.sprite.Group()

class Rain(Sprite):
    """A class to represent a single raindrop"""
    def __init__(self, x, y):
        super().__init__()
        self.screen = screen

        try:
            self.image = pygame.image.load("images_1/raindrop.png")
        except FileNotFoundError:
            self.image = pygame.Surface((2, 5))
            self.image.fill((0, 255, 255))

        self.image = pygame.transform.smoothscale(self.image, (5, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Use floats for smooth movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Reduced variation in speed for smoother animation
        self.speed = randint(2, 4)

    def update(self):
        """Move the raindrop downward smoothly"""
        self.y += self.speed
        self.rect.y = int(self.y)

def _create_grid_of_raindrops():
    """Create a grid of raindrops filling the screen"""
    rain_sample = Rain(0, 0)
    rain_width = rain_sample.rect.width
    rain_height = rain_sample.rect.height

    spacing_x = rain_width + 20
    spacing_y = rain_height + 20

    number_of_raindrops = screen.get_width() // spacing_x
    number_of_rows = screen.get_height() // spacing_y

    for row in range(number_of_rows):
        for col in range(number_of_raindrops):
            x = col * spacing_x
            y = row * spacing_y
            raindrop = Rain(x, y)
            raindrops.add(raindrop)

# Create the initial grid
_create_grid_of_raindrops()

# Clock to control frame rate
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill background black
    raindrops.update()
    raindrops.draw(screen)

    # Recycle raindrops from top when they fall below
    for drop in raindrops.copy():
        if drop.rect.top >= screen_rect.bottom:
            raindrops.remove(drop)
            new_drop = Rain(randint(0, screen.get_width() - 20), -10)
            raindrops.add(new_drop)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
