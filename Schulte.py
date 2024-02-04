import pygame
import random
import sys
from main import BLACK
from main import FPS


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
                text_rect = text.get_rect(
                    center=(j * self.cell_size + self.cell_size // 2, i * self.cell_size + self.cell_size // 2))
                screen.blit(text, text_rect)
                pygame.draw.rect(screen, pygame.Color('black'),
                                 (i * self.cell_size,
                                  j * self.cell_size,
                                  self.cell_size, self.cell_size), 1)


def Schulte(screen, return_flag):
    if return_flag:
        return
    clock = pygame.time.Clock()
    board = Board(150)
    vol = 0.5
    time = 0
    sec = 0
    minu = 0
    font = pygame.font.Font(None, 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if sec < 10:
                    return f'{minu}:0{sec}'
                return f'{minu}:{sec}'
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
        screen.fill((255, 255, 255))
        board.draw(screen)

        pygame.draw.rect(screen, BLACK, (5, 5, 60, 30), 1)
        sec = 0
        minu = 0
        sec += time // 1000
        minu += sec // 60
        sec = sec % 60
        if sec < 10:
            time_text = font.render(f'{minu}:0{sec}', True, (0, 0, 0))
        else:
            time_text = font.render(f'{minu}:{sec}', True, (0, 0, 0))
        screen.blit(time_text, (10, 8, 60, 30))

        pygame.display.flip()
        time += clock.tick(FPS)
