import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        mole_square_x, mole_square_y = 0, 0
        mole_x_pos = 0
        mole_y_pos = 0
        screen = pygame.display.set_mode((640, 512))

        def draw_grid():
            for i in range(1, 16):
                pygame.draw.line(screen, pygame.Color(0, 0, 0), (0, 32 * i), (640, 32 * i))
            for i in range(1, 20):
                pygame.draw.line(screen, pygame.Color(0, 0, 0), (32 * i, 0), (32 * i, 512))


        clock = pygame.time.Clock()
        running = True
        while running:
            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x_pos+3, mole_y_pos+3)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y // 32
                    col = x // 32
                    if (row, col) == (mole_square_x, mole_square_y):
                        mole_x_pos = random.randrange(0, 20)*32
                        mole_y_pos = random.randrange(0, 16)*32
                        mole_square_x = mole_y_pos//32
                        mole_square_y = mole_x_pos//32
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()