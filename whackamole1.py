import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        mole_square_x, mole_square_y = 0, 0
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            screen.fill("light green")
            for i in range(1, 16):
                pygame.draw.line(screen, pygame.Color(0, 0, 0), (0, 32 * i), (640, 32 * i))
            for i in range(1, 20):
                pygame.draw.line(screen, pygame.Color(0, 0, 0), (32 * i, 0), (32 * i, 512))
            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y // 200
                    col = x // 200
                    if (row, col) == (mole_square_x, mole_square_y):
                        screen.blit(mole_image, mole_image.get_rect(topleft=(random.randrange(0, 640//32), random.randrange(0, 512//32))))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()