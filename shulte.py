import pygame
import random
import sys

class Board:
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.font = pygame.font.SysFont(None, 40)
        self.board = [[0 for _ in range(5)] for _ in range(5)]
        self.generate_numbers()

    def generate_numbers(self):
        nums = random.sample(range(1, 5 * 5 + 1), 5 * 5)
        for i in range(5):
            for j in range(5):
                self.board[i][j] = nums[i * 5 + j]

    def draw(self, screen):
        for i in range(5):
            for j in range(5):
                number = self.board[i][j]
                text = self.font.render(str(number), True, (0, 0, 0))
                text_rect = text.get_rect(center=(j * self.cell_size + self.cell_size // 2, i * self.cell_size + self.cell_size // 2))
                screen.blit(text, text_rect)
                pygame.draw.rect(screen, pygame.Color('black'),
                                 (i * self.cell_size,
                                  j * self.cell_size,
                                  self.cell_size, self.cell_size), 1)

def main():
    pygame.init()
    width = 750
    height = 750
    screen = pygame.display.set_mode((width, height))
    board = Board(150)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255, 255, 255))
        board.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
