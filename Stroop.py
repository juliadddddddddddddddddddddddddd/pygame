import random
import pygame
from main import COLOR_WORD
from main import COLORS
from main import width
from main import height
from main import FPS


def sattoloCycle(items):
    items = items.copy()
    i = len(items)
    while i > 1:
        i = i - 1
        j = random.randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]
    return items


class StroopTest:
    def __init__(self):
        self.color_words = COLOR_WORD
        self.colors = sattoloCycle(COLORS)
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


def Strup(screen, return_flag):
    if return_flag:
        return
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    stroop = StroopTest()
    stroop.draw_words(all_sprites)
    vol = 0.5
    sec = 0
    minu = 0
    time = 0
    running = True
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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        time += clock.tick(FPS)
