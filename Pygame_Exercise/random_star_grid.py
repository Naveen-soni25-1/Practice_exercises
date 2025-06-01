import pygame
from random import randint
from pygame.sprite import Sprite

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Star Grid")

stars = pygame.sprite.Group()

class Star(Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("images_1/star.bmp")
        self.image = pygame.transform.smoothscale(self.image, (40, 40))
        self.rect = self.image.get_rect()

def _create_grid_of_star():
    """Create a grid of stars with random spacing."""
    star = Star()
    star_width, star_height = star.rect.size

    # Start with a bit of randomness
    current_y = randint(0, 50)

    while current_y < (screen.get_height() - star_height):
        current_x = randint(0, 50)
        while current_x < (screen.get_width() - star_width):
            new_star = Star()
            new_star.rect.x = current_x
            new_star.rect.y = current_y
            stars.add(new_star)

            # Random spacing between stars horizontally
            current_x += star_width + randint(10, 50)

        # Random spacing vertically
        current_y += star_height + randint(10,50)

_create_grid_of_star()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))
    stars.draw(screen)
    pygame.display.flip()
