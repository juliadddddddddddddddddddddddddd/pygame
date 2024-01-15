import random
import sqlite3

import pygame
import sys
import os
import time

GRAVITY = 0.045
FPS = 50
pygame.mixer.pre_init(44100, -16, 1, 512)

pygame.init()
fullname = os.path.join('data', "звук_нажатия_на_кнопку.ogg")
s = pygame.mixer.Sound(fullname)
fullname = os.path.join('data', "zvuk3.wav")
star = pygame.mixer.Sound(fullname)
fullname = os.path.join('data', "музыка_на_фон.mp3")
pygame.mixer.music.load(fullname)
pygame.mixer.music.set_volume(0.5)
font_name = fullname = os.path.join('data', "Gilroy-ExtraBold.otf")
width = 750
height = 750
screen = pygame.display.set_mode((width, height))
BLACK = (11, 76, 87)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (105, 0, 198)
ORANGE = (255, 102, 0)
WHITE = (255, 255, 255)
COLORS = [RED, YELLOW, GREEN, BLUE, VIOLET, ORANGE]
COLOR_WORD = ['КРАСНЫЙ', 'ОРАНЖЕВЫЙ', 'СИНИЙ', 'ФИОЛЕТОВЫЙ', 'ЗЕЛЕНЫЙ', 'ЖЕЛТЫЙ']


def Strup(screen):
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    stroop = StroopTest()
    stroop.draw_words(all_sprites)
    vol = 0.5
    sec = 0
    minu = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        time.sleep(1)
        sec += 1
        minu += sec // 60
        sec = sec % 60
        clock.tick(FPS)


def Schulte(screen):
    clock = pygame.time.Clock()
    board = Board(150)
    vol = 0.5
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
        if sec < 10:
            time_text = font.render(f'{minu}:0{sec}', True, (0, 0, 0))
        else:
            time_text = font.render(f'{minu}:{sec}', True, (0, 0, 0))
        screen.blit(time_text, (10, 8, 60, 30))

        pygame.display.flip()
        time.sleep(1)
        sec += 1
        minu += sec // 60
        sec = sec % 60
        clock.tick(FPS)


def Table(screen):
    clock = pygame.time.Clock()
    num = RandomNumbersDisplay()
    alpth = num.generate_random_numbers(10)
    alpth1 = num.generate_additional_numbers(20)
    running = True
    sec = 0
    minu = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if sec < 10:
                    return f'{minu}:0{sec}'
                return f'{minu}:{sec}'
        num.display_numbers(alpth, alpth1)
        pygame.display.flip()

        time.sleep(1)
        sec += 1
        minu += sec // 60
        sec = sec % 60
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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return
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


def create_particles(position, all_sprites):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers), all_sprites)


screen_rect = (0, 0, width, height)


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, flag=False, touch=False, *args):
        super().__init__()
        if args:
            for i, j in args:
                self.h = i
                self.w = j
        else:
            self.h = 95
            self.w = 375
        self.x, self.y = pos
        image = load_image("кнопка1.png", (255, 255, 255))
        self.image = pygame.transform.scale(image, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect_for_text = (self.rect.x + 15, self.rect.y, self.rect.width, self.rect.height)
        self.flag = flag
        self.touch = touch

    def update(self, even_list):
        for event in even_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos):
                s.play()
                self.flag = not self.flag
            elif event.type == pygame.MOUSEMOTION and self.rect.collidepoint(event.pos):
                self.touch = True
            elif event.type == pygame.MOUSEMOTION and not (self.rect.collidepoint(event.pos)):
                self.touch = False


class StroopTest:
    def __init__(self):
        self.color_words = random.sample(COLOR_WORD, len(COLOR_WORD))
        self.colors = random.sample(COLORS, len(COLORS))
        self.font = pygame.font.Font(None, 50)

    def draw_words(self, all_sprites):
        for i in range(len(self.color_words)):
            text = self.font.render(self.color_words[i], True, self.colors[i])
            sprite = pygame.sprite.Sprite()
            sprite.image = text
            sprite.rect = sprite.image.get_rect()
            sprite.rect.y = random.randint(0, height - sprite.rect.height)
            sprite.rect.x = random.randint(0, width - sprite.rect.width)
            while pygame.sprite.spritecollideany(sprite, all_sprites):
                sprite.rect.y = random.randint(0, height - sprite.rect.height)
                sprite.rect.x = random.randint(0, width - sprite.rect.width)
            all_sprites.add(sprite)


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


class Particle(pygame.sprite.Sprite):
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy, all_sprites):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = GRAVITY

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()


def start_screen(screen, all_sprites):
    clock = pygame.time.Clock()
    vol = 0.5
    font = pygame.font.Font(font_name, 37)
    start1 = font.render(' Начать', True, BLACK)
    start2 = font.render(' Начать', True, BLACK, (179, 233, 230))
    finish1 = font.render('Выйти', True, BLACK)
    finish2 = font.render('Выйти', True, BLACK, (179, 233, 230))
    name = font.render('Приложение для развития навыков при', True, BLACK)
    name1 = font.render('подготовке к ЕГЭ по информатике', True, BLACK)
    start_x = 235
    start_y = 400
    start_w = start1.get_width()
    start_h = start1.get_height()
    screen.blit(start1, (start_x, start_y))
    finish_x = 435
    finish_y = 400
    screen.blit(finish1, (finish_x, finish_y))
    name_x = width // 2 - name.get_width() // 2
    name_y = height // 2 - name.get_height() // 2 - 175
    screen.blit(name, (name_x, name_y))
    name1_x = width // 2 - name1.get_width() // 2
    name1_y = height // 2 - name1.get_height() // 2 - 105
    screen.blit(name1, (name1_x, name1_y))
    fon = pygame.transform.scale(load_image('когнетивные2.png'),
                                 (width, height))
    nota = pygame.transform.scale(load_image('нота.png'),
                                  (45, 45))
    screen.blit(fon, (0, 0))
    screen.blit(nota, (0, 0))
    flag = False
    touch = False

    start_btn = Button((start_x, start_y), flag, touch,
                       (start1.get_height(), start1.get_width()))

    finish_btn = Button((finish_x, finish_y), flag, touch,
                        (finish1.get_height(), finish1.get_width()))
    music = Button((0, 0), flag, touch, (45, 45))
    while True:
        even_list = pygame.event.get()
        for event in even_list:
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and music.x <= event.pos[0] <= (
                    music.x + music.w) and music.y <= event.pos[1] <= (
                    music.y + music.h):
                music.update(even_list)
                if music.flag:
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.stop()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not (start_x - 10 <= event.pos[0] <= (
                    start_x + start_w + 20) and start_y - 10 <= event.pos[1] <= (
                                                                                             start_y + start_h + 20)):
                star.play()
                create_particles(pygame.mouse.get_pos(), all_sprites)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                finish_btn.update(even_list)
                start_btn.update(even_list)
                if finish_btn.flag:
                    terminate()
                elif start_btn.flag:
                    return
            elif event.type == pygame.MOUSEMOTION:
                finish_btn.update(even_list)
                start_btn.update(even_list)
                pass

        all_sprites.update()
        screen.fill((255, 255, 255))
        screen.blit(fon, (0, 0))
        screen.blit(nota, (0, 0))
        all_sprites.draw(screen)
        screen.blit(name, (name_x, name_y))
        screen.blit(name1, (name1_x, name1_y))
        if start_btn.touch:

            screen.blit(start2, (start_x, start_y))
        elif finish_btn.touch:
            screen.blit(finish2, (finish_x, finish_y))
        screen.blit(start1, (start_x, start_y))
        screen.blit(finish1, (finish_x, finish_y))

        pygame.display.flip()
        clock.tick(FPS)


def main_window(screen):
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    vol = 0.5
    con = sqlite3.connect('pygamebase.db')
    cur = con.cursor()

    intro_text = ["Тест Струпа",
                  "Таблицы Шульте",
                  "Клиновидные таблицы",
                  "Курсор"]
    fon = pygame.transform.scale(load_image('когнетивные2.png'),
                                 (width, height))
    screen.blit(fon, (0, 0))
    nota = pygame.transform.scale(load_image('нота.png'),
                                  (45, 45))
    screen.blit(nota, (0, 0))
    font = pygame.font.Font(font_name, 55)
    strup1 = font.render(intro_text[0], True, BLACK)
    schulte1 = font.render(intro_text[1], True, BLACK)
    table1 = font.render(intro_text[2], True, BLACK)
    cursor11 = font.render(intro_text[3], True, BLACK)

    flag = False
    touch = False

    strup = Button((screen.get_width() // 2 - strup1.get_width() // 2, 175), flag, touch,
                   (strup1.get_height(), strup1.get_width()))

    schulte = Button((screen.get_width() // 2 - schulte1.get_width() // 2, 300), flag, touch,
                     (schulte1.get_height(), schulte1.get_width()))

    table = Button((screen.get_width() // 2 - table1.get_width() // 2, 425), flag, touch,
                   (table1.get_height(), table1.get_width()))

    cursor = Button((screen.get_width() // 2 - cursor11.get_width() // 2, 550), flag, touch,
                    (cursor11.get_height(),
                     cursor11.get_width()))

    music = Button((0, 0), flag, touch, (45, 45))
    screen.blit(strup1, strup.rect_for_text)
    screen.blit(schulte1, schulte.rect_for_text)
    screen.blit(table1, table.rect_for_text)
    screen.blit(cursor11, cursor.rect_for_text)
    group = pygame.sprite.Group(strup, schulte, table, cursor)
    while True:
        even_list = pygame.event.get()
        for event in even_list:
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                group.update(even_list)
                if strup.flag:
                    final_window(screen)
                    cur.execute(f"""INSERT INTO Stroop(time) VALUES(?)""", (Strup(screen),))
                    con.commit()
                    strup.flag = False
                elif schulte.flag:
                    final_window(screen)
                    Schulte(screen)
                    schulte.flag = False
                elif cursor.flag:
                    final_window(screen)
                    Cursor(screen)
                    cursor.flag = False
                elif table.flag:
                    final_window(screen)
                    Table(screen)
                    table.flag = False
                elif event.type == pygame.MOUSEBUTTONDOWN and music.x <= event.pos[0] <= (
                        music.x + music.w) and music.y <= event.pos[1] <= (
                        music.y + music.h):
                    music.update(even_list)
                    if music.flag:
                        pygame.mixer.music.play(-1)
                    else:
                        pygame.mixer.music.stop()
            elif event.type == pygame.MOUSEMOTION:
                group.update(even_list)
                pass

        screen.blit(fon, (0, 0))
        screen.blit(nota, (0, 0))
        group.draw(screen)
        strup2 = font.render(intro_text[0], True, BLACK, (179, 233, 230))
        schulte2 = font.render(intro_text[1], True, BLACK, (179, 233, 230))
        table2 = font.render(intro_text[2], True, BLACK, (179, 233, 230))
        cursor21 = font.render(intro_text[3], True, BLACK, (179, 233, 230))

        if strup.touch:
            screen.blit(strup2, strup.rect_for_text)
        elif schulte.touch:
            screen.blit(schulte2, schulte.rect_for_text)
        elif cursor.touch:
            screen.blit(cursor21, cursor.rect_for_text)
        elif table.touch:
            screen.blit(table2, table.rect_for_text)

        screen.blit(strup1, strup.rect_for_text)
        screen.blit(schulte1, schulte.rect_for_text)
        screen.blit(table1, table.rect_for_text)
        screen.blit(cursor11, cursor.rect_for_text)
        pygame.display.flip()
        clock.tick(FPS)


def final_window(screen):  # это окно нужно будет потом изменить (возможно здесь как раз таки и выводить результаты)
    clock = pygame.time.Clock()
    fon = pygame.transform.scale(load_image('когнетивные2.png'),
                                 (width, height))
    font = pygame.font.Font(font_name, 37)
    start1 = font.render(' Начать', True, BLACK)
    start2 = font.render(' Начать', True, BLACK, (179, 233, 230))
    res = font.render('Предыдущие результаты', True, BLACK)
    screen.blit(fon, (0, 0))

    flag = False
    touch = False
    start_btn = Button((screen.get_width() // 2 - start1.get_width() // 2 - 15, 650), flag, touch,
                       (start1.get_height(), start1.get_width()))
    while True:
        even_list = pygame.event.get()
        for event in even_list:
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                start_btn.update(even_list)
                if start_btn.flag:
                    return
            elif event.type == pygame.MOUSEMOTION:
                start_btn.update(even_list)
                pass
        screen.blit(fon, (0, 0))
        screen.blit(res, (screen.get_width() // 2 - res.get_width() // 2, 100, res.get_height(), res.get_width()))
        screen.blit(start1, start_btn.rect_for_text)
        if start_btn.touch:
            screen.blit(start2, start_btn.rect_for_text)

        pygame.display.flip()
        clock.tick(FPS)


def main():
    all_sprites = pygame.sprite.Group()
    start_screen(screen, all_sprites)
    main_window(screen)
    final_window(screen)

    running = True
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()
        running = False

    pygame.quit()


if __name__ == '__main__':
    main()
