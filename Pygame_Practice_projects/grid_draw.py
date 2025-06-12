import pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid Example")

def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)
            if row == mouse_y and col == mouse_x:
                pygame.draw.rect(screen, (255, 0, 0), rect)

running = True
while running:
    screen.fill((30, 30, 30))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_x = mouse_x // CELL_SIZE 
    mouse_y = mouse_y // CELL_SIZE 
    draw_grid()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
