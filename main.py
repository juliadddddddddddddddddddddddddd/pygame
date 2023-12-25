import random

import pygame
import sys
import os

FPS = 50
pygame.init()
width = 800
height = 800
screen = pygame.display.set_mode((width, height))


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def start_screen(screen):
    clock = pygame.time.Clock()
    for i in range(10000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 1, 1))
    font = pygame.font.SysFont('Franklin Gothic', 50)
    text = font.render('СТАРТ', 50, (248, 244, 255))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (248, 244, 255), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.MOUSEBUTTONDOWN and text_x - 10 <= event.pos[0] <= (
                    text_x + text_w + 20) and text_y - 10 <= event.pos[1] <= (
                    text_y + text_h + 20):
                return

        pygame.display.flip()
        clock.tick(FPS)


def main_window(screen):
    clock = pygame.time.Clock()
    intro_text = ["Тест Струпа",
                  "Таблицы Шульте",
                  "Клиновидные таблицы",
                  "Курсор как инструмент",
                  "для поддержания внимания",
                  "Результат"]
    fon = pygame.transform.scale(load_image('fon.jpg'),
                                 (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.SysFont('Franklin Gothic', 60)
    text_coord = 150
    for line in intro_text:
        string_rendered = font.render(line, 1, (248, 244, 255))
        intro_rect = string_rendered.get_rect()
        text_coord += 35
        intro_rect.top = text_coord
        intro_rect.x = width // 2 - string_rendered.get_width() // 2
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            # elif event.type == pygame.MOUSEBUTTONDOWN and text_x - 10 <= event.pos[0] <= (
            #         text_x + text_w + 20) and text_y - 10 <= event.pos[1] <= (
            #         text_y + text_h + 20):
            #             return
        pygame.display.flip()
        clock.tick(FPS)


def main():
    start_screen(screen)
    main_window(screen)

    running = True
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()