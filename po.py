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
COLOR_KOG = (3, 183, 172)


def Strup(screen):
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    fon = pygame.transform.scale(load_image('когнетивные2.png'),
                                 (width, height))
    screen.blit(fon, (0, 0))
    while True:
        even_list = pygame.event.get()
        for event in even_list:
            if event.type == pygame.QUIT:
                terminate()
        screen.blit(fon, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)


def Schulte(screen):
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    fon = pygame.transform.scale(load_image('когнетивные2.png'),
                                 (width, height))
    screen.blit(fon, (0, 0))
    while True:
        even_list = pygame.event.get()
        for event in even_list:
            if event.type == pygame.QUIT:
                terminate()
        screen.blit(fon, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)


def Table(screen):
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    fon = pygame.transform.scale(load_image('когнетивные2.png'),
                                 (width, height))
    screen.blit(fon, (0, 0))
    while True:
        even_list = pygame.event.get()
        for event in even_list:
            if event.type == pygame.QUIT:
                terminate()
        screen.blit(fon, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)


def Cursor(screen):
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    fon = pygame.transform.scale(load_image('когнетивные2.png'),
                                 (width, height))
    screen.blit(fon, (0, 0))
    while True:
        even_list = pygame.event.get()
        for event in even_list:
            if event.type == pygame.QUIT:
                terminate()
        screen.blit(fon, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)


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
    def __init__(self, pos, all_sprites, flag=False, *args):
        super().__init__(all_sprites)
        if args:
            for i, j in args:
                self.h = i
                self.w = j
        else:
            self.h = 95
            self.w = 375
        self.x, self.y = pos
        image = load_image("кнопка.png", (255, 255, 255))
        self.image = pygame.transform.scale(image, (self.w + 55, self.h + 42))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect_for_text = (self.rect.x + 25, self.rect.y + 25, self.rect.width, self.rect.height)
        self.flag = flag

    def update(self, even_list):
        for event in even_list:
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.flag = True


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
    font = pygame.font.SysFont('Franklin Gothic', 50)
    start = font.render('СТАРТ', True, COLOR_KOG)
    finish = font.render('ВЫХОД', True, COLOR_KOG)
    name = font.render('Приложение для развития навыков при', True, COLOR_KOG)
    name1 = font.render('подготовке к ЕГЭ по информатике', True, COLOR_KOG)
    start_x = 235
    start_y = 400
    start_w = start.get_width()
    start_h = start.get_height()
    screen.blit(start, (start_x, start_y))
    finish_x = 435
    finish_y = 400
    finish_w = finish.get_width()
    finish_h = finish.get_height()
    screen.blit(finish, (finish_x, finish_y))
    name_x = width // 2 - name.get_width() // 2
    name_y = height // 2 - name.get_height() // 2 - 175
    screen.blit(name, (name_x, name_y))
    name1_x = width // 2 - name1.get_width() // 2
    name1_y = height // 2 - name1.get_height() // 2 - 105
    screen.blit(name1, (name1_x, name1_y))
    pygame.draw.rect(screen, COLOR_KOG, (start_x - 10, start_y - 10,
                                         start_w + 20, start_h + 20), 5)
    pygame.draw.rect(screen, COLOR_KOG, (finish_x - 10, finish_y - 10,
                                         finish_w + 20, finish_h + 20), 5)
    pygame.draw.rect(screen, COLOR_KOG, (35, 35,
                                         width - 70, height - 70), 5)
    fon = pygame.transform.scale(load_image('когнетивные2.png'),
                                 (width, height))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.MOUSEBUTTONDOWN and start_x - 10 <= event.pos[0] <= (
                    start_x + start_w + 20) and start_y - 10 <= event.pos[1] <= (
                    start_y + start_h + 20):
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and finish_x - 10 <= event.pos[0] <= (
                    finish_x + finish_w + 20) and finish_y - 10 <= event.pos[1] <= (
                    finish_y + finish_h + 20):
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and not (start_x - 10 <= event.pos[0] <= (
                    start_x + start_w + 20) and start_y - 10 <= event.pos[1] <= (
                                                                       start_y + start_h + 20)):
                create_particles(pygame.mouse.get_pos(), all_sprites)
        all_sprites.update()
        screen.fill((255, 255, 255))
        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)
        screen.blit(name, (name_x, name_y))
        screen.blit(name1, (name1_x, name1_y))
        screen.blit(start, (start_x, start_y))
        screen.blit(finish, (finish_x, finish_y))
        pygame.draw.rect(screen, COLOR_KOG, (start_x - 10, start_y - 10,
                                             start_w + 20, start_h + 20), 5)
        pygame.draw.rect(screen, COLOR_KOG, (finish_x - 10, finish_y - 10,
                                             finish_w + 20, finish_h + 20), 5)
        pygame.draw.rect(screen, COLOR_KOG, (35, 35,
                                             width - 70, height - 70), 5)

        pygame.display.flip()
        clock.tick(FPS)


def main_window(screen, all_sprites):
    global Strup, Schulte, Table, Cursor
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))

    intro_text = ["Тест Струпа",
                  "Таблицы Шульте",
                  "Клиновидные таблицы",
                  "Курсор как инструмент",
                  "для поддержания внимания",
                  "Результат"]
    fon = pygame.transform.scale(load_image('когнетивные2.png'),
                                 (width, height))
    screen.blit(fon, (0, 0))
    # fon = pygame.Surface((width, height))
    # fon.set_alpha(20)
    # fon.blit(fon_image, (0, 0))

    pygame.draw.rect(fon, "white", fon.get_rect(), 10)

    font = pygame.font.SysFont('Franklin Gothic', 60)
    string_rendered1 = font.render(intro_text[0], True, (248, 244, 255))
    string_rendered2 = font.render(intro_text[1], True, (248, 244, 255))
    string_rendered3 = font.render(intro_text[2], True, (248, 244, 255))
    string_rendered4 = font.render(intro_text[3], True, (248, 244, 255))
    string_rendered5 = font.render(intro_text[4], True, (248, 244, 255))
    string_rendered6 = font.render(intro_text[5], True, (248, 244, 255))
    flag = False

    strup = Button((screen.get_width() // 2 - string_rendered1.get_width() // 2, 200), all_sprites, flag,
                   (string_rendered1.get_height(), string_rendered1.get_width()))

    schulte = Button((screen.get_width() // 2 - string_rendered2.get_width() // 2, 300), all_sprites, flag,
                     (string_rendered2.get_height(), string_rendered2.get_width()))

    table = Button((screen.get_width() // 2 - string_rendered3.get_width() // 2, 400), all_sprites, flag,
                   (string_rendered3.get_height(), string_rendered3.get_width()))

    cursor = Button((screen.get_width() // 2 - string_rendered5.get_width() // 2, 500), all_sprites, flag,
                    (string_rendered4.get_height() + string_rendered5.get_height(),
                     string_rendered5.get_width()))
    result = Button((screen.get_width() // 2 - string_rendered6.get_width() // 2, 645), all_sprites, flag,
                    (string_rendered6.get_height(), string_rendered6.get_width()))
    screen.blit(string_rendered1, strup.rect_for_text)
    screen.blit(string_rendered2, schulte.rect_for_text)
    screen.blit(string_rendered3, table.rect_for_text)
    screen.blit(string_rendered4, cursor.rect_for_text)
    screen.blit(string_rendered5, (
        cursor.rect_for_text[0], cursor.rect_for_text[1] + 95, cursor.rect_for_text[2], cursor.rect_for_text[3]))
    screen.blit(string_rendered6, result.rect_for_text)
    group = pygame.sprite.Group(strup, schulte, table, cursor, result)
    while True:
        even_list = pygame.event.get()
        for event in even_list:
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                group.update(even_list)
                if strup.flag:
                    Strup(screen)
                elif schulte.flag:
                    Schulte(screen)
                elif cursor.flag:
                    Cursor(screen)
                elif table.flag:
                    Table(screen)

        screen.blit(fon, (0, 0))
        group.draw(screen)

        screen.blit(string_rendered1, strup.rect_for_text)
        screen.blit(string_rendered2, schulte.rect_for_text)
        screen.blit(string_rendered3, table.rect_for_text)
        screen.blit(string_rendered4, cursor.rect_for_text)
        screen.blit(string_rendered5, (
            cursor.rect_for_text[0], cursor.rect_for_text[1] + 38, cursor.rect_for_text[2], cursor.rect_for_text[3]))
        screen.blit(string_rendered6, result.rect_for_text)
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
