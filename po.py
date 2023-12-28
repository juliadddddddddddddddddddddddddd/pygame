import random

import pygame
import sys
import os

GRAVITY = 0.045
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


screen_rect = (0, 0, width, height)


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, all_sprites, height=35, width=95, flag=False):
        super().__init__(all_sprites)
        self.x, self.y = pos
        self.image = load_image("кнопка.png")
        self.rect = (self.x, self.y, width, height)
        self.flag = flag

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.flag = True
                return


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy, all_sprites):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = GRAVITY

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position, all_sprites):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers), all_sprites)


def start_screen(screen, all_sprites):
    clock = pygame.time.Clock()
    for i in range(10000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 1, 1))
    font = pygame.font.SysFont('Franklin Gothic', 50)
    text = font.render('СТАРТ', True, (248, 244, 255))
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
            elif event.type == pygame.MOUSEBUTTONDOWN and not (text_x - 10 <= event.pos[0] <= (
                    text_x + text_w + 20) and text_y - 10 <= event.pos[1] <= (
                                                                       text_y + text_h + 20)):
                create_particles(pygame.mouse.get_pos(), all_sprites)
        all_sprites.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (248, 244, 255), (text_x - 10, text_y - 10,
                                                   text_w + 20, text_h + 20), 1)
        pygame.display.flip()
        clock.tick(50)

        pygame.display.flip()
        clock.tick(FPS)


def main_window(screen, all_sprites):
    clock = pygame.time.Clock()

    intro_text = ["Тест Струпа",
                  "Таблицы Шульте",
                  "Клиновидные таблицы",
                  "Курсор как инструмент",
                  "для поддержания внимания",
                  "Результат"]
    fon = pygame.transform.scale(load_image('когнетивные.png'),
                                 (width, height))
    screen.blit(fon, (0, 0))
    Strup = False
    strup = Button((100, 200), all_sprites, Strup)
    Schulte = False
    schulte = Button((100, 200), all_sprites, Schulte)
    Table = False
    table = Button((100, 200), all_sprites, Table)
    Cursor = False
    cursor = Button((100, 200), all_sprites, 75, Cursor)
    Result = False
    result = Button((100, 200), all_sprites, Result)
    font = pygame.font.SysFont('Franklin Gothic', 60)
    text_coord = 150
    for line in intro_text:
        string_rendered = font.render(line, True, (248, 244, 255))
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
        all_sprites.update()
        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def main():
    all_sprites = pygame.sprite.Group()
    start_screen(screen, all_sprites)
    main_window(screen, all_sprites)

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
