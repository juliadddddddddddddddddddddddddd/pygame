import pygame
import random

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (105, 0, 198)
ORANGE = (255, 102, 0)

COLORS = [RED, YELLOW, GREEN, BLUE, VIOLET, ORANGE]
COLOR_WORD = ['КРАСНЫЙ', 'ОРАНЖЕВЫЙ', 'СИНИЙ', 'ФИОЛЕТОВЫЙ', 'ЗЕЛЕНЫЙ', 'ЖЕЛТЫЙ']
width = 750
height = 750

pygame.init()
screen = pygame.display.set_mode((width, height))

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


def main():
    all_sprites = pygame.sprite.Group()
    stroop = StroopTest()
    stroop.draw_words(all_sprites)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()