import random

import pygame
from main import screen
from main import width
from main import FPS

class RandomNumbersDisplay:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)

    def generate_random_numbers(self, count):
        return [random.randint(1, 100) for _ in range(count)]

    def generate_additional_numbers(self, add_count):
        return [str(random.randint(1, 100)) for _ in range(add_count)]

    def display_numbers(self, numbers, numbers1):
        screen.fill((255, 255, 255))
        y = 100  # Начальная координата Y для вывода чисел
        x = 50
        for i in range(len(numbers)):
            text_surface = self.font.render(str(numbers[i]), True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(width // 2, y))
            screen.blit(text_surface, text_rect)
            text_surface_x_left = self.font.render(str(numbers1[2 * i]), True, (0, 0, 0))
            text_rect_x_left = text_surface.get_rect(center=(width // 2 + x, y))
            screen.blit(text_surface_x_left, text_rect_x_left)
            text_surface_x_right = self.font.render(str(numbers1[2 * i + 1]), True, (0, 0, 0))
            text_rect_x_right = text_surface.get_rect(center=(width // 2 - x, y))
            screen.blit(text_surface_x_right, text_rect_x_right)
            y += 60  # Увеличение координаты Y для следующего числа
            x += 20

def Table(screen):
    clock = pygame.time.Clock()
    num = RandomNumbersDisplay()
    alpth = num.generate_random_numbers(10)
    alpth1 = num.generate_additional_numbers(20)
    running = True
    time = 0
    sec = 0
    minu = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                sec += time // 1000
                minu += sec // 60
                sec = sec % 60
                if sec < 10:
                    return f'{minu}:0{sec}'
                return f'{minu}:{sec}'
        num.display_numbers(alpth, alpth1)
        pygame.display.flip()
        time += clock.tick(FPS)