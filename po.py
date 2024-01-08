import random
import pygame
import sys
import os

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

width = 800
height = 800
screen = pygame.display.set_mode((width, height))
BLACK = (11, 76, 87)


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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return
        screen.blit(fon, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)


# эти класы потом нужно будет заменить
# также нужно добавить кнопку для того чтобы возвращаться обратно в меню
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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return
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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return
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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return
        screen.blit(fon, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)


def Result(screen):
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


def create_particles(position, all_sprites):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers), all_sprites)


def start_screen(screen, all_sprites):
    clock = pygame.time.Clock()
    fullname = os.path.join('data', "Gilroy-ExtraBold.otf")
    font = pygame.font.Font(fullname, 37)
    start1 = font.render(' Начать', True, BLACK)
    finish1 = font.render('Выйти', True, BLACK)
    start2 = font.render(' Начать', True, BLACK, (179, 233, 230))
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
    global Strup, Schulte, Table, Cursor, Result
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
    nota = pygame.transform.scale(load_image('нота.png'),
                                  (45, 45))
    screen.blit(nota, (0, 0))
    fullname = os.path.join('data', "Gilroy-ExtraBold.otf")
    font = pygame.font.Font(fullname, 42)
    strup1 = font.render(intro_text[0], True, BLACK)
    schulte1 = font.render(intro_text[1], True, BLACK)
    table1 = font.render(intro_text[2], True, BLACK)
    cursor11 = font.render(intro_text[3], True, BLACK)
    cursor12 = font.render(intro_text[4], True, BLACK)
    result1 = font.render(intro_text[5], True, BLACK)

    flag = False
    touch = False

    strup = Button((screen.get_width() // 2 - strup1.get_width() // 2, 200), flag, touch,
                   (strup1.get_height(), strup1.get_width()))

    schulte = Button((screen.get_width() // 2 - schulte1.get_width() // 2, 300), flag, touch,
                     (schulte1.get_height(), schulte1.get_width()))

    table = Button((screen.get_width() // 2 - table1.get_width() // 2, 400), flag, touch,
                   (table1.get_height(), table1.get_width()))

    cursor = Button((screen.get_width() // 2 - cursor12.get_width() // 2, 500), flag, touch,
                    (cursor11.get_height() + cursor12.get_height(),
                     cursor12.get_width()))

    result = Button((screen.get_width() // 2 - result1.get_width() // 2, 645), flag, touch,
                    (result1.get_height(), result1.get_width()))

    music = Button((0, 0), flag, touch, (45, 45))
    screen.blit(strup1, strup.rect_for_text)
    screen.blit(schulte1, schulte.rect_for_text)
    screen.blit(table1, table.rect_for_text)
    screen.blit(cursor11, cursor.rect_for_text)
    screen.blit(cursor12, (
        cursor.rect_for_text[0], cursor.rect_for_text[1] + 95, cursor.rect_for_text[2], cursor.rect_for_text[3]))
    screen.blit(result1, result.rect_for_text)
    group = pygame.sprite.Group(strup, schulte, table, cursor, result)
    while True:
        even_list = pygame.event.get()
        for event in even_list:
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                group.update(even_list)
                if strup.flag:
                    Strup(screen)
                    final_window(screen)
                    strup.flag = False
                elif schulte.flag:
                    Schulte(screen)
                    final_window(screen)
                    schulte.flag = False
                elif cursor.flag:
                    Cursor(screen)
                    final_window(screen)
                    cursor.flag = False
                elif table.flag:
                    Table(screen)
                    final_window(screen)
                    table.flag = False
                elif result.flag:
                    Result(screen)
                    final_window(screen)
                    result.flag = False
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
        cursor22 = font.render(intro_text[4], True, BLACK, (179, 233, 230))
        result2 = font.render(intro_text[5], True, BLACK, (179, 233, 230))

        if strup.touch:

            screen.blit(strup2, strup.rect_for_text)
        elif schulte.touch:
            screen.blit(schulte2, schulte.rect_for_text)
        elif cursor.touch:
            screen.blit(cursor21, cursor.rect_for_text)
            screen.blit(cursor22, (
                cursor.rect_for_text[0], cursor.rect_for_text[1] + 38, cursor.rect_for_text[2],
                cursor.rect_for_text[3]))
        elif table.touch:
            screen.blit(table2, table.rect_for_text)
        elif result.touch:
            screen.blit(result2, result.rect_for_text)

        screen.blit(strup1, strup.rect_for_text)
        screen.blit(schulte1, schulte.rect_for_text)
        screen.blit(table1, table.rect_for_text)
        screen.blit(cursor11, cursor.rect_for_text)
        screen.blit(cursor12, (
            cursor.rect_for_text[0], cursor.rect_for_text[1] + 38, cursor.rect_for_text[2], cursor.rect_for_text[3]))
        screen.blit(result1, result.rect_for_text)
        pygame.display.flip()
        clock.tick(FPS)


def final_window(screen):  # это окно нужно будет потом изменить (возможно здесь как раз таки и выводить результаты)
    clock = pygame.time.Clock()
    fon = pygame.transform.scale(load_image('когнетивные.png'),
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
