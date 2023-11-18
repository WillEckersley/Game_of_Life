import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 1000, 1000
TILE_SIZE = 10
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE 
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def draw_gird(positions):
    for position in positions:
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, WHITE, (*top_left, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, WHITE, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, WHITE, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))

def main():
    running = True
    positions = set()
    positions.add((10,10))

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_gird(positions)
        pygame.display.update()
        
    pygame.quit()


if __name__ == "__main__":
    main()

