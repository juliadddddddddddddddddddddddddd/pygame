import pygame
import sys
import random

# Инициализация Pygame

# Определение базовых параметров
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH//2, y))
            screen.blit(text_surface, text_rect)
            text_surface_x_left = self.font.render(str(numbers1[2 * i]), True, (0, 0, 0))
            text_rect_x_left = text_surface.get_rect(center=(SCREEN_WIDTH // 2 + x, y))
            screen.blit(text_surface_x_left, text_rect_x_left)
            text_surface_x_right = self.font.render(str(numbers1[2 * i + 1]), True, (0, 0, 0))
            text_rect_x_right = text_surface.get_rect(center=(SCREEN_WIDTH // 2 - x, y))
            screen.blit(text_surface_x_right, text_rect_x_right)
            y += 60  # Увеличение координаты Y для следующего числа
            x += 20

def main():
    num = RandomNumbersDisplay()
    alpth = num.generate_random_numbers(10)
    alpth1 = num.generate_additional_numbers(20)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        num.display_numbers(alpth, alpth1)
        pygame.display.flip()

if __name__ == '__main__':
    main()