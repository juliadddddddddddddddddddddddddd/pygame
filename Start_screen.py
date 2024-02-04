import random

import pygame
from main import load_image
from main import font_name
from main import BLACK
from main import height
from main import width
from main import Button
from main import terminate
from main import FPS
from main import star


class Particle(pygame.sprite.Sprite):
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy, all_sprites):
        from main import GRAVITY
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = GRAVITY

    def update(self):
        from main import screen_rect
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
    vol = 0.5
    font = pygame.font.Font(font_name, 39)
    font1 = pygame.font.Font(font_name, 45)
    start1 = font1.render(' Начать', True, BLACK)
    start2 = font1.render(' Начать', True, BLACK, (179, 233, 230))
    name = font.render('Приложение для развития навыков при', True, BLACK)
    name1 = font.render('подготовке к ЕГЭ по информатике', True, BLACK)
    start_x = width // 2 - start1.get_width() // 2
    start_y = 400
    start_w = start1.get_width()
    start_h = start1.get_height()
    screen.blit(start1, (start_x, start_y))
    name_x = width // 2 - name.get_width() // 2
    name_y = height // 2 - name.get_height() // 2 - 165
    screen.blit(name, (name_x, name_y))
    name1_x = width // 2 - name1.get_width() // 2
    name1_y = height // 2 - name1.get_height() // 2 - 95
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
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not (start_x - 10 <= event.pos[0] <= (
                    start_x + start_w + 20) and start_y - 10 <= event.pos[1] <= (start_y + start_h + 20))):
                star.play()
                create_particles(pygame.mouse.get_pos(), all_sprites)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                start_btn.update(even_list)
                if start_btn.flag:
                    return
            elif event.type == pygame.MOUSEMOTION:
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
        screen.blit(start1, (start_x, start_y))

        pygame.display.flip()
        clock.tick(FPS)
