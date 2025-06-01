import pygame
from pygame.sprite import Sprite

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Star Grid")

# Group to hold all stars
stars = pygame.sprite.Group()

class Star(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images_1/star.bmp")
        self.image = pygame.transform.smoothscale(self.image, (40, 40))
        self.rect = self.image.get_rect()

        # Start from top-left by default
        self.x = 0
        self.y = 0

        self.x = float(self.x)

def _create_grid_of_star():
    """Create a grid of stars."""
    star = Star()
    star_width, star_height = star.rect.size

    current_x, current_y = star_width, star_height
    while current_y < (screen.get_height() - star_height):
        while current_x < (screen.get_width() - star_width):
            new_star = Star()
            new_star.rect.x = current_x
            new_star.rect.y = current_y
            stars.add(new_star)
            current_x += star_width

        current_x = star_width
        current_y += star_height

# Create stars after class and group are defined
_create_grid_of_star()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))  # Clear screen every frame
    stars.draw(screen)
    pygame.display.flip()
