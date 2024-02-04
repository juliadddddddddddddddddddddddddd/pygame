import os
import random
import sqlite3

import pygame
from main import load_image
from main import terminate
from main import FPS


class Arrow(pygame.sprite.Sprite):
    image = load_image("arrow.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Arrow.image
        self.rect = self.image.get_rect()

    def update(self, *args):
        self.rect.topleft = args[0].pos


class TextRenderer:
    def __init__(self, screen, font, text, x, y, max_width):
        self.screen = screen
        self.font = font
        self.text = text
        self.x = x
        self.y = y
        self.max_width = max_width

    def render_text(self):
        words = [word.split(' ') for word in self.text.splitlines()]
        space = self.font.size(' ')[0]

        for line in words:
            for word in line:
                word_surface = self.font.render(word, True, (0, 0, 0))
                word_width, word_height = word_surface.get_size()
                if self.x + word_width >= self.max_width:
                    self.x = 10
                    self.y += word_height
                self.screen.blit(word_surface, (self.x, self.y))
                self.x += word_width + space
            self.x = 10
            self.y += word_height


def Cursor(screen, return_flag):
    if return_flag:
        return
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont('Times New Roman', 28)
    sec = 0
    minu = 0
    time = 0
    con = sqlite3.connect('data/tests/tests(2).db')
    cur = con.cursor()
    text = cur.execute(f"""SELECT file_name FROM text WHERE id = {random.randint(1, 2)}""").fetchone()
    with open(f'data/texts/{text[0]}', encoding='utf8') as f:
        text = f.read()
    renderer = TextRenderer(screen, font, text, 10, 10, 750)
    renderer.render_text()
    pygame.mouse.set_visible(False)
    all_sprites = pygame.sprite.Group()
    Arrow(all_sprites)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                sec += time // 1000
                minu += sec // 60
                sec = sec % 60
                if sec < 10:
                    return f'{minu}:0{sec}'
                return f'{minu}:{sec}'
            elif event.type == pygame.MOUSEMOTION:
                all_sprites.update(event)

        screen.fill((255, 255, 255))
        renderer = TextRenderer(screen, font, text, 10, 10, 750)
        renderer.render_text()
        if pygame.mouse.get_focused():
            all_sprites.draw(screen)

        pygame.display.flip()
        time += clock.tick(FPS)
